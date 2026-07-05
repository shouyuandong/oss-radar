#!/usr/bin/env python3
"""
Fetch skills.sh leaderboard (All Time + Trending 24h + Hot).

Uses BeautifulSoup to parse Next.js SSR HTML.
Falls back gracefully — if parsing fails, saves raw HTML for agent debugging.

Usage:
    python3 scripts/fetch_skills_sh.py [--output /path/to/output/]
"""
import argparse
import csv
import json
import os
import re
import time
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

BASE = "https://www.skills.sh"
PAGES = {
    "all_time": f"{BASE}/",
    "trending_24h": f"{BASE}/trending",
    "hot": f"{BASE}/hot",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) oss-radar-skill-tracker",
    "Accept": "text/html,application/xhtml+xml",
}


def parse_installs(text):
    """Parse '2.3M', '625.5K', '349' to int."""
    text = text.strip().replace(",", "")
    if not text:
        return 0
    multipliers = {"K": 1000, "M": 1_000_000, "B": 1_000_000_000}
    if text[-1] in multipliers:
        try:
            return int(float(text[:-1]) * multipliers[text[-1]])
        except ValueError:
            return 0
    try:
        return int(text)
    except ValueError:
        return 0


def fetch_page(url):
    for attempt in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
            if r.status_code == 200:
                return r.text
            elif r.status_code == 429:
                print(f"    -> 429 rate limited, waiting 15s... (attempt {attempt+1})")
                time.sleep(15)
            else:
                print(f"    -> HTTP {r.status_code}")
                time.sleep(3)
        except Exception as e:
            print(f"    -> error: {e}")
            time.sleep(3)
    return None


def parse_leaderboard(html, board_type="all_time"):
    """
    Parse skills.sh leaderboard HTML using BeautifulSoup.
    
    HTML structure (per skill entry):
    <a class="group grid ..." href="/owner/repo/skill-name">
      <span class="font-mono">RANK</span>         ← rank number
      ...skill name (in <b> or text)...
      <span class="font-mono">INSTALLS</span>      ← install count (e.g., "2.3M")
    </a>
    
    For hot board, installs format is "958-109" or "250+42".
    """
    soup = BeautifulSoup(html, "html.parser")
    skills = []
    
    # Find all <a> tags that link to skill pages
    # Pattern: /owner/repo/skill-name
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Skill URLs look like /owner/repo/skill-name (3+ path segments)
        # Exclude /trending, /hot, /docs etc.
        parts = href.strip("/").split("/")
        if len(parts) < 3:
            continue
        # Skip non-skill URLs
        if parts[0] in ("trending", "hot", "docs", "api", "site"):
            continue
        
        # Extract text content
        text = a.get_text(separator=" ", strip=True)
        if not text:
            continue
        
        # The text contains: rank, skill name, owner/repo, installs
        # e.g., "1 find-skills vercel-labs/skills 2.3M"
        
        # Find rank (first number)
        rank_match = re.match(r'^(\d+)\s+', text)
        if not rank_match:
            continue
        rank = int(rank_match.group(1))
        
        # Find installs (last token, like "2.3M" or "625.5K" or "958-109")
        tokens = text.split()
        if len(tokens) < 3:
            continue
        
        # Last token is installs (or hot score for hot board)
        last_token = tokens[-1]
        
        # For hot board: format "958-109" or "250+42"
        hot_match = re.match(r'^(\d+)([+\-])(\d+)$', last_token)
        
        if board_type == "hot" and hot_match:
            hot_score = int(hot_match.group(1))
            hot_change = int(hot_match.group(3)) * (1 if hot_match.group(2) == "+" else -1)
            installs = hot_score
            installs_raw = last_token
        else:
            # Normal install count
            installs = parse_installs(last_token)
            installs_raw = last_token
            hot_score = None
            hot_change = None
        
        # Extract skill name and owner/repo
        # URL: /owner/repo/skill-name
        owner_repo = "/".join(parts[:2])
        skill_name = parts[-1] if len(parts) >= 3 else ""
        
        # Also try to find skill name from text (between rank and owner/repo)
        # text = "1 find-skills vercel-labs/skills 2.3M"
        # rank=1, last=2.3M, owner/repo=vercel-labs/skills
        # skill name = "find-skills"
        mid_tokens = tokens[1:-1]  # remove rank and installs
        # Remove owner/repo from mid_tokens
        owner_parts = owner_repo.split("/")
        mid_text = " ".join(mid_tokens)
        # Try to find owner_repo in mid_text and split
        if owner_repo in mid_text:
            idx = mid_text.index(owner_repo)
            skill_name_from_text = mid_text[:idx].strip()
            if skill_name_from_text:
                skill_name = skill_name_from_text
        
        # Deduplicate by rank (some pages have duplicate ranks from collapsed groups)
        if any(s["rank"] == rank for s in skills):
            continue
        
        skills.append({
            "rank": rank,
            "skill": skill_name,
            "owner_repo": owner_repo,
            "installs": installs,
            "installs_raw": installs_raw,
            "url": f"{BASE}{href}",
            **({"hot_score": hot_score, "hot_change": hot_change} if hot_score is not None else {}),
        })
    
    # Sort by rank
    skills.sort(key=lambda x: x["rank"])
    return skills


def main():
    parser = argparse.ArgumentParser(description="Fetch skills.sh leaderboards")
    parser.add_argument("--output", default=".", help="Output directory")
    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    
    current_week = datetime.now(timezone.utc).isocalendar()
    week_str = f"{current_week.year}-W{current_week.week:02d}"
    
    print(f"=== skills.sh fetch ({week_str}) ===\n")
    
    results = {}
    
    for name, url in PAGES.items():
        print(f"[*] Fetching {name}: {url}")
        html = fetch_page(url)
        
        if not html:
            print(f"    -> FAILED, skipping {name}")
            results[name] = []
            continue
        
        skills = parse_leaderboard(html, board_type=name)
        print(f"    -> Parsed {len(skills)} skills")
        
        if len(skills) == 0:
            raw_path = os.path.join(args.output, f"skills_sh_{name}_raw.html")
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"    -> Parsing returned 0! Raw HTML saved to {raw_path}")
            print(f"    -> Agent should inspect and adjust parsing.")
        
        if skills:
            print(f"    -> Top 3:")
            for s in skills[:3]:
                print(f"       #{s['rank']} {s['skill']} ({s['owner_repo']}) — {s['installs_raw']}")
        
        results[name] = skills
        time.sleep(2)
    
    # Save JSON
    output = {
        "week": week_str,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "source": "skills.sh",
        "leaderboards": results,
    }
    
    json_path = os.path.join(args.output, "skills_sh_raw.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] JSON: {json_path}")
    
    # Save flat CSV (all_time as primary)
    csv_path = os.path.join(args.output, "skills_sh_snapshot.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["week", "rank", "skill", "owner_repo", "installs", "installs_raw", "url"])
        for s in results.get("all_time", []):
            w.writerow([week_str, s["rank"], s["skill"], s["owner_repo"],
                        s["installs"], s["installs_raw"], s["url"]])
    print(f"[OK] CSV: {csv_path}")
    
    # Summary
    print(f"\n=== Summary ===")
    for name, skills in results.items():
        if skills:
            print(f"{name}: {len(skills)} skills, #1 = {skills[0]['skill']} ({skills[0]['installs_raw']})")
        else:
            print(f"{name}: FAILED")


if __name__ == "__main__":
    main()
