#!/usr/bin/env python3
"""
oss-radar weekly orchestrator.

Runs the full 7-step pipeline:
1. Fetch GitHub Trending (weekly)
2. Parse Top N repos
3. (Agent analyzes category/purpose/principle — done outside this script)
4. Compute rank diff vs last week
5. Generate report markdown
6. Append to all_weeks.csv
7. Git commit + push

Usage:
    python3 scripts/run_weekly.py [--top 20] [--week 2026-W28]

Note: This script handles steps 1-2, 4-7. Step 3 (analysis) must be done
by the agent — it reads the fetched data and produces category/purpose/principle.
After analysis, the agent calls compute_diff.py and append_csv.py.

For a fully agent-driven run (recommended), see references/manual-steps.md.
"""
import argparse
import csv
import json
import os
import re
import subprocess
import sys
from datetime import datetime, date

# Ensure we're in the repo root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

CSV_PATH = os.path.join(REPO_ROOT, "data/github-ranking/all_weeks.csv")
REPORTS_DIR = os.path.join(REPO_ROOT, "reports")


def get_iso_week(d=None):
    """Get ISO week string like '2026-W28'."""
    if d is None:
        d = date.today()
    iso = d.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def get_previous_week(week_str):
    """Given '2026-W28', return '2026-W27'."""
    match = re.match(r"(\d{4})-W(\d{2})", week_str)
    if not match:
        return None
    year, week = int(match.group(1)), int(match.group(2))
    # Compute the Monday of the given week
    jan4 = date(year, 1, 4)
    jan4_iso = jan4.isocalendar()
    week_monday = jan4 + datetime.timedelta(days=(week - jan4_iso.week) * 7 - (jan4_iso.weekday - 1))
    prev_monday = week_monday - datetime.timedelta(days=7)
    prev_iso = prev_monday.isocalendar()
    return f"{prev_iso.year}-W{prev_iso.week:02d}"


def read_csv():
    """Read all_weeks.csv into a list of dicts."""
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def get_last_week_data(week_str):
    """Get all rows for a given week from CSV."""
    rows = read_csv()
    return [r for r in rows if r["week"] == week_str]


def compute_rank_diff(current_repos, last_week_rows):
    """
    Compare current week's ranks with last week's.
    
    Args:
        current_repos: list of (repo, rank) tuples for this week
        last_week_rows: list of CSV row dicts from last week
    
    Returns:
        dict: repo -> change string (e.g. "🆕", "↑3", "↓2", "—")
    """
    last_week_ranks = {r["repo"]: int(r["rank"]) for r in last_week_rows}
    diffs = {}
    for repo, rank in current_repos:
        if repo not in last_week_ranks:
            diffs[repo] = "🆕"
        else:
            prev_rank = last_week_ranks[repo]
            diff = prev_rank - rank
            if diff > 0:
                diffs[repo] = f"↑{diff}"
            elif diff < 0:
                diffs[repo] = f"↓{-diff}"
            else:
                diffs[repo] = "—"
    return diffs


def append_csv(week, projects):
    """Append this week's project rows to all_weeks.csv."""
    fieldnames = ["week", "rank", "repo", "language", "weekly_stars",
                  "total_stars", "category", "purpose", "principle"]
    
    file_exists = os.path.exists(CSV_PATH)
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for p in projects:
            writer.writerow({
                "week": week,
                "rank": p["rank"],
                "repo": p["repo"],
                "language": p["language"],
                "weekly_stars": p["weekly_stars"],
                "total_stars": p["total_stars"],
                "category": p["category"],
                "purpose": p["purpose"],
                "principle": p["principle"],
            })
    print(f"[OK] Appended {len(projects)} rows to {CSV_PATH}")


def generate_report(week, projects, diffs, observations):
    """Generate reports/{week}.md."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    # Period string
    match = re.match(r"(\d{4})-W(\d{2})", week)
    year, week_num = int(match.group(1)), int(match.group(2))
    jan4 = date(year, 1, 4)
    jan4_iso = jan4.isocalendar()
    week_monday = jan4 + datetime.timedelta(days=(week_num - jan4_iso.week) * 7 - (jan4_iso.weekday - 1))
    week_sunday = week_monday + datetime.timedelta(days=6)
    period = f"{week_monday.strftime('%m.%d')} — {week_sunday.strftime('%m.%d')}"
    
    lines = [
        f"# GitHub 每周星标追踪 · {week}",
        f"",
        f"> 数据来源：oss-radar | 周期：{period} | 详见 [all_weeks.csv](../all_weeks.csv)",
        f"",
        f"---",
        f"",
        f"### 📊 本期榜单 · {week}（{period}）",
        f"",
        f"| # | 变化 | 项目 | 类型 | 语言 | 用途 | 实现原理 | 周增⭐ | 总⭐ |",
        f"|:---:|:---:|------|------|:---:|------|----------|-----:|-----:|",
    ]
    
    for p in projects:
        rank = p["rank"]
        change = diffs.get(p["repo"], "🆕")
        star = " ⭐" if rank == 1 else ""
        lines.append(
            f"| {rank} | {change} | **{p['repo']}**{star} | {p['category']} | {p['language']} | "
            f"{p['purpose']} | {p['principle']} | {p['weekly_stars']:,} | {p['total_stars']:,} |"
        )
    
    lines.append("")
    lines.append("### 🔍 本周观察")
    lines.append("")
    for obs in observations:
        lines.append(f"- {obs}")
    lines.append("")
    
    report_path = os.path.join(REPORTS_DIR, f"{week}.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print(f"[OK] Report generated: {report_path}")
    return report_path


def git_push(week):
    """Commit and push changes."""
    try:
        subprocess.run(["git", "add", "all_weeks.csv", f"reports/{week}.md"], check=True, cwd=REPO_ROOT)
        subprocess.run(
            ["git", "commit", "-m", f"feat({week}): 新增Top20报告"],
            check=True, cwd=REPO_ROOT
        )
        subprocess.run(["git", "push", "origin", "main"], check=True, cwd=REPO_ROOT)
        print(f"[OK] Pushed to GitHub: {week}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Git operation failed: {e}")
        print("You may need to manually run: git add . && git commit && git push")


def main():
    parser = argparse.ArgumentParser(description="oss-radar weekly runner")
    parser.add_argument("--top", type=int, default=20, help="Number of repos to track")
    parser.add_argument("--week", type=str, help="Override week string (e.g. 2026-W28)")
    parser.add_argument("--input", type=str, help="Path to JSON file with fetched+analyzed data")
    args = parser.parse_args()
    
    week = args.week or get_iso_week()
    prev_week = get_previous_week(week)
    
    print(f"=== oss-radar weekly run ===")
    print(f"Week: {week} (previous: {prev_week})")
    print(f"Top: {args.top}")
    print()
    
    # Load analyzed data (agent must have created this)
    if not args.input:
        print("[ERROR] --input required: path to JSON with fetched+analyzed repo data")
        print("The agent should fetch GitHub Trending, analyze category/purpose/principle,")
        print("save to a temp JSON, then run this script with --input <path>")
        print()
        print("Expected JSON format:")
        print(json.dumps({
            "week": week,
            "projects": [{
                "rank": 1,
                "repo": "owner/repo",
                "language": "Python",
                "weekly_stars": 12345,
                "total_stars": 67890,
                "category": "AI Agent",
                "purpose": "一句话用途",
                "principle": "实现原理"
            }]
        }, indent=2, ensure_ascii=False))
        sys.exit(1)
    
    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    projects = data["projects"][:args.top]
    
    # Step 4: Compute rank diff
    print(f"[Step 4] Computing rank diff vs {prev_week}...")
    last_week_rows = get_last_week_data(prev_week)
    current_repos = [(p["repo"], p["rank"]) for p in projects]
    diffs = compute_rank_diff(current_repos, last_week_rows)
    print(f"  Last week data: {len(last_week_rows)} rows")
    print(f"  New entries: {sum(1 for v in diffs.values() if v == '🆕')}")
    print(f"  Returning: {sum(1 for v in diffs.values() if v != '🆕')}")
    
    # Step 5: Generate report (observations should be in the input JSON)
    observations = data.get("observations", ["(observations to be added)"])
    print(f"[Step 5] Generating report...")
    report_path = generate_report(week, projects, diffs, observations)
    
    # Step 6: Append CSV
    print(f"[Step 6] Appending to CSV...")
    append_csv(week, projects)
    
    # Step 7: Git push
    print(f"[Step 7] Git push...")
    git_push(week)
    
    print()
    print(f"=== Done! {week} ===")
    print(f"Report: {report_path}")
    print(f"CSV: {CSV_PATH}")
    print()
    print("Top 5 this week:")
    for p in projects[:5]:
        print(f"  #{p['rank']} {p['repo']} (+{p['weekly_stars']:,})")


if __name__ == "__main__":
    main()
