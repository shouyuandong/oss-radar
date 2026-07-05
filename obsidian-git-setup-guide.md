# Obsidian Git 插件配置指引

> 将 oss-radar 仓库接入 Obsidian，实现每周报告自动同步到知识库。

---

## 前置准备

| 项目 | 说明 |
|------|------|
| Obsidian | 已安装（Mac 端） |
| oss-radar 仓库 | https://github.com/shouyuandong/oss-radar |
| Git | Mac 已安装（终端输入 `git --version` 能返回版本号即可） |
| GitHub 认证 | SSH key 或 HTTPS token（下面会配） |

---

## 步骤 1：克隆仓库到 Obsidian vault

### 方式 A：作为 vault 子目录（推荐）

如果你的 vault 已经有内容，想把 oss-radar 作为其中一部分：

```bash
# 进入你的 Obsidian vault 目录
cd ~/path/to/your-vault

# 创建技术雷达目录（如果没有）
mkdir -p 知识库/技术雷达

# 克隆 oss-radar 到该目录下
git clone https://github.com/shouyuandong/oss-radar.git 知识库/技术雷达/开源雷达
```

这样 vault 里的路径是：

```
your-vault/
├── 知识库/
│   └── 技术雷达/
│       └── 开源雷达/          ← oss-radar 仓库
│           ├── README.md
│           ├── all_weeks.csv
│           ├── reports/
│           │   └── 2026-W27.md  ← 每周自动更新
│           └── ...
├── 日记/
├── 投资研究/
└── ...
```

### 方式 B：整个 vault 就是 oss-radar（不推荐）

只有当你想专门建一个"GitHub 趋势观察"的独立 vault 时才用这个方式。

---

## 步骤 2：安装 Obsidian Git 插件

1. 打开 Obsidian → **设置** → **第三方插件**
2. 关闭"安全模式"（如果还开着）
3. 点 **浏览** → 搜索 **"Obsidian Git"**
4. 找到作者为 **Vinzent03** 的那个 → **安装** → **启用**

> 如果社区插件市场打不开（网络问题），可手动下载：
> 1. 去 https://github.com/Vinzent03/obsidian-git/releases 下载最新 `main.js`、`manifest.json`、`styles.css`
> 2. 放到 `<vault>/.obsidian/plugins/obsidian-git/` 目录
> 3. 重启 Obsidian → 设置 → 第三方插件 → 启用

---

## 步骤 3：配置 GitHub 认证

### 推荐：用 Personal Access Token（HTTPS）

```bash
# 在 oss-radar 目录里配置 credential helper
cd ~/path/to/your-vault/知识库/技术雷达/开源雷达
git config credential.helper osxkeychain

# 手动触发一次 pull，输入用户名和 token（会存到 keychain，以后免输）
git pull
# Username: shouyuandong
# Password: <粘贴你的 GitHub token，不是密码>
```

配置完成后，Obsidian Git 插件会自动使用 keychain 中的凭证，无需在插件里填 token。

### 备选：用 SSH key

如果你已经配过 GitHub SSH key：

```bash
cd ~/path/to/your-vault/知识库/技术雷达/开源雷达
git remote set-url origin git@github.com:shouyuandong/oss-radar.git
```

---

## 步骤 4：配置 Obsidian Git 插件

打开 Obsidian → **设置** → **Obsidian Git**，按下表配置：

### 核心配置

| 配置项 | 推荐值 | 说明 |
|--------|--------|------|
| **Auto pull interval** | `30` (分钟) | 每 30 分钟自动 pull，sandbox 周一 9 点 push 后半小时内同步 |
| **Auto commit+push interval** | `0` (禁用) | 设为 0 禁用自动提交。oss-radar 是只读仓库，你不需要往里 push |
| **Commit message** | `vault: auto sync {{date}}` | 如果开启自动提交时的消息模板 |
| **Pull on startup** | ✅ 开启 | 每次 Obsidian 启动时先 pull 一次 |
| **Push after commit** | ❌ 关闭 | oss-radar 对你是只读的，不需要 push |

### 通知与提醒

| 配置项 | 推荐值 | 说明 |
|--------|--------|------|
| **Show status bar** | ✅ 开启 | 底部状态栏显示 `↓1` 待 pull / `↑2` 待 push |
| **Desktop notifications** | ✅ 开启 | pull 到新内容时弹系统通知 |
| **Notify on auto-pull** | ✅ 开启 | 自动 pull 后有变化时提醒 |

### 高级（按需）

| 配置项 | 推荐值 | 说明 |
|--------|--------|------|
| **Submodule support** | ✅ 开启 | 如果 oss-radar 是作为 submodule 接入的 |
| **Ignore path patterns** | `.obsidian/` | 避免 vault 配置文件干扰 |

---

## 步骤 5：验证

1. **手动 pull 测试**：`Ctrl/Cmd + P` → 输入 `Obsidian Git: Pull` → 执行
2. 检查状态栏是否显示 `✓` 或同步状态
3. 在文件树里确认 `知识库/技术雷达/开源雷达/reports/2026-W27.md` 能正常打开

---

## 日常使用

### 每周一期报告的体验流程

```
周一 09:00  sandbox 自动抓取 → push 到 GitHub
周一 ~09:30 Obsidian Git 自动 pull → 报告出现在 vault
            状态栏显示 ↓1 + 系统通知"有新内容"
你打开 Obsidian → 阅读 reports/2026-W28.md
            → 用 [[双链]] 关联感兴趣的项目到你自己的笔记
```

### 常用快捷操作

| 操作 | 命令面板输入 | 建议快捷键 |
|------|-------------|-----------|
| 手动同步（pull） | `Obsidian Git: Pull` | `Cmd+Shift+P` 后搜 pull |
| 查看变更 | `Obsidian Git: Open source control view` | 可固定到侧边栏 |
| 查看文件历史 | `Obsidian Git: Open file history` | 右键文件 → Open history |

### 在 Obsidian 里利用 oss-radar 数据

**双链关联**：在你的项目笔记里引用报告

```markdown
# DeusData/codebase-memory-mcp 调研

看到 [[2026-W27]] 里排名第2，连续三周上榜。
与我的 codegraph MCP 是同赛道。

## 核心能力
- 代码库索引为知识图谱
- 158 语言支持
- MCP 协议

## 与我的关联
- [[codegraph MCP 笔记]]
- [[Bug 蒸馏系统 PRD]] 的 RAG 架构可参考
```

**Dataview 查询**（如果装了 Dataview 插件）：

```dataview
TABLE week, rank, category
FROM "知识库/技术雷达/开源雷达/reports"
WHERE contains(file.content, "codebase-memory-mcp")
SORT week DESC
```

---

## 常见问题

### Q: pull 时提示认证失败？

```bash
# 重新配置 token
cd ~/path/to/开源雷达
git config credential.helper osxkeychain
# 删除 keychain 中的旧凭证：钥匙串访问.app → 搜索 github.com → 删除
# 重新 pull，输入新 token
```

### Q: 网络慢 / pull 超时？

方案一：watt 加速 GitHub（你已有）
方案二：换 SSH 协议（有时比 HTTPS 稳定）
方案三：配置 git 代理

```bash
git config --global http.proxy http://127.0.0.1:watt端口
git config --global https.proxy http://127.0.0.1:watt端口
```

### Q: vault 里其他目录被 git 追踪了？

如果 oss-radar 是 vault 的子目录，Obsidian Git 插件默认只管 vault 根目录的 git 仓库。子目录里的 git 仓库需要：

- **方案一**：用 `git subtree` 而非 `git clone`（把 oss-radar 内容并入 vault 仓库）
- **方案二**：在 oss-radar 子目录里用终端手动 `git pull`，Obsidian Git 插件只管 vault 主仓库

> 推荐 **方案二**：vault 主仓库管你的个人笔记，oss-radar 子目录单独用终端 pull。虽然多一步手动，但隔离干净，不会互相干扰。

### Q: 想在 iPhone 上也同步？

- iOS Obsidian + GitKeep 或 Working Copy 插件
- 或用 Obsidian Sync（$8/月，官方同步，不走 git）
- oss-radar 仓库本身可以在手机浏览器直接看 https://github.com/shouyuandong/oss-radar

---

## 配置检查清单

完成以下所有项即表示接入成功：

- [ ] oss-radar 已 clone 到 vault 的 `知识库/技术雷达/开源雷达/`
- [ ] Obsidian Git 插件已安装并启用
- [ ] GitHub token 已存入 keychain（手动 pull 一次验证）
- [ ] Auto pull interval 设为 30 分钟
- [ ] Pull on startup 已开启
- [ ] Desktop notifications 已开启
- [ ] 手动执行一次 Pull，状态栏显示正常
- [ ] 能在 Obsidian 中打开 `reports/2026-W27.md`
