#!/usr/bin/env python3
"""
Multi-strategy GitHub Search API caller for agent skill projects.

Runs 6 search queries, merges & deduplicates by repo full name,
sorts by stars descending. Computes weekly_stars by comparing
with last week's snapshot in skills_history.csv.

Usage:
    python3 scripts/search_skills.py [--top 30] [--output /path/to/output/]
"""
import argparse
import csv
import json
import os
import time
from datetime import datetime, timezone, timedelta
import requests

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "oss-radar-skill-tracker",
}
TOKEN = os.environ.get("GITHUB_TOKEN", "")
if TOKEN:
    HEADERS["Authorization"] = f"token {TOKEN}"

API = "https://api.github.com/search/repositories"

QUERIES = [
    '"agent skill" in:description',
    'skill in:description "claude code" in:description',
    'skill in:name agent in:description',
    'topic:claude-code topic:skill',
    'skill in:description "cursor" in:description',
    'skill in:description "codex" in:description',
]


def get_iso_week(d=None):
    if d is None:
        d = datetime.now(timezone.utc)
    iso = d.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def load_last_week_snapshot(history_path, current_week):
    """Load last week's total_stars from skills_history.csv."""
    if not os.path.exists(history_path):
        return {}
    last_stars = {}
    with open(history_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        weeks = {}
        for row in reader:
            week = row["week"]
            repo = row["repo"]
            stars = int(row["total_stars"])
            if week not in weeks:
                weeks[week] = {}
            weeks[week][repo] = stars
        # Find the most recent week before current_week
        earlier = sorted([w for w in weeks if w < current_week])
        if earlier:
            last_week = earlier[-1]
            last_stars = weeks[last_week]
            print(f"    [snapshot] Using {last_week} as baseline ({len(last_stars)} repos)")
        else:
            print(f"    [snapshot] No earlier week found, all weekly_stars=0")
    return last_stars


def save_snapshot(history_path, week, repos):
    """Append this week's total_stars to skills_history.csv."""
    fieldnames = ["week", "repo", "total_stars", "captured_at"]
    file_exists = os.path.exists(history_path)
    
    # Read existing to check for duplicates
    existing = set()
    if file_exists:
        with open(history_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                existing.add((row["week"], row["repo"]))
    
    with open(history_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        now = datetime.now(timezone.utc).isoformat()
        added = 0
        for r in repos:
            key = (week, r["repo"])
            if key not in existing:
                writer.writerow({
                    "week": week, "repo": r["repo"],
                    "total_stars": r["stars"], "captured_at": now,
                })
                added += 1
    print(f"    [snapshot] Saved {added} repos for {week} to {history_path}")


def search(query, per_page=30):
    params = {"q": query, "sort": "stars", "order": "desc", "per_page": per_page}
    for attempt in range(3):
        try:
            r = requests.get(API, params=params, headers=HEADERS, timeout=30)
            if r.status_code == 200:
                data = r.json()
                count = data.get("total_count", 0)
                items = data.get("items", [])
                print(f"    -> total_count={count}, fetched {len(items)}")
                return items
            elif r.status_code == 403:
                print(f"    -> rate limited, waiting 30s... (attempt {attempt+1})")
                time.sleep(30)
            else:
                print(f"    -> HTTP {r.status_code}: {r.text[:100]}")
                time.sleep(5)
        except Exception as e:
            print(f"    -> error: {e}")
            time.sleep(5)
    return []


def main():
    parser = argparse.ArgumentParser(description="Search GitHub for agent skill projects")
    parser.add_argument("--top", type=int, default=30, help="Number of top repos to output")
    parser.add_argument("--output", default=".", help="Output directory")
    parser.add_argument("--per-page", type=int, default=30, help="Results per query")
    args = parser.parse_args()

    current_week = get_iso_week()
    history_path = os.path.join(args.output, "skills_history.csv")
    
    print(f"=== skill-ranking search ({current_week}) ===")
    print(f"Strategies: {len(QUERIES)}")
    print()

    # Load last week's snapshot for weekly_stars calculation
    last_stars = load_last_week_snapshot(history_path, current_week)

    # Search
    all_repos = {}
    for i, q in enumerate(QUERIES, 1):
        print(f"[*] Search {i}/{len(QUERIES)}: {q[:60]}...")
        items = search(q, per_page=args.per_page)

        for repo in items:
            full_name = repo["full_name"]
            if full_name not in all_repos:
                all_repos[full_name] = {
                    "repo": full_name,
                    "description": (repo.get("description") or "").strip(),
                    "language": repo.get("language") or "未指定",
                    "stars": repo["stargazers_count"],
                    "forks": repo["forks_count"],
                    "topics": repo.get("topics", []),
                    "url": repo["html_url"],
                    "created_at": repo.get("created_at", "")[:10],
                    "pushed_at": repo.get("pushed_at", "")[:10],
                    "matched_queries": [q],
                }
            else:
                all_repos[full_name]["matched_queries"].append(q)

        time.sleep(2)

    # Sort by stars
    sorted_repos = sorted(all_repos.values(), key=lambda x: -x["stars"])

    # Compute weekly_stars: this week total - last week total
    for r in sorted_repos:
        prev = last_stars.get(r["repo"])
        if prev is not None:
            r["weekly_stars"] = max(0, r["stars"] - prev)
        else:
            # New entry not in last week's snapshot
            r["weekly_stars"] = 0  # Will show as "新入榜" in report

    # Save this week's snapshot
    save_snapshot(history_path, current_week, sorted_repos)

    # Print summary
    print(f"\n=== Merged: {len(sorted_repos)} unique repos ===")
    print(f"{'Rank':<5} {'⭐':>7} {'+周增':>7} {'Repo':<50} {'Lang':<12} Description")
    print("-" * 130)
    for i, r in enumerate(sorted_repos[:args.top], 1):
        desc = r["description"][:45] if r["description"] else "(no description)"
        weekly = f"+{r['weekly_stars']:,}" if r["weekly_stars"] > 0 else "—"
        print(f"{i:<5} {r['stars']:>7} {weekly:>7} {r['repo']:<50} {r['language']:<12} {desc}")

    # Save raw JSON
    os.makedirs(args.output, exist_ok=True)
    raw_path = os.path.join(args.output, "skills_raw.json")
    r["collected_week"] = current_week
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(sorted_repos, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Raw data: {raw_path}")
    print(f"     Snapshot: {history_path}")
    print(f"     Total: {len(sorted_repos)} repos, Top {args.top} shown")

    return sorted_repos


if __name__ == "__main__":
    main()
