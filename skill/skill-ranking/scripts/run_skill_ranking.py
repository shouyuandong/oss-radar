#!/usr/bin/env python3
"""
Full orchestrator for skill-ranking: search → (agent analyzes) → report → CSV → push.

Usage:
    python3 scripts/run_skill_ranking.py [--top 30]

Note: This script handles search (step 1) and CSV/report generation (steps 3-5).
Step 2 (category/purpose/principle analysis) must be done by the agent.
After the agent analyzes, it calls this script with --input <analyzed.json>.
"""
import argparse
import csv
import json
import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(REPO_ROOT)

OUTPUT_DIR = os.path.join(REPO_ROOT, "skill-ranking")


def generate_report_and_csv(repos, top=30):
    """Generate skills_top30.md and skills_top30.csv from analyzed repo data."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # CSV
    csv_path = os.path.join(OUTPUT_DIR, "skills_top30.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "repo", "stars", "forks", "language", "category",
                     "purpose", "principle", "url", "created_at", "pushed_at"])
        for i, r in enumerate(repos[:top], 1):
            w.writerow([i, r["repo"], r["stars"], r["forks"], r["language"],
                        r.get("category", "未分类"), r.get("purpose", ""),
                        r.get("principle", ""), r["url"],
                        r["created_at"], r["pushed_at"]])
    print(f"[OK] CSV: {csv_path}")

    # MD report
    md_path = os.path.join(OUTPUT_DIR, "skills_top30.md")
    lines = [
        "# 🧩 智能体 Skill 排名 · Top " + str(top),
        "",
        f"> 通过 GitHub Search API 多策略搜索，合并去重后按总星标排序。",
        f"> 数据采集时间：{repos[0].get('collected_at', '最新采集')}",
        "",
        "---",
        "",
        "## 排名",
        "",
        "| # | 项目 | ⭐ | forks | 类型 | 语言 | 用途 | 实现原理 |",
        "|:---:|------|-----:|-----:|------|:---:|------|----------|",
    ]

    for i, r in enumerate(repos[:top], 1):
        cat = r.get("category", "未分类")
        pur = r.get("purpose", r["description"][:30] if r["description"] else "")
        pri = r.get("principle", "")
        star = " ⭐" if i <= 3 else ""
        lines.append(
            f"| {i} | **[{r['repo']}]({r['url']})**{star} | {r['stars']:,} | "
            f"{r['forks']:,} | {cat} | {r['language']} | {pur} | {pri} |"
        )

    lines += [
        "",
        "---",
        "",
        "## 生态分析",
        "",
        "*(由 agent 根据当期数据生成)*",
        "",
        "---",
        "",
        "## 数据说明",
        "",
        "- **数据源**：GitHub Search API，6 组搜索策略合并去重",
        "- **搜索策略**：`agent skill` in:description / `skill` + `claude code` / "
        "`skill` in:name + agent / `topic:claude-code` + `topic:skill` / "
        "`skill` + `cursor` / `skill` + `codex`",
        "- **排序依据**：总星标数",
        f"- **去重后项目总数**：{len(repos)} 个，本表展示 Top {top}",
        "- **category/purpose/principle** 为 AI 辅助分析，仅供参考",
    ]

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[OK] MD: {md_path}")

    return csv_path, md_path


def git_push():
    """Commit and push skill-ranking updates."""
    try:
        subprocess.run(["git", "add", "skill-ranking/"], check=True, cwd=REPO_ROOT)
        subprocess.run(
            ["git", "commit", "-m", "feat: 更新智能体 Skill 排名 Top 30"],
            check=True, cwd=REPO_ROOT
        )
        subprocess.run(["git", "push", "origin", "main"], check=True, cwd=REPO_ROOT)
        print(f"[OK] Pushed skill-ranking to GitHub")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Git failed: {e}")


def main():
    parser = argparse.ArgumentParser(description="skill-ranking orchestrator")
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--input", help="Path to analyzed JSON (skip search)")
    parser.add_argument("--search-only", action="store_true", help="Only run search, skip report")
    args = parser.parse_args()

    if args.search_only:
        # Step 1 only: search
        search_script = os.path.join(os.path.dirname(__file__), "search_skills.py")
        subprocess.run([sys.executable, search_script, "--top", str(args.top),
                        "--output", OUTPUT_DIR], check=True)
        print("\n[Next] Agent should now analyze category/purpose/principle")
        print("       Then run: python3 run_skill_ranking.py --input <analyzed.json>")
        return

    if not args.input:
        print("[ERROR] --input required: path to JSON with analyzed skill data")
        print("Run with --search-only first, then agent analyzes, then --input <path>")
        sys.exit(1)

    with open(args.input, "r", encoding="utf-8") as f:
        repos = json.load(f)

    print(f"=== skill-ranking report generation ===")
    print(f"Input: {len(repos)} repos, Top {args.top}")

    csv_path, md_path = generate_report_and_csv(repos, args.top)
    git_push()

    print(f"\n=== Done! ===")
    print(f"Top 5:")
    for i, r in enumerate(repos[:5], 1):
        print(f"  #{i} {r['repo']} ({r['stars']:,}⭐)")


if __name__ == "__main__":
    main()
