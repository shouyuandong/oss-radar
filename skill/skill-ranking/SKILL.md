---
name: skill-ranking
description: Track and rank AI agent skills on GitHub. Use this skill when the user wants to discover, rank, and analyze agent-skill projects (Claude Code skills, Cursor skills, Codex skills, etc.). Triggers on requests like "skill排名"、"智能体skill"、"agent skill排行"、"更新skill排名".
---

# skill-ranking

Discover and rank AI agent skills on GitHub. Uses multi-strategy GitHub Search API to find skill projects, deduplicates by repo, sorts by stars, analyzes type/purpose/principle, and generates a Top 30 ranking report.

## When to Use

- User asks for agent skill rankings / discoveries
- Weekly scheduled execution (alongside oss-radar trending)
- User says "更新skill排名" / "有哪些agent skill" / "skill排行"

## When NOT to Use

- General GitHub trending (use oss-radar skill instead)
- Star history of one repo (use star-history.com)
- Searching for a specific known repo

## Workflow

skill-ranking runs in 5 steps:

1. **Multi-strategy search** — Run `scripts/search_skills.py` to query GitHub Search API with 6 strategies, merge & deduplicate
2. **Analyze** — For each Top 30 repo, determine `category` / `purpose` / `principle` (see `references/analysis-guide.md`)
3. **Generate report** — Write `skill-ranking/skills_top30.md` with ranking table + ecosystem analysis
4. **Save CSV** — Write `skill-ranking/skills_top30.csv` with full data
5. **Git push** — Commit and push to the oss-radar repository

## Search Strategies

The search uses 6 GitHub Search API queries to maximize coverage:

| # | Query | Coverage |
|---|-------|----------|
| 1 | `"agent skill" in:description` | Core agent-skill projects |
| 2 | `skill in:description "claude code" in:description` | Claude Code ecosystem |
| 3 | `skill in:name agent in:description` | Repos named "skill" |
| 4 | `topic:claude-code topic:skill` | Double-tagged repos |
| 5 | `skill in:description "cursor" in:description` | Cursor ecosystem |
| 6 | `skill in:description "codex" in:description` | Codex ecosystem |

Results are merged and deduplicated by `repo` full name, then sorted by `stargazers_count` descending.

## Quick Start

```bash
# Run the full pipeline
python3 scripts/search_skills.py --top 30 --output /workspace/skill-ranking/
```

The script handles steps 1 (search) automatically. Steps 2-5 (analyze, report, CSV, push) are done by the agent or orchestrated via `scripts/run_skill_ranking.py`.

## Configuration

| Config | Default | Notes |
|--------|---------|-------|
| Top N | 30 | Adjust via `--top` flag |
| Search strategies | 6 queries | Hardcoded in `search_skills.py`, can be extended |
| GitHub token | env `GITHUB_TOKEN` | Raises rate limit from 10 to 30 req/min |
| Output dir | `skill-ranking/` | Relative to repo root |

## Data Schema

CSV columns:

```
rank,repo,stars,forks,language,category,purpose,principle,url,created_at,pushed_at
```

## Resources

### scripts/
- `search_skills.py` — Multi-strategy GitHub Search API caller, outputs raw JSON
- `run_skill_ranking.py` — Full orchestrator (search → analyze → report → CSV → push)

### references/
- `analysis-guide.md` — How to categorize and analyze skill projects (shared with oss-radar skill)

## Relationship to oss-radar

| Aspect | oss-radar | skill-ranking |
|--------|-----------|---------------|
| Data source | GitHub Trending (weekly) | GitHub Search API (multi-strategy) |
| What it tracks | All trending repos | Agent skill repos only |
| Granularity | Weekly snapshot | Current snapshot (refreshed weekly) |
| Rank basis | Weekly new stars | Total stars |
| Output | `reports/{week}.md` + `all_weeks.csv` | `skill-ranking/skills_top30.md` + `.csv` |

Both run together every Monday: oss-radar tracks the broad ecosystem, skill-ranking zooms into the agent-skill niche.

## Limitations

- Search API results depend on query quality; some skill projects may be missed
- `category`/`purpose`/`principle` are AI-assisted analysis
- Total stars is a cumulative metric, not weekly growth
- Rate limit: 30 req/min with token, 10 without
