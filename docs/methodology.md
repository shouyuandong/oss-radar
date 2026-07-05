# 数据采集与分析方法论

## 数据源

| 周期 | 数据源 | 说明 |
|------|--------|------|
| W23 — W26 | [git-trending-rank.github.io](https://git-trending-rank.github.io/categories/weekly/) | 真实 GitHub Trending 周榜存档 |
| W27 起 | `github.com/trending?since=weekly` | 实时抓取 GitHub Trending |

## 采集流程

1. **抓取**：获取 GitHub Trending (weekly) 页面，提取 Top 20 项目
2. **分析**：对每个项目提取三个维度：
   - **类型**：项目所属技术类别（如 AI Agent、代码智能、安全测试）
   - **用途**：一句话说明项目解决什么问题
   - **实现原理**：核心技术的实现思路（1-2 句）
3. **排名变化**：与上一期对比，标注 ↑N / ↓N / 🆕 / —
4. **归档**：追加到 `all_weeks.csv` + 生成独立 md 报告

## 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| week | str | ISO 周号 (如 2026-W27) |
| rank | int | 当期排名 (1-20) |
| repo | str | 仓库路径 (owner/repo) |
| language | str | 主要编程语言 |
| weekly_stars | int | 本周新增星标数 |
| total_stars | int | 总星标数 |
| category | str | 技术类型分类（AI 辅助分析） |
| purpose | str | 一句话用途说明（AI 辅助分析） |
| principle | str | 实现原理简述（AI 辅助分析） |

## 注意事项

- 星标数据采集时有数小时延迟，与 GitHub 实时显示可能存在小幅差异
- `category`、`purpose`、`principle` 三列为基于项目描述的 AI 辅助分析，仅供参考
- 历史数据（W23-W26）来自第三方存档站点，项目数为该站点收录数量（19-20 个）
