# Manual Steps — Agent-Driven Execution

When scripts can't run (e.g. sandbox limitations), the agent executes these steps manually.

## Step 1: Determine Week

```python
from datetime import date
d = date.today()
iso = d.isocalendar()
week = f"{iso.year}-W{iso.week:02d}"
# Previous week:
prev = d.fromisocalendar(iso.year, iso.week - 1, 1) if iso.week > 1 else ...
```

## Step 2: Fetch GitHub Trending

Use WebFetch on `https://github.com/trending?since=weekly`:

```
Extract the top 20 repos. For each, get:
- repo path (owner/repo)
- description
- language
- weekly stars added
- total stars
```

## Step 3: Analyze

For each repo, determine three fields:
- `category`: Tech category (e.g. "AI Agent", "代码智能 / MCP", "安全测试")
- `purpose`: One sentence describing what problem it solves
- `principle`: 1-sentence implementation approach

See `analysis-guide.md` for guidance.

## Step 4: Compute Rank Diff

Read `all_weeks.csv` with pandas, find last week's rows, compare ranks:

```python
import pandas as pd
df = pd.read_csv("all_weeks.csv")
prev_week = "<previous week>"
last = df[df.week == prev_week].set_index("repo")["rank"].to_dict()
for repo, rank in current_repos:
    if repo not in last:
        change = "🆕"
    else:
        diff = last[repo] - rank
        change = f"↑{diff}" if diff > 0 else f"↓{-diff}" if diff < 0 else "—"
```

## Step 5: Generate Report

Write `reports/{week}.md`:

```markdown
# GitHub 每周星标追踪 · {week}

> 数据来源：oss-radar | 周期：{period} | 详见 [all_weeks.csv](../all_weeks.csv)

---

### 📊 本期榜单 · {week}（{period}）

| # | 变化 | 项目 | 类型 | 语言 | 用途 | 实现原理 | 周增⭐ | 总⭐ |
|:---:|:---:|------|------|:---:|------|----------|-----:|-----:|
| 1 | 🆕 | **owner/repo** ⭐ | 类型 | 语言 | 用途 | 原理 | 10,483 | 127,017 |
...

### 🔍 本周观察

- Observation 1
- Observation 2
- Observation 3
```

## Step 6: Append CSV

Append rows (DO NOT overwrite):

```python
import pandas as pd
df_old = pd.read_csv("all_weeks.csv")
df_new = pd.DataFrame(new_rows)  # same columns
df_all = pd.concat([df_old, df_new], ignore_index=True)
df_all.to_csv("all_weeks.csv", index=False)
```

## Step 7: Git Push

```bash
cd /path/to/oss-radar
git add all_weeks.csv reports/{week}.md
git commit -m "feat({week}): 新增Top20报告"
git push origin main
```

## Step 8: Report to User

Summarize Top 5 + key trends in 3-5 sentences.
