# GitHub 每周星标追踪

> 自动化收集 GitHub 每周最受关注的 **Top 20** 项目，分析其类型、用途与实现原理，并追踪排名变化。
>
> - **更新频率**：每周一 09:00（Asia/Shanghai）自动执行
> - **数据源**：W23-W26 来自 [git-trending-rank.github.io](https://git-trending-rank.github.io/categories/weekly/) 真实周榜存档；W27 起为实时抓取 `github.com/trending?since=weekly`
> - **排名变化**：🆕 = 新入榜，↑N / ↓N = 升 / 降位次，— = 持平，⭐ = 当期冠军

---

### 📊 本期榜单 · 2026-W27（2026-06-29 ~ 2026-07-05）

| # | 变化 | 项目 | 类型 | 语言 | 用途 | 实现原理 | 周增⭐ | 总⭐ |
|:---:|:---:|------|------|:---:|------|----------|-----:|-----:|
| 1 | 🆕 | **msitarzewski/agency-agents** ⭐ | AI Agent 角色库 | Shell | 一整套 AI 代理机构的专业 Agent 模板 | Shell 脚本组织 Agent 提示词模板与工作流配置 | 10,483 | 127,017 |
| 2 | — | **DeusData/codebase-memory-mcp** | 代码智能 / MCP | C | 将代码库索引为持久知识图谱，158 语言毫秒查询 | C 高性能解析器构建 AST+符号引用知识图谱，MCP 暴露查询 | 10,186 | 26,140 |
| 3 | ↓2 | **calesthio/OpenMontage** | AI 视频制作 | Python | 开源智能体视频制作系统，12 流水线/52 工具 | 视频制作拆解为多阶段 Agent 流水线端到端自动化 | 9,213 | 33,080 |
| 4 | 🆕 | **usestrix/strix** | AI 安全测试 | Python | 开源 AI 渗透测试工具，自动发现并修复漏洞 | 大模型安全分析+传统渗透工具链，Agent 自主规划攻击路径 | 7,567 | 35,987 |
| 5 | 🆕 | **xbtlin/ai-berkshire** | AI 投资研究 | Python | 基于 Claude Code/Codex 的价值投资框架 | 四位大师方法论编码为 Agent 角色，多 Agent 对抗式分析 | 6,230 | 9,655 |
| 6 | ↑1 | **simplex-chat/simplex-chat** | 隐私通讯 | Haskell | 首个无任何用户标识符的消息网络 | 不分配用户 ID，双向临时队列建立连接，路由层不存储标识 | 5,971 | 17,844 |
| 7 | ↓1 | **JCodesMore/ai-website-cloner-template** | AI 网站克隆 | TypeScript | 一行命令用 AI Agent 克隆任意网站 | 抓取目标 DOM 与样式喂给 Agent 生成前端模板，迭代修补 | 4,205 | 25,542 |
| 8 | 🆕 | **browser-use/video-use** | AI 视频编辑 | Python | 用编程 Agent 编辑视频 | 视频编辑操作抽象为工具 API，Agent 编排调用序列 | 4,056 | 14,665 |
| 9 | 🆕 | **topoteretes/cognee** | AI 记忆平台 | Python | 开源 Agent 持久长期记忆，自托管知识图谱 | 文档经 LLM 抽取实体关系构建图谱，向量化语义检索 | 4,001 | 26,967 |
| 10 | ↓1 | **ZhuLinsen/daily_stock_analysis** | AI 股票分析 | Python | LLM 多市场股票分析，多源行情+新闻+看板+推送 | 定时拉取行情新闻→LLM 分析→写看板+推送，零成本运行 | 3,912 | 54,256 |
| 11 | ↓1 | **stablyai/orca** | Agent 并行调度 | TypeScript | 并行 Agent 舰队管理 ADE，桌面+移动端 | TypeScript 实现多 Agent 并行调度管理，跨桌面移动端 | 3,700 | 12,011 |
| 12 | 🆕 | **diegosouzapw/OmniRoute** | AI 网关 | TypeScript | 免费 AI 网关，231+ 供应商，连接主流编程 Agent | TypeScript 统一端点聚合 231+ AI 供应商，智能故障转移+token 压缩 | 3,631 | 11,292 |
| 13 | 🆕 | **ogulcancelik/herdr** | Agent 多路复用 | Rust | 终端 Agent 多路复用器 | Rust 实现终端多 Agent 并发调度 | 3,024 | 11,406 |
| 14 | 🆕 | **Robbyant/lingbot-map** | 3D 基础模型 | Python | 前馈 3D 基础模型，从流数据重建场景 | Python 实现前馈 3D 场景重建，处理流式数据输入 | 2,171 | 9,724 |
| 15 | ↑2 | **alibaba/page-agent** | 网页 GUI Agent | TypeScript | JavaScript 网页内 GUI Agent，自然语言控制界面 | TypeScript 注入网页的 GUI Agent，解析 DOM 执行自然语言指令 | 1,901 | 23,076 |
| 16 | ↓8 | **interviewstreet/hiring-agent** | AI 招聘 | Python | AI Agent 评估和评分简历 | Python 实现的简历评估 Agent，自动打分筛选 | 1,643 | 4,687 |
| 17 | 🆕 | **logto-io/logto** | 认证授权 | TypeScript | SaaS 和 AI 应用的认证授权基础设施 | TypeScript 实现 OIDC/OAuth 2.1 认证，多租户+SSO+RBAC | 1,368 | 13,721 |
| 18 | 🆕 | **openai/codex-plugin-cc** | Codex 插件 | JavaScript | 在 Claude Code 中使用 Codex 审查代码或委派任务 | JavaScript 桥接 Codex 到 Claude Code，跨 Agent 协作 | 1,296 | 24,341 |
| 19 | 🆕 | **allenai/olmocr** | PDF 处理 | Python | 为 LLM 数据集/训练线性化 PDF 的工具包 | Python 实现 PDF 文档线性化，适配 LLM 训练数据格式 | 1,216 | 18,696 |
| 20 | 🆕 | **Starmel/OpenSuperWhisper** | 语音听写 | Swift | macOS 听写应用 | Swift 实现 macOS 原生语音听写 | 494 | 1,707 |
### 🔍 W27 观察

- **Agent 基础设施持续霸榜**：codebase-memory-mcp（#2, 连续三周）、OpenMontage（#3, 连续三周）、cognee（#9, 连续两周）——Agent 底座项目已成"常客"。
- **视频 Agent 赛道成型**：OpenMontage（#3, 制作）+ video-use（#8, 编辑）三周内聚集成独立赛道。
- **AI 网关与多路复用新入榜**：OmniRoute（#12, 免费 AI 网关聚合 231+ 供应商）、herdr（#13, 终端 Agent 多路复用）、orca（#11, 并行 Agent 舰队）——Agent 调度层开始爆发。
- **中文 AI+金融连续两周**：daily_stock_analysis（W26 #9 → W27 #10）、ai-berkshire（#5 新入榜）。
- **隐私通讯逆势上升**：simplex-chat 从 W26 #7 升至 W27 #6。

---

### 📜 历史榜单 · 2026-W26（2026-06-22 ~ 2026-06-28）

| # | 变化 | 项目 | 类型 | 语言 | 用途 | 实现原理 | 周增⭐ | 总⭐ |
|:---:|:---:|------|------|:---:|------|----------|-----:|-----:|
| 1 | ↑8 | **calesthio/OpenMontage** ⭐ | AI 视频制作 | Python | 开源智能体视频制作系统，12 流水线/52 工具 | 视频制作拆解为多阶段 Agent 流水线端到端自动化 | 18,000 | 26,838 |
| 2 | ↓1 | **DeusData/codebase-memory-mcp** | 代码智能 / MCP | C | 将代码库索引为持久知识图谱，158 语言毫秒查询 | C 高性能解析器构建 AST+符号引用知识图谱，MCP 暴露查询 | 7,674 | 19,514 |
| 3 | 🆕 | **kunchenguid/no-mistakes** | Git 工具 | Go | git push no-mistakes 防误推送 | Go 实现的 Git pre-push 钩子，拦截误操作推送 | 2,229 | 4,046 |
| 4 | 🆕 | **palmier-io/palmier-pro** | AI 视频编辑 | Swift | macOS 平台 AI 视频编辑器 | Swift 实现 macOS 原生视频编辑，AI 辅助剪辑 | 6,126 | 9,297 |
| 5 | 🆕 | **google-labs-code/design.md** | AI 设计规范 | TypeScript | 向编码 Agent 描述视觉身份的格式规范 | 定义 DESIGN.md 格式让 Agent 持久理解设计系统 | 6,014 | 22,812 |
| 6 | 🆕 | **JCodesMore/ai-website-cloner-template** | AI 网站克隆 | TypeScript | 一行命令用 AI Agent 克隆任意网站 | 抓取目标 DOM 与样式喂给 Agent 生成前端模板，迭代修补 | 4,565 | 22,773 |
| 7 | 🆕 | **simplex-chat/simplex-chat** | 隐私通讯 | Haskell | 首个无任何用户标识符的消息网络 | 不分配用户 ID，双向临时队列建立连接，路由层不存储标识 | 1,973 | 14,927 |
| 8 | 🆕 | **interviewstreet/hiring-agent** | AI 招聘 | Python | AI Agent 评估和评分简历 | Python 实现的简历评估 Agent，自动打分筛选候选人 | 1,836 | 3,162 |
| 9 | 🆕 | **ZhuLinsen/daily_stock_analysis** | AI 股票分析 | Python | LLM 多市场股票分析，多源行情+新闻+决策看板 | 定时拉取行情新闻→LLM 分析→写看板+推送，零成本运行 | 7,137 | 51,085 |
| 10 | 🆕 | **stablyai/orca** | Agent 并行调度 | TypeScript | 并行 Agent 舰队管理 ADE，桌面+移动端 | TypeScript 实现多 Agent 并行调度管理，跨桌面移动端 | 2,554 | 8,590 |
| 11 | ↓8 | **Panniantong/Agent-Reach** | Agent 全网访问 | Python | 让 Agent 零 API 费用读取 17 个平台内容 | CLI 爬取各平台公开内容，无需付费 API | 7,676 | 44,402 |
| 12 | 🆕 | **mukul975/Anthropic-Cybersecurity-Skills** | Agent 安全技能 | Python | 817 个结构化网安技能，映射 6 大安全框架 | 按 MITRE ATT&CK 等框架组织安全技能，可插拔到 20+ 平台 | 5,121 | 22,624 |
| 13 | 🆕 | **penpot/penpot** | 设计工具 | Clojure | 开源设计工具，设计与代码协作 | Clojure 实现的开源设计工具，替代 Figma | 3,343 | 54,381 |
| 14 | 🆕 | **BuilderIO/agent-native** | Agent 应用框架 | TypeScript | 构建 Agent 原生应用的框架 | TypeScript 框架，为 Agent 原生应用设计的基础设施 | 1,474 | 2,873 |
| 15 | 🆕 | **jamiepine/voicebox** | AI 语音 | TypeScript | 开源 AI 语音工作室，克隆/听写/创作 | TypeScript 实现 TTS/语音克隆/听写的全栈语音工具 | 3,965 | 35,395 |
| 16 | 🆕 | **aws/agent-toolkit-for-aws** | AWS Agent 工具 | Python | AWS 官方 MCP 服务器/技能/插件 | Python 实现 AWS 官方 Agent 工具包，MCP 服务器+技能+插件 | 524 | 1,540 |
| 17 | 🆕 | **alibaba/page-agent** | 网页 GUI Agent | TypeScript | JavaScript 网页内 GUI Agent，自然语言控制界面 | TypeScript 注入网页的 GUI Agent，解析 DOM 执行自然语言指令 | 1,649 | 20,465 |
| 18 | 🆕 | **Stirling-Tools/Stirling-PDF** | PDF 工具 | Java | GitHub #1 PDF 应用，全设备编辑 PDF | Java 实现的 PDF 编辑工具，全平台支持 | 3,231 | 84,935 |
| 19 | 🆕 | **koala73/worldmonitor** | 全球情报看板 | TypeScript | 实时全球情报仪表板，AI 新闻聚合+地缘监测 | TypeScript 实现 AI 驱动的全球情报聚合与态势感知 | 2,735 | 60,684 |
| 20 | 🆕 | **NanmiCoder/MediaCrawler** | 社交媒体爬虫 | Python | 小红书/抖音/快手/B站/微博/贴吧/知乎爬虫 | Python 实现多平台社交媒体内容与评论爬虫 | 2,225 | 54,012 |
---

### 📜 历史榜单 · 2026-W25（2026-06-15 ~ 2026-06-21）

| # | 变化 | 项目 | 类型 | 语言 | 用途 | 实现原理 | 周增⭐ | 总⭐ |
|:---:|:---:|------|------|:---:|------|----------|-----:|-----:|
| 1 | 🆕 | **DeusData/codebase-memory-mcp** ⭐ | 代码智能 / MCP | C | 将代码库索引为持久知识图谱，158 语言毫秒查询 | C 高性能解析器构建 AST+符号引用知识图谱，MCP 暴露查询 | 5,419 | 10,204 |
| 2 | ↑2 | **chopratejas/headroom** | LLM Token 压缩 | Python | LLM 输入前智能压缩省 60-95% token | 日志/文件/RAG 片段压缩，库/代理/MCP Server 接入 | 14,982 | 44,187 |
| 3 | ↑4 | **Panniantong/Agent-Reach** | Agent 全网访问 | Python | 让 Agent 零 API 费用读取 17 个平台内容 | CLI 爬取各平台公开内容，无需付费 API | 8,483 | 36,799 |
| 4 | 🆕 | **iptv-org/iptv** | IPTV 资源 | TypeScript | 全球公开 IPTV 频道持续维护合集 | 社区维护的全球 IPTV 播放列表合集 | 7,856 | 127,101 |
| 5 | 🆕 | **n0-computer/iroh** | 网络协议 | Rust | 模块化 Rust 网络栈，用密钥而非 IP 地址拨号 | Rust 实现基于密钥的 P2P 网络栈，避免 IP 地址失效 | 1,621 | 10,441 |
| 6 | 🆕 | **google-research/timesfm** | 时序基础模型 | Python | Google Research 时序预测基础模型 | 预训练时序基础模型，支持时间序列预测任务 | 3,655 | 24,868 |
| 7 | ↓2 | **NVIDIA/SkillSpector** | Agent 安全扫描 | Python | NVIDIA 出品：AI Agent 技能安全扫描器 | 扫描 Agent 技能检测漏洞、恶意模式与安全风险 | 4,631 | 9,006 |
| 8 | 🆕 | **asgeirtj/system_prompts_leaks** | 提示词泄露 | JavaScript | 收录 Claude/ChatGPT/Gemini/Grok 等系统提示词 | 持续收集整理各 AI 产品系统提示词并公开 | 1,866 | 44,342 |
| 9 | 🆕 | **calesthio/OpenMontage** | AI 视频制作 | Python | 开源智能体视频制作系统，12 流水线/52 工具 | 视频制作拆解为多阶段 Agent 流水线端到端自动化 | 2,253 | 8,564 |
| 10 | 🆕 | **withastro/flue** | Agent 框架 | TypeScript | Astro 团队出品的沙箱 Agent 框架 | TypeScript 沙箱化 Agent 执行框架 | 1,012 | 6,287 |
| 11 | ↓5 | **addyosmani/agent-skills** | Agent 工程技能 | Shell | 面向 AI 编码 Agent 的生产级工程技能集合 | 沉淀工程实践为可安装技能库 | 6,332 | 64,725 |
| 12 | 🆕 | **Kong/insomnia** | API 客户端 | TypeScript | 开源跨平台 API 客户端，支持 GraphQL/REST/gRPC | TypeScript 实现，支持多种 API 协议的调试客户端 | 657 | 39,510 |
| 13 | 🆕 | **tursodatabase/turso** | 数据库 | Rust | 进程内 SQL 数据库，兼容 SQLite | Rust 实现的嵌入式 SQL 数据库，SQLite 兼容 | 968 | 20,766 |
| 14 | 🆕 | **makeplane/plane** | 项目管理 | TypeScript | 开源 Jira/Linear 替代品 | TypeScript 现代项目管理平台，任务/冲刺/文档 | 1,389 | 52,331 |
| 15 | 🆕 | **LMCache/LMCache** | LLM 推理加速 | Python | LLM 最快 KV Cache 层 | Python 实现高性能 KV Cache 加速 LLM 推理 | 713 | 9,537 |
| 16 | 🆕 | **meshery/meshery** | 云原生管理 | TypeScript | 云原生管理平台 | TypeScript 实现的云原生基础设施管理工具 | 898 | 11,222 |
| 17 | 🆕 | **chatwoot/chatwoot** | 客服系统 | Ruby | 开源全渠道客服平台 | Ruby 全栈实现，替代 Intercom/Zendesk | 2,233 | 33,105 |
| 18 | 🆕 | **swc-project/swc** | Web 编译 | Rust | Rust 实现的 Web 编译平台 | Rust 高性能 JS/TS 编译器，替代 Babel | 538 | 34,103 |
| 19 | 🆕 | **freeCodeCamp/freeCodeCamp** | 编程学习 | TypeScript | freeCodeCamp 开源课程平台 | TypeScript 全栈学习平台，免费编程课程 | 3,308 | 450,068 |
---

### 📜 历史榜单 · 2026-W24（2026-06-08 ~ 2026-06-14）

| # | 变化 | 项目 | 类型 | 语言 | 用途 | 实现原理 | 周增⭐ | 总⭐ |
|:---:|:---:|------|------|:---:|------|----------|-----:|-----:|
| 1 | ↑7 | **mvanhorn/last30days-skill** ⭐ | Agent 研究技能 | Python | 跨多平台一键研究任意话题并生成摘要 | Agent 技能跨 Reddit/X/YouTube/HN/Polymarket 聚合信息 | 12,602 | 41,962 |
| 2 | 🆕 | **apple/container** | Mac 容器化 | Swift | Apple 官方 Mac 容器化工具，轻量 VM 跑 Linux | Swift 实现，基于 macOS 虚拟化框架，专为 Apple Silicon 优化 | 9,173 | 36,944 |
| 3 | 🆕 | **phuryn/pm-skills** | PM Agent 技能 | 未指定 | 产品经理 Agent 技能市场，100+ 技能 | 策展式组织 PM 技能为可安装技能市场，覆盖发现到增长全流程 | 5,408 | 18,022 |
| 4 | ↓3 | **chopratejas/headroom** | LLM Token 压缩 | Python | LLM 输入前智能压缩省 60-95% token | 日志/文件/RAG 片段压缩，库/代理/MCP Server 接入 | 10,406 | 27,501 |
| 5 | 🆕 | **NVIDIA/SkillSpector** | Agent 安全扫描 | Python | NVIDIA 出品：AI Agent 技能安全扫描器 | 扫描 Agent 技能检测漏洞、恶意模式与安全风险 | 2,799 | 5,223 |
| 6 | 🆕 | **addyosmani/agent-skills** | Agent 工程技能 | Shell | 面向 AI 编码 Agent 的生产级工程技能集合 | 沉淀工程实践为可安装到 Claude Code/Cursor 的技能库 | 9,348 | 59,433 |
| 7 | ↑7 | **Panniantong/Agent-Reach** | Agent 全网访问 | Python | 让 Agent 零 API 费用读取 17 个平台内容 | CLI 爬取各平台公开内容，无需付费 API | 5,183 | 28,692 |
| 8 | 🆕 | **refactoringhq/tolaria** | 知识管理 | TypeScript | 管理 markdown 知识库的桌面应用 | 桌面端 markdown 知识库管理与组织工具 | 3,708 | 16,206 |
| 9 | ↑3 | **openai/plugins** | AI 插件规范 | JavaScript | OpenAI 官方插件仓库与开发规范 | 插件开发规范+示例代码+工具链 | 1,298 | 3,024 |
| 10 | ↓1 | **Leonxlnx/taste-skill** | Agent 审美技能 | Shell | 赋予 AI Agent 审美品味，拦截平庸生成内容 | 注入设计原则与审美规则提升输出质量 | 8,097 | 43,654 |
| 11 | ↓9 | **microsoft/markitdown** | 文档转 Markdown | Python | 将各类文件一键转 Markdown | Python 解析文档格式转 Markdown，LLM 预处理层标配 | 6,635 | 153,322 |
| 12 | 🆕 | **aaif-goose/goose** | AI Agent 框架 | Rust | 开源可扩展 AI Agent，超越代码建议 | Rust 实现的通用 Agent，支持安装/执行/编辑/测试 | 2,366 | 49,363 |
| 13 | 🆕 | **roboflow/supervision** | 计算机视觉 | Python | 可复用的计算机视觉工具库 | 提供检测/标注/跟踪等可复用 CV 工具 | 4,022 | 44,188 |
| 14 | 🆕 | **music-assistant/server** | 音乐管理 | Python | 开源媒体库管理器，连接流媒体服务和音箱 | Python 服务器端，连接多 streaming 服务与音箱设备 | 476 | 2,166 |
| 15 | 🆕 | **safishamsi/graphify** | 代码知识图谱 | Python | 将代码/SQL/文档/图像转为可查询知识图谱 | Agent 技能：多源素材构建统一知识图谱供查询 | 5,478 | 67,124 |
| 16 | 🆕 | **microsoft/PowerToys** | Windows 工具 | C | Microsoft PowerToys 效率工具集 | C 实现的 Windows 效率增强工具合集 | 826 | 134,872 |
| 17 | 🆕 | **mattermost/mattermost** | 团队协作 | TypeScript | 开源安全协作平台 | TypeScript 全栈开源协作平台，替代 Slack | 754 | 37,811 |
| 18 | ↓2 | **lfnovo/open-notebook** | 知识管理 | TypeScript | NotebookLM 开源平替 | AI 驱动摘要/问答/知识点提取，完全本地部署 | 3,570 | 30,504 |
| 19 | 🆕 | **opencv/opencv** | 计算机视觉 | C++ | 开源计算机视觉库 | C++ 实现，涵盖图像处理/视频分析/ML 等 CV 全栈 | 1,237 | 89,121 |
| 20 | 🆕 | **huggingface/OpenEnv** | RL 训练 | Python | HuggingFace 出品：RL 后训练环境接口库 | Python 接口库，为强化学习后训练提供环境抽象 | 235 | 2,210 |
---

### 📜 历史榜单 · 2026-W23（2026-06-01 ~ 2026-06-07）

| # | 变化 | 项目 | 类型 | 语言 | 用途 | 实现原理 | 周增⭐ | 总⭐ |
|:---:|:---:|------|------|:---:|------|----------|-----:|-----:|
| 1 | 🆕 | **chopratejas/headroom** ⭐ | LLM Token 压缩 | Python | LLM 输入前智能压缩省 60-95% token | 日志/文件/RAG 片段送入 LLM 前压缩，提供库/代理/MCP Server 三种接入 | 13,308 | 16,859 |
| 2 | 🆕 | **microsoft/markitdown** | 文档转 Markdown | Python | 将 PDF/Word/PPT/Excel/音视频一键转 Markdown | Python 解析各类文档格式转 Markdown，LLM 预处理层事实标配 | 15,015 | 147,287 |
| 3 | 🆕 | **harry0703/MoneyPrinterTurbo** | AI 短视频生成 | Python | 接入 LLM 一键生成高清短视频 | 文案→配音→字幕→素材→剪辑全流程自动化 | 9,174 | 81,141 |
| 4 | 🆕 | **supermemoryai/supermemory** | AI 记忆引擎 | TypeScript | 面向 AI 应用的极速可扩展 Memory API | Cloudflare Workers+PostgreSQL 分布式记忆引擎 | 2,992 | 26,005 |
| 5 | 🆕 | **affaan-m/ECC** | Agent 性能优化 | JavaScript | 为 Claude Code/Codex/Cursor 注入技能/本能/记忆/安全四维优化 | 四维体系扩展 Agent 工程能力，零配置兼容多框架 | 10,351 | 209,800 |
| 6 | 🆕 | **Open-LLM-VTuber/Open-LLM-VTuber** | AI 语音交互 | Python | 本地运行 Live2D 虚拟形象，语音与 LLM 实时对话 | 完全离线：LLM+语音识别+合成+Live2D 渲染全部本地化 | 2,273 | 10,340 |
| 7 | 🆕 | **revfactory/harness** | Agent 编排 | HTML | 元技能：设计领域特定 Agent 团队并生成技能配置 | 输入领域描述，输出完整 Agent 团队方案+技能分配 | 2,098 | 6,409 |
| 8 | 🆕 | **mvanhorn/last30days-skill** | Agent 研究技能 | Python | 跨 Reddit/X/YouTube/HN/Polymarket 研究任意话题 | Agent 技能跨多平台聚合信息生成有据可查的摘要 | 1,801 | 30,747 |
| 9 | 🆕 | **Leonxlnx/taste-skill** | Agent 审美技能 | Shell | 赋予 AI Agent 审美品味，拦截平庸生成内容 | 注入设计原则与审美规则，拦截 AI 通用平庸输出 | 6,085 | 36,515 |
| 10 | 🆕 | **EveryInc/compound-engineering-plugin** | Agent 工程插件 | TypeScript | Compound Engineering 官方插件，为多平台注入工程实践 | 将企业级工程实践封装为可复用 Agent 插件 | 1,752 | 20,356 |
| 11 | 🆕 | **can1357/oh-my-pi** | 终端 AI 编程 Agent | TypeScript | 终端 AI 编程 Agent，哈希锚定编辑+LSP+子代理 | Hash-anchored 编辑精确定位代码行，Rust+TS 双语言架构 | 2,318 | 11,081 |
| 12 | 🆕 | **openai/plugins** | AI 插件规范 | JavaScript | OpenAI 官方插件仓库与开发规范 | 插件开发规范+示例代码+工具链 | 360 | 2,009 |
| 13 | 🆕 | **aquasecurity/trivy** | 安全扫描 | Go | 检测容器/K8s/代码/云环境中的漏洞与配置错误 | Go 全栈扫描，SBOM 生成，CI/CD 集成 | 711 | 36,105 |
| 14 | 🆕 | **Panniantong/Agent-Reach** | Agent 全网访问 | Python | 让 Agent 零 API 费用读取 17 个平台内容 | CLI 爬取各平台公开内容，无需付费 API | 1,513 | 23,130 |
| 15 | 🆕 | **NousResearch/hermes-agent** | AI Agent 框架 | Python | 通用 Agent 框架，支持多模型后端与技能系统 | 持续学习积累技能的 Agent 平台，多模型后端切换 | 11,355 | 185,850 |
| 16 | 🆕 | **lfnovo/open-notebook** | 知识管理 | TypeScript | NotebookLM 开源平替，支持多源导入 | AI 驱动摘要/问答/知识点提取，完全本地部署 | 2,588 | 27,192 |
| 17 | 🆕 | **pbakaus/impeccable** | AI 设计语言 | JavaScript | 定义设计规则让 AI 生成界面具备专业审美 | 设计原则体系作为 Agent 技能安装，实时审美评估 | 3,562 | 35,527 |
| 18 | 🆕 | **nesquena/hermes-webui** | Agent Web UI | Python | 为 hermes-agent 提供网页端和移动端界面 | Python+FastAPI 后端，响应式 Web UI 管理 Agent | 4,418 | 13,827 |
| 19 | 🆕 | **dmtrKovalenko/fff** | 文件搜索 | Rust | 面向 AI Agent/Neovim/Rust 的极速文件搜索工具包 | Rust 实现高性能精确文件搜索，CLI+Neovim+NodeJS 绑定 | 983 | 7,666 |
---

## 📈 多周排名汇总（多周上榜项目）

| 项目 | 类型 | W23 | W24 | W25 | W26 | W27 | 趋势 |
|------|------|:---:|:---:|:---:|:---:|:---:|------|
| **Panniantong/Agent-Reach** | Agent 全网访问 | 14 | 7 | 3 | 11 | — | 4周上榜(-W23+-W24+-W25+-W26) |
| **chopratejas/headroom** | LLM Token 压缩 | ⭐1 | 4 | 2 | — | — | 3周上榜(-W23+-W24+-W25) |
| **DeusData/codebase-memory-mcp** | 代码智能 / MCP | — | — | ⭐1 | 2 | 2 | 3周上榜(-W25+-W26+-W27) |
| **calesthio/OpenMontage** | AI 视频制作 | — | — | 9 | ⭐1 | 3 | 3周上榜(-W25+-W26+-W27) |
| **microsoft/markitdown** | 文档转 Markdown | 2 | 11 | — | — | — | 2周上榜(-W23+-W24) |
| **mvanhorn/last30days-skill** | Agent 研究技能 | 8 | ⭐1 | — | — | — | 2周上榜(-W23+-W24) |
| **Leonxlnx/taste-skill** | Agent 审美技能 | 9 | 10 | — | — | — | 2周上榜(-W23+-W24) |
| **openai/plugins** | AI 插件规范 | 12 | 9 | — | — | — | 2周上榜(-W23+-W24) |
| **lfnovo/open-notebook** | 知识管理 | 16 | 18 | — | — | — | 2周上榜(-W23+-W24) |
| **NVIDIA/SkillSpector** | Agent 安全扫描 | — | 5 | 7 | — | — | 2周上榜(-W24+-W25) |
| **addyosmani/agent-skills** | Agent 工程技能 | — | 6 | 11 | — | — | 2周上榜(-W24+-W25) |
| **JCodesMore/ai-website-cloner-template** | AI 网站克隆 | — | — | — | 6 | 7 | 2周上榜(-W26+-W27) |
| **simplex-chat/simplex-chat** | 隐私通讯 | — | — | — | 7 | 6 | 2周上榜(-W26+-W27) |
| **interviewstreet/hiring-agent** | AI 招聘 | — | — | — | 8 | 16 | 2周上榜(-W26+-W27) |
| **ZhuLinsen/daily_stock_analysis** | AI 股票分析 | — | — | — | 9 | 10 | 2周上榜(-W26+-W27) |
| **stablyai/orca** | Agent 并行调度 | — | — | — | 10 | 11 | 2周上榜(-W26+-W27) |
| **alibaba/page-agent** | 网页 GUI Agent | — | — | — | 17 | 15 | 2周上榜(-W26+-W27) |
---

## 📈 跨周趋势观察（W23 — W27，5 周 Top 20 回顾）

### 赛道热度演变

| 大类 | W23 | W24 | W25 | W26 | W27 | 趋势判断 |
|------|:---:|:---:|:---:|:---:|:---:|----------|
| Agent 基础设施（MCP/记忆/代码智能） | 1 | 1 | 2 | 3 | 3 | **持续升温**，从应用层向基础设施深化 |
| Agent 技能（审美/工程/研究/安全/角色库） | 2 | 4 | 2 | 1 | 1 | **高位震荡**，可插拔技能成独立品类 |
| AI 视频（制作/编辑/生成） | 1 | 0 | 1 | 2 | 2 | **新赛道崛起**，W26-W27 集中爆发 |
| LLM 效率（Token 压缩/推理加速） | 1 | 1 | 1 | 1 | 0 | **W23-W26 刚需**，headroom 四周霸榜后离榜 |
| Agent 信息获取（全网访问/研究） | 0 | 1 | 1 | 1 | 0 | **稳定存在**，Agent-Reach 连续三周 |
| Agent 调度（并行/多路复用/网关） | 0 | 0 | 0 | 1 | 3 | **W27 新爆发**，orca/herdr/OmniRoute 聚集 |
| 安全（渗透/扫描/技能） | 1 | 1 | 1 | 1 | 1 | **每期 1-2 个**，安全持续受关注 |
| 投资/金融（股票/投研） | 0 | 0 | 0 | 1 | 2 | **新兴**，AI+金融连续两周上榜 |
| 隐私通讯 | 0 | 0 | 0 | 1 | 1 | **抬头**，simplex-chat 连续上升 |

### 五周关键洞察

1. **Agent 基础设施"三巨头"成型**：codebase-memory-mcp（代码智能，W25-W27 连续三周 #4→#3→#2 持续攀升）、cognee（记忆平台，W26-W27 连续两周）、OpenMontage（视频制作，W25-W27 连续三周 #8→#1→#3）。MCP 协议是共同接口层。

2. **Token 压缩是 W23-W26 的绝对主线**：headroom 四周上榜（#1→#4→#1→离榜），周增长 1-1.5 万星稳定。W27 离榜说明 Token 压缩已从"新痛点"变为"已解决基础设施"，市场教育完成。

3. **Agent 技能生态成型独立赛道**：taste-skill、agent-skills、last30days-skill、Anthropic-Cybersecurity-Skills、agency-agents——"-skill"后缀项目五周内出现 10+ 次。Claude Code/Cursor 可插拔技能体系催生独立品类。

4. **大厂官方项目密集入场**：microsoft/markitdown（W23-W24）、apple/container（W24 #2）、NVIDIA/SkillSpector（W24-W25）、google-research/timesfm（W25）、google-labs-code/design.md（W26）、aws/agent-toolkit-for-aws（W26）、alibaba/page-agent（W26-W27）、openai/codex-plugin-cc（W27）。大厂瞄准 Agent 基础设施位。

5. **AI+金融连续两周上榜且与你的身份强相关**：daily_stock_analysis（W26 #9 → W27 #10）、ai-berkshire（W27 #5）。AI 驱动投研/量化工具正形成 recurring 赛道。

6. **视频 Agent 是 W26-W27 新爆发点**：OpenMontage（制作）、video-use（编辑）、palmier-pro（macOS 编辑）。从"AI 生成短视频"升级到"Agent 制作/编辑视频"。

7. **Agent 调度层 W27 首次聚集**：orca（#11, 并行舰队）、herdr（#13, 终端多路复用）、OmniRoute（#12, 免费 AI 网关）——当 Agent 数量增多后，调度/路由/网关成为新需求。

---

## 🗂️ 历史归档

每期原始数据以 JSON 格式归档至 `/workspace/github-weekly-archive/` 目录。

| 周期 | 时间范围 | 数据源 | 项目数 | 冠军项目 | 周增⭐ | 归档文件 |
|------|----------|--------|:---:|----------|-----:|----------|
| 2026-W23 | 06.01 — 06.07 | git-trending-rank 存档 | 19 | chopratejas/headroom | 13,308 | `2026-W23.json` ✅ |
| 2026-W24 | 06.08 — 06.14 | git-trending-rank 存档 | 20 | mvanhorn/last30days-skill | 12,602 | `2026-W24.json` ✅ |
| 2026-W25 | 06.15 — 06.21 | git-trending-rank 存档 | 19 | chopratejas/headroom | 14,982 | `2026-W25.json` ✅ |
| 2026-W26 | 06.22 — 06.28 | git-trending-rank 存档 | 20 | calesthio/OpenMontage | 18,000 | `2026-W26.json` ✅ |
| 2026-W27 | 06.29 — 07.05 | GitHub Trending 实时 | 20 | msitarzewski/agency-agents | 10,483 | `2026-W27.json` ✅ |

---

## ⚙️ 自动化机制

- **定时任务**：每周一 09:00（Asia/Shanghai）触发
- **执行流程**：抓取 GitHub Trending → 提取 Top 20 → 分析类型/用途/原理 → 计算排名变化 → 更新报告+保存 JSON 归档
- **数据源**：`github.com/trending?since=weekly`（W27 起）+ [git-trending-rank.github.io](https://git-trending-rank.github.io/categories/weekly/)（W23-W26 历史回溯）
