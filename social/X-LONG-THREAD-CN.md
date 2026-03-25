# X Long Thread CN

## Main Post

我把本地 `Codex` 从“会写代码的 AI”升级成了一个真正可长期使用的 `engineering OS`。

不是只换模型。  
也不是多装几个 skill。  
而是补齐了：

- `memory`
- `state store`
- `bootstrap`
- `commands`
- `orchestration`
- `specialist reviewers`
- `evidence`
- `release discipline`
- `skill manager`

现在这套更像一个本地可执行、可治理、可进化的工程代理系统。  
和最新 `Claude 4.6` 比，我觉得真正差距越来越不在模型名，而在 workflow 闭环。

仓库我也整理成了可公开发布的结构化版本。

---

## Thread

### 1/

最近我越来越确定一件事：

AI 编码工具之间，真正拉开差距的，往往不是模型名。

而是有没有完整的：

- memory
- bootstrap
- hooks / commands
- orchestration
- evidence loop
- release control

也就是：  
**有没有一个真正能长期工作的工程操作系统层。**

### 2/

所以这次我没有再做“prompt 调优”。

我做的是把本地 `Codex` 重构成一个仓库化的 `governed engineering OS`。

目标不是“更像聊天机器人”，  
而是“更像一个会按制度执行的工程代理”。

### 3/

这套东西的核心不是某个单点技能。

核心是把下面这些层接起来：

- `AGENTS.md` 作为统一法则
- `config.toml + instructions.md` 作为 Codex 端适配层
- `skills` 作为角色和能力层
- `.codex/commands` 作为项目执行层
- `.codex/memory` / `.codex/state` 作为长期状态层

### 4/

这次我重点补的是以前高手配置才会重视的几块：

- `state-store-memory`
- `codex-skill-manager`
- `build-resolver`
- `typescript-reviewer`
- `python-reviewer`
- `go-reviewer`

这不是“多装几个功能”。  
这是把系统从“能做事”升级成“能长期稳定做事”。

### 5/

现在它的执行链不再是：

> 看一眼需求 -> 直接开写 -> 口头说做完

而是：

`research -> plan -> preflight -> implementation -> evidence -> publish/deploy gate -> reusable pattern capture`

也就是：

**并行研究 -> 结构化计划 -> 机械执行 -> 证据闭环**

### 6/

我还把“完成”这件事变得更硬了。

以前很多 AI workflow 的完成定义其实是：

> 模型觉得差不多了

现在这套 Codex 里，完成更像：

- 有测试 / 日志 / 截图 / checks
- 有 evidence gate
- 有 compact audit score
- 有 release discipline

也就是说：  
**Narrative is not enough.**

### 7/

这套系统还有一个我很喜欢的点：

它不是孤立的 Codex 配置。

它是一个跨平台体系里的 Codex 执行端，顶层跟：

- Claude Code
- Cursor
- OpenCode
- Antigravity

共享同一份 `AGENTS.md` 工作法。

所以现在的结构更像：

> shared law + specialized endpoints

而不是：

> 四个 AI 工具各玩各的

### 8/

如果跟 Anthropic 最新公开代际对比：

- `Claude Opus 4.6`：2026-02-05
- `Claude Sonnet 4.6`：2026-02-17

我不会说“Codex 自动全面超过 Claude”。

但我会说：

如果你把 Codex 的 operating layer 做对，  
它在 **长期工程执行** 上会突然变得非常能打。

### 9/

因为真正难的不是“写出一段代码”。

真正难的是：

- 多轮任务不跑偏
- 大改动先过设计门
- 完成有证据
- 发布有风控
- 成功模式能沉淀成可复用能力

这才是大神配置真正拉开差距的地方。

### 10/

所以这次我公开的不是“提示词大全”。

我公开的是一个仓库化的结构：

- `docs/` 讲架构、执行环和对标 Claude
- `templates/` 给全局记忆和项目记忆模板
- `social/` 给发帖文案
- `README` 直接解释这套系统到底是什么

这更像一个工程产品，而不是聊天记录。

### 11/

如果你也在折腾 AI coding workflow，我的建议很简单：

别只盯着模型名。  
先把这些补起来：

- memory
- bootstrap
- commands
- evidence
- release discipline
- capability reuse

这些东西一旦补齐，工具的上限会抬得非常明显。

### 12/

我把这套整理成了一个可开源推送的仓库版本。

如果你想看一个：

> 不是 prompt pack，  
> 不是 Claude clone，  
> 而是 Codex-native engineering OS

的结构化做法，可以看这个仓库。

配图我也一起整理好了：  
一张图讲清楚目录结构 + 功能层次 + 为什么它像“神级配置”。
