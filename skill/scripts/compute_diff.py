#!/usr/bin/env python3
"""
Compute rank changes between current and previous week.

Standalone tool — reads all_weeks.csv, compares two weeks, outputs diff.

Usage:
    python3 scripts/compute_diff.py --week 2026-W28
    python3 scripts/compute_diff.py --week 2026-W28 --prev 2026-W27
"""
import argparse
import csv
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(REPO_ROOT, "all_weeks.csv")


def read_csv():
    if not os.path.exists(CSV_PATH):
        print(f"[ERROR] CSV not found: {CSV_PATH}")
        sys.exit(1)
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def get_week_rows(rows, week):
    return [r for r in rows if r["week"] == week]


def compute_diff(current_rows, prev_rows):
    prev_ranks = {r["repo"]: int(r["rank"]) for r in prev_rows}
    diffs = {}
    for r in current_rows:
        repo = r["repo"]
        rank = int(r["rank"])
        if repo not in prev_ranks:
            diffs[repo] = "🆕"
        else:
            diff = prev_ranks[repo] - rank
            if diff > 0:
                diffs[repo] = f"↑{diff}"
            elif diff < 0:
                diffs[repo] = f"↓{-diff}"
            else:
                diffs[repo] = "—"
    return diffs


def main():
    parser = argparse.ArgumentParser(description="Compute rank diff between weeks")
    parser.add_argument("--week", required=True, help="Current week (e.g. 2026-W28)")
    parser.add_argument("--prev", help="Previous week (auto-detected if omitted)")
    args = parser.parse_args()

    rows = read_csv()
    
    # Auto-detect previous week
    if not args.prev:
        all_weeks = sorted(set(r["week"] for r in rows))
        if args.week in all_weeks:
            idx = all_weeks.index(args.week)
            if idx > 0:
                prev_week = all_weeks[idx - 1]
            else:
                prev_week = None
        else:
            # Current week not in CSV yet, find the latest week before it
            earlier = [w for w in all_weeks if w < args.week]
            prev_week = earlier[-1] if earlier else None
    else:
        prev_week = args.prev

    current_rows = get_week_rows(rows, args.week)
    if not current_rows:
        print(f"[WARN] No data for {args.week} in CSV yet.")
        print("This is expected if running before appending this week's data.")
        print("The diff will show all 🆕 if previous week exists, or note no baseline.")
        if not prev_week:
            print("\nNo previous week data found. All entries will be 🆕.")
            sys.exit(0)

    prev_rows = get_week_rows(rows, prev_week) if prev_week else []
    
    print(f"Current week: {args.week} ({len(current_rows)} repos)")
    print(f"Previous week: {prev_week} ({len(prev_rows)} repos)")
    print()
    
    if not current_rows:
        # Pre-append mode: agent has fetched data but not yet appended
        # Just show what previous week looks like for reference
        if prev_rows:
            print("Previous week's Top 5 (for reference):")
            for r in sorted(prev_rows, key=lambda x: int(x["rank"]))[:5]:
                print(f"  #{r['rank']} {r['repo']} (+{r['weekly_stars']})")
        sys.exit(0)
    
    diffs = compute_diff(current_rows, prev_rows)
    
    print(f"{'Rank':<6} {'Change':<8} {'Repo':<40} {'Prev Rank':<10}")
    print("-" * 66)
    for r in sorted(current_rows, key=lambda x: int(x["rank"])):
        repo = r["repo"]
        rank = r["rank"]
        change = diffs.get(repo, "🆕")
        prev_rank = prev_ranks.get(repo, "-") if (prev_ranks := {rr["repo"]: rr["rank"] for rr in prev_rows}) else "-"
        print(f"#{rank:<5} {change:<8} {repo:<40} {prev_rank:<10}")
    
    # Summary
    new_count = sum(1 for v in diffs.values() if v == "🆕")
    up_count = sum(1 for v in diffs.values() if v.startswith("↑"))
    down_count = sum(1 for v in diffs.values() if v.startswith("↓"))
    same_count = sum(1 for v in diffs.values() if v == "—")
    print()
    print(f"Summary: {new_count} new, {up_count} up, {down_count} down, {same_count} same")


if __name__ == "__main__":
    main()
