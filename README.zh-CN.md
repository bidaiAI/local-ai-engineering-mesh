# Local AI Engineering Mesh

[中文](README.zh-CN.md) | [English](README.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md)

把你的 AI 工具，从彼此割裂的助手，升级成一套有治理、有记忆、有证据闭环的工程系统。

这不是一个 prompt 包，也不是 skill 收藏夹。它更像一套“仓库形态的 operating model”，目标是把本地 AI 工具从“会回答”升级成“会按制度做工程”。

这里的核心思想是：Codex 不是单独运行的。Codex、Cursor、Antigravity、Claude Code、OpenCode 可以在同一份 `AGENTS.md` 之下，作为一套跨平台 AI 编码系统中的不同端点协同工作。

## 这个仓库解决什么问题

大多数人其实并没有真正的 AI 系统。
他们只是不断在多个工具之间切换：
- 一个拿来写代码
- 一个拿来查资料
- 一个拿来做浏览器操作
- 还有一个作为兜底工具

结果往往是：
- 工具频繁切换
- 指令重复维护
- 记忆断裂
- 输出风格和质量门槛不一致
- 过度依赖某一个当下感觉最顺手的产品

这个仓库存在的目的，就是把这些本地 AI 工具组织成一套系统，而不是一堆孤岛。

## 它升级的是什么

- `shared law`：用 `AGENTS.md` 统一顶层规则
- `memory`：持久化规则、路由和项目状态
- `bootstrap`：给项目初始化命令、记忆和风险边界
- `orchestration`：把规划、设计、验证、发布变成明确角色
- `planning`：先研究，再形成结构化执行计划
- `evidence`：完成必须有证据，不靠口头叙述
- `release safety`：预览优先、发布前门禁
- `evolution`：重复成功的方法可以升级成可复用能力

## 当前真实落地程度

这个仓库背后对应的是一套已经运行中的本地环境。写这份 README 时，真实状态包括：
- `~/.codex/skills` 中有 `30` 个 Codex skills
- `~/.codex/memories` 中有 `3` 个全局记忆文件
- 项目 `.codex/commands` 中有 `10` 个治理命令
- 项目 `.codex/memory` 中有 `5` 个项目记忆文件
- 项目 `.codex/state` 中已经存在状态文件

这意味着它不是概念稿，而是已经落到：
- 规则层
- 技能层
- 项目运行层
- 状态层
- 证据层

## 这台机器上的四工具综合评估

下面这些评分不是通用跑分，而是基于这台机器在 **2026 年 3 月 25 日** 的真实配置，对其架构成熟度做出的判断。

### Codex — 92/100
**定位：** 主工程执行中枢 + 主治理中枢。

**优势**
- 当前体系里最强的本地执行中心
- skills、commands、发布纪律、证据闭环最完整
- 最适合把计划推进成受治理的实际交付

**短板**
- 某些默认产品体验和自动化顺滑感，仍然不如 Claude 自然

### Claude — 90/100
**定位：** 工作流方法论引擎 + 参考栈。

**优势**
- 命令化和工作流感最强
- 模块化思维、审查习惯、协作体验成熟
- 依旧是 AI coding workflow 的重要标杆

**短板**
- 在这套本地系统里，它没有像 Codex 那样深度接入执行治理层

### Cursor — 89/100
**定位：** IDE 主战场 + 编辑器原生实现层。

**优势**
- 离实际编码表面最近
- 编辑器内项目规则密度高
- 非常适合降低日常开发摩擦

**短板**
- 系统治理感和“操作系统层”能力弱于 Codex / Antigravity

### Antigravity — 91/100
**定位：** 广谱能力扩展平台。

**优势**
- 浏览器、artifact、knowledge、扩展技能覆盖面广
- 更像一个 AI 平台，而不只是单工具
- 很适合做能力外延和跨域工作

**短板**
- 太宽容易带来噪音
- 做工程主线时不一定比 Codex 更稳

### 本机综合系统 — 91/100
这台机器最强的地方，不是某一个 AI 天下第一，而是它们已经被组织成了一套系统：
- 有共享法则
- 有多端分工
- 有项目级记忆
- 有执行门禁
- 有跨平台一致性

最准确的定义是：

**Shared Law + Multi-Tool Specialized AI System**

这已经不是“四选一”的配置，而是一套本地 AI 工程 Mesh。

## 跨平台结构

在这套真实环境里：
- `~/.codex/config.toml` 通过 `model_instructions_file` 加载 `~/AGENTS.md`
- `~/.codex/instructions.md` 负责 Codex 专属路由、profiles 和 skills 指南
- 多个编码工具共享同一份顶层 operating law

这意味着它同时具备：
- 执行层的工具原生能力
- 策略层的跨平台一致性

也意味着：你不需要每次切工具就把整个 workflow 从零重来。

参见 [CROSS-PLATFORM.md](docs/CROSS-PLATFORM.md)。

## 与最新 Claude 的关系

截至 **2026 年 3 月 23 日**，Anthropic 公开的最新 Claude coding 栈主要是：
- `Claude Opus 4.6`：发布于 **2026 年 2 月 5 日**
- `Claude Sonnet 4.6`：发布于 **2026 年 2 月 17 日**

这个仓库并不声称“本地工具天然就超过 Claude 的模型能力”。

它提出的是一个更窄、但更实用的判断：

只要把本地 AI 工具的 operating layer 做强，它们在长流程工程执行上就会明显更能打，因为 workflow 不再依赖一个完美 prompt，也不再依赖某一个产品永远在线。

参见 [COMPARE-WITH-CLAUDE.md](docs/COMPARE-WITH-CLAUDE.md)。

## 仓库结构

```text
local-ai-engineering-mesh/
├── README.md
├── README.zh-CN.md
├── README.ru.md
├── README.ja.md
├── README.fr.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── COMPARE-WITH-CLAUDE.md
│   ├── CROSS-PLATFORM.md
│   ├── EXECUTION-LOOP.md
│   ├── REPO-MAP.md
│   ├── STACK.md
│   └── FRAMEWORK-DIAGRAM.md
└── templates/
    ├── antigravity/
    ├── cursor/
    ├── global-memory/
    ├── project-memory/
    └── policy.env.example
```

参见 [REPO-MAP.md](docs/REPO-MAP.md)。

## 仓库里有什么模板

这个仓库包含：
- 全局记忆模板
- 项目记忆模板
- Cursor 规则模板
- Antigravity workflow / knowledge 模板
- policy 默认值模板

采用方式可以分三种：
- 先升级单个工具
- 双工具协作
- 全量 Mesh：Codex + Cursor + Antigravity + Claude 共用一套法则

## 参考来源

- [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/)
- [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)
- [Introducing Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [Compound Engineering plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [shinpr/agentic-code](https://github.com/shinpr/agentic-code)
- [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)
