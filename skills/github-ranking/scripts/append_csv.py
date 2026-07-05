#!/usr/bin/env python3
"""
Append a week's data to all_weeks.csv.

Usage:
    python3 scripts/append_csv.py --input data.json
    
Input JSON format:
{
    "week": "2026-W28",
    "projects": [
        {"rank": 1, "repo": "owner/repo", "language": "Python",
         "weekly_stars": 12345, "total_stars": 67890,
         "category": "AI Agent", "purpose": "...", "principle": "..."}
    ]
}
"""
import argparse
import csv
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(REPO_ROOT, "data/github-ranking/all_weeks.csv")

FIELDNAMES = ["week", "rank", "repo", "language", "weekly_stars",
              "total_stars", "category", "purpose", "principle"]


def main():
    parser = argparse.ArgumentParser(description="Append week data to all_weeks.csv")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    week = data["week"]
    projects = data["projects"]

    # Check for duplicates
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            existing = list(csv.DictReader(f))
        existing_weeks = set(r["week"] for r in existing)
        if week in existing_weeks:
            print(f"[WARN] Week {week} already exists in CSV!")
            print("Options:")
            print("  1. Remove existing rows for this week first:")
            print(f"     python3 -c \"import csv; rows=[r for r in csv.DictReader(open('{CSV_PATH}')) if r['week']!='{week}']; csv.DictWriter(open('{CSV_PATH}','w'),fieldnames={FIELDNAMES}).writeheader(); [csv.DictWriter(open('{CSV_PATH}','a'),fieldnames={FIELDNAMES}).writerow(r) for r in rows]\"")
            print("  2. Use a different week string")
            response = input("Overwrite? (y/N): ").strip().lower()
            if response != 'y':
                sys.exit(0)
            # Remove existing rows for this week
            rows = [r for r in existing if r["week"] != week]
            with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(rows)
            print(f"[OK] Removed existing {week} rows, will re-append")

    # Append
    file_exists = os.path.exists(CSV_PATH) and os.path.getsize(CSV_PATH) > 0
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
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

    print(f"[OK] Appended {len(projects)} rows for {week} to {CSV_PATH}")
    
    # Verify
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        total = sum(1 for _ in f) - 1  # minus header
    print(f"CSV total: {total} rows")


if __name__ == "__main__":
    main()
