#!/usr/bin/env python3
"""
Multi-strategy GitHub Search API caller for agent skill projects.

Runs 6 search queries, merges & deduplicates by repo full name,
sorts by stars descending, outputs raw JSON.

Usage:
    python3 scripts/search_skills.py [--top 30] [--output /path/to/output/]
    python3 scripts/search_skills.py --top 50 --output ./skill-ranking/
"""
import argparse
import json
import os
import time
import requests

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "oss-radar-skill-tracker",
}
TOKEN = os.environ.get("GITHUB_TOKEN", "")
if TOKEN:
    HEADERS["Authorization"] = f"token {TOKEN}"

API = "https://api.github.com/search/repositories"

# 6 search strategies for maximum coverage
QUERIES = [
    '"agent skill" in:description',
    'skill in:description "claude code" in:description',
    'skill in:name agent in:description',
    'topic:claude-code topic:skill',
    'skill in:description "cursor" in:description',
    'skill in:description "codex" in:description',
]


def search(query, per_page=30):
    """Execute one GitHub Search API query, return list of repo dicts."""
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
    parser.add_argument("--output", default=".", help="Output directory for raw JSON")
    parser.add_argument("--per-page", type=int, default=30, help="Results per query (max 30 without auth)")
    args = parser.parse_args()

    print(f"=== skill-ranking search ===")
    print(f"Strategies: {len(QUERIES)}")
    print(f"Per-page: {args.per_page}")
    print()

    all_repos = {}  # repo_full_name -> data

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

        time.sleep(2)  # avoid rate limit

    # Sort by stars
    sorted_repos = sorted(all_repos.values(), key=lambda x: -x["stars"])

    print(f"\n=== Merged: {len(sorted_repos)} unique repos ===")
    print(f"{'Rank':<5} {'Stars':>7} {'Repo':<50} {'Language':<12} Description")
    print("-" * 120)
    for i, r in enumerate(sorted_repos[:args.top], 1):
        desc = r["description"][:50] if r["description"] else "(no description)"
        print(f"{i:<5} {r['stars']:>7} {r['repo']:<50} {r['language']:<12} {desc}")

    # Save raw JSON
    os.makedirs(args.output, exist_ok=True)
    raw_path = os.path.join(args.output, "skills_raw.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(sorted_repos, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Raw data saved: {raw_path}")
    print(f"     Total unique repos: {len(sorted_repos)}")
    print(f"     Top {args.top} displayed above")

    return sorted_repos


if __name__ == "__main__":
    main()
