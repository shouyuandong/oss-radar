---
name: oss-radar
description: Track GitHub trending repositories weekly. Use this skill when the user wants to collect, analyze, and archive GitHub Trending data — specifically weekly Top-N projects with category/purpose/principle analysis and rank-change tracking. Triggers on requests like "收集GitHub Trending"、"本周热门项目"、"GitHub周报"、"更新oss-radar".
---

# oss-radar

Weekly GitHub Trending tracker. Collects Top-N trending repos, analyzes type/purpose/principle, computes rank changes vs last week, appends to CSV, generates markdown report, and pushes to a git repo.

## When to Use

- User asks to collect/track GitHub Trending (weekly)
- Scheduled weekly execution (every Monday)
- User says "更新oss-radar" / "跑一下GitHub周报" / "收集本周Trending"

## When NOT to Use

- Daily trending (this skill is weekly-only)
- Star history of a specific repo (use star-history.com instead)
- General GitHub search (use GitHub Search API directly)

## Workflow

oss-radar runs in 7 sequential steps:

1. **Determine week** — Get current date, compute ISO week number (e.g. `2026-W28`) and previous week
2. **Fetch data** — WebFetch `github.com/trending?since=weekly`, extract Top 20
3. **Analyze** — For each repo, determine `category` / `purpose` / `principle`
4. **Rank diff** — Run `scripts/compute_diff.py` to compare with last week's CSV
5. **Generate report** — Write `reports/{week}.md` with table + observations
6. **Append CSV** — Run `scripts/append_csv.py` to append this week's rows to `all_weeks.csv`
7. **Git push** — Commit and push to the oss-radar repository

## Quick Start

### First-time setup (one-time)

```bash
# Clone the repo to the working directory
git clone https://github.com/shouyuandong/oss-radar.git
cd oss-radar
```

### Weekly execution

Run `scripts/run_weekly.py` which orchestrates the full pipeline:

```bash
python3 scripts/run_weekly.py
```

This script:
1. Fetches GitHub Trending (weekly) via WebFetch
2. Asks the agent to analyze category/purpose/principle for each repo
3. Computes rank changes against last week
4. Generates `reports/{week}.md`
5. Appends rows to `all_weeks.csv`
6. Commits and pushes to git

### Manual steps (if run_weekly.py is unavailable)

The agent can execute steps manually. See `references/manual-steps.md` for the step-by-step procedure.

## Configuration

| Config | Location | Default | Notes |
|--------|----------|---------|-------|
| Repo URL | git remote `origin` | `github.com/shouyuandong/oss-radar` | Change for your own fork |
| Top N | `scripts/run_weekly.py` | 20 | Adjust to 10/25/50 |
| Git identity | repo `.git/config` | shouyuandong | Set via `git config user.email/name` |
| Git auth | remote URL (token) or keychain | — | See `references/git-setup.md` |

## Data Schema

CSV columns (see `docs/methodology.md` for full spec):

```
week,rank,repo,language,weekly_stars,total_stars,category,purpose,principle
```

- `week`: ISO week (e.g. `2026-W28`)
- `rank`: 1-N
- `category`/`purpose`/`principle`: AI-assisted analysis (Chinese)

## Resources

### scripts/
- `run_weekly.py` — Main orchestrator, runs the full 7-step pipeline
- `compute_diff.py` — Computes rank changes by comparing current week vs last week in CSV
- `append_csv.py` — Appends new week's rows to `all_weeks.csv`

### references/
- `manual-steps.md` — Step-by-step manual procedure (when scripts are unavailable)
- `git-setup.md` — Git authentication and push configuration
- `analysis-guide.md` — How to determine category/purpose/principle for a repo

## Adapting for Your Own Use

To fork and run your own oss-radar:

1. Fork the repo
2. Update git remote to your fork
3. Configure git auth (token with `public_repo` scope, or SSH key)
4. Adjust Top-N in `run_weekly.py` if needed
5. Set up a weekly cron/scheduled task to run `python3 scripts/run_weekly.py`
6. (Optional) Connect to Obsidian via Obsidian Git plugin for auto-sync

## Limitations

- GitHub Trending has no official API; data is scraped from the HTML page
- `category`/`purpose`/`principle` are AI-assisted analysis, not authoritative
- Star counts have a few hours delay vs GitHub's real-time display
- Weekly granularity only (no daily/monthly)
