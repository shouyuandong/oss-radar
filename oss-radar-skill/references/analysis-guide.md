# Analysis Guide — How to Determine Category/Purpose/Principle

## Overview

For each GitHub Trending repo, determine three fields:

| Field | Max Length | Language | Description |
|-------|-----------|----------|-------------|
| `category` | ~10 chars | Chinese | Tech category |
| `purpose` | ~20 chars | Chinese | One-sentence problem statement |
| `principle` | ~30 chars | Chinese | Implementation approach |

## Category Taxonomy

Use existing categories from the CSV when possible. Common categories:

### AI Agent Ecosystem
- `AI Agent 角色库` — Agent persona/role templates
- `Agent 框架` — Agent orchestration frameworks
- `Agent 技能` — Pluggable skills for coding agents (Claude Code, Cursor, etc.)
- `Agent 工程技能` — Engineering practice skills
- `Agent 审美技能` — Design/aesthetics skills
- `Agent 研究技能` — Research/information gathering skills
- `Agent 安全技能` — Security skills
- `Agent 调度` — Multi-agent scheduling/multiplexing
- `Agent 性能优化` — Agent harness optimization
- `Agent 全网访问` — Web scraping / multi-platform access for agents
- `Agent Web UI` — Web/mobile UI for agents
- `Agent 编排` — Agent team design/orchestration
- `Agent 学习` — Agent self-improvement/apprenticeship

### Infrastructure
- `代码智能 / MCP` — Code intelligence via MCP protocol
- `代码知识图谱` — Codebase as queryable knowledge graph
- `AI 记忆平台` / `AI 记忆引擎` — Persistent memory for agents
- `LLM Token 压缩` — Token compression before LLM input
- `AI 网关` — Unified AI provider gateway
- `认证授权` — Auth infrastructure (OIDC, OAuth)

### Content & Media
- `AI 视频制作` — End-to-end video production
- `AI 视频编辑` — Video editing with agents
- `AI 短视频生成` — Short video generation
- `文档转 Markdown` — Document → Markdown conversion
- `PDF 工具` — PDF manipulation

### Security
- `AI 安全测试` — AI-driven penetration testing
- `安全扫描` — Vulnerability scanning
- `安全研究` — Exploit PoC / vulnerability research

### Data & Analytics
- `AI 股票分析` — Stock market analysis
- `AI 投资研究` — Investment research
- `量化交易` — Quantitative trading
- `时序基础模型` — Time-series foundation models

### Other
- `隐私通讯` — Privacy-focused messaging
- `知识管理` — Note-taking / PKM
- `AI 设计工具` / `AI 设计语言` / `AI 设计规范` — Design-related
- `Mac 容器化` — macOS container tools
- `开发工具` — General dev tools

> When a repo doesn't fit any existing category, create a new concise one.

## Purpose — How to Write

**Formula**: `[verb] + [what it does] + [key differentiator]`

**Good examples**:
- "将代码库索引为持久知识图谱，158 语言毫秒查询" ✓
- "让 Agent 零 API 费用读取 17 个平台内容" ✓
- "一行命令用 AI Agent 克隆任意网站" ✓

**Bad examples**:
- "A powerful tool" ❌ (too vague)
- "This project helps developers" ❌ (no specifics)

## Principle — How to Write

**Formula**: `[core tech] + [how it works] + [key mechanism]`

**Good examples**:
- "C 高性能解析器构建 AST+符号引用知识图谱，MCP 暴露查询" ✓
- "不分配用户 ID，双向临时队列建立连接，路由层不存储标识" ✓
- "四位大师方法论编码为 Agent 角色，多 Agent 对抗式分析" ✓

**Bad examples**:
- "Uses AI to do things" ❌
- "Based on machine learning" ❌ (too generic)

## Decision Flow

1. Read the repo's GitHub description
2. If unclear, check the README or topics
3. Determine category (match existing or create new)
4. Write purpose (one sentence, problem-focused)
5. Write principle (one sentence, implementation-focused)
6. If description is empty/unhelpful, mark as `(待确认)` and note for later

## Quality Check

- Category should be ≤ 10 Chinese characters
- Purpose should be ≤ 25 characters, single sentence
- Principle should be ≤ 35 characters, single sentence
- Both purpose and principle should be Chinese (中文)
- No marketing language ("powerful", " revolutionary", etc.)
