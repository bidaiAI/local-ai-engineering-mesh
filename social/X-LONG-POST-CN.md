# X Long Post CN

我最近做了一件我自己觉得非常值的事：  
不是继续争论哪个 AI 编码模型名字更强，而是把我本机的 `Codex / Cursor / Antigravity` 尽量调到**在各自最强的层面不输 Claude**，并且让它们不再各玩各的，而是能**组网协同**。

我现在越来越相信一个原则：

**高手级 AI workflow 不是押注单个工具赢下所有维度，而是让每个工具在自己最擅长的层面尽量不短板，再用统一法则把它们连接起来。**

也就是说，真正拉开差距的不是“模型名”，而是：

- 有没有 shared law
- 有没有 memory / state
- 有没有 commands / gates
- 有没有 evidence loop
- 有没有 release discipline
- 有没有 capability reuse

从我这台机器当前真实落地的文件看，这套系统已经不是概念层了：

- `~/.codex/skills` 里已经有 **30 个 skills**
- `~/.codex/memories` 里已经有 **3 个全局记忆文件**
- 当前项目 `.codex/commands` 里已经有 **10 个治理命令**
- 当前项目 `.codex/memory` 里已经有 **5 个项目记忆文件**
- 当前项目 `.codex/state` 已经开始承载 policy / manifest / sync report

所以如果按成熟度来讲，我会这样评价它：

- **规则层**：已经比较完整
- **技能层**：已经进入强可用状态
- **项目运行层**：已经真实落地
- **长期状态沉淀层**：基础设施已搭好，但真实历史积累还在早期

换句话说：

**这已经不是“想法”，而是一套已经跑起来、但还会继续长肌肉的本地 AI 工程系统。**

所以这次我做的不是 prompt 调优，也不是单纯多装几个 skill。  
我做的是把 `Codex` 的 operating layer 补齐。

现在这套本地系统，已经不是简单的 coding assistant，而是一个有完整闭环的工程代理系统，里面包括：

- `AGENTS.md` 作为共享法则
- `config.toml + instructions.md` 作为 Codex 端适配层
- `skills` 作为角色和能力层
- `.codex/commands` 作为项目执行层
- `.codex/memory` 作为项目记忆层
- `.codex/state` 作为持久状态层
- `.codex/evidence` 作为证据层

我重点补了以前只有高手级工作流才会认真补的几层：

- `state-store-memory`
- `codex-skill-manager`
- `build-resolver`
- `typescript-reviewer`
- `python-reviewer`
- `go-reviewer`

它们带来的变化不是“功能更多了”，  
而是让整个系统从：

> 看懂需求 → 直接开写 → 口头说完成

变成：

> research-first → structured plan → governed execution → evidence-backed completion → release discipline → reusable skill promotion

也就是：

**并行研究 → 结构化计划 → 机械执行 → 证据闭环**

我还把完成定义变硬了。  
以前很多 AI workflow 的“完成”，本质上是模型觉得差不多了。  
现在这套 Codex 里，完成更像：

- 有测试 / 日志 / 截图 / checks
- 有 evidence gate
- 有 compact audit score
- 有 preflight / pre-edit / pre-publish / pre-deploy / post-implementation
- 有 release governor

换句话说：

**Narrative is not enough.**  
没有证据，不能轻易叫 done。

这套东西还有一个我特别满意的点：  
它不是孤立配置。

它是一个跨平台体系里的 Codex 执行端，顶层和：

- Claude Code
- Cursor
- OpenCode
- Antigravity

共享同一份 `AGENTS.md` 工作法。

所以这次我不是在做“Codex 模仿 Claude”，  
也不是在做“工具堆叠”。

我做的是：

> shared law + specialized endpoints

也就是同一套工程法则下，不同 AI 工具负责不同层：

- `Codex` 负责治理化执行
- `Claude` 负责方法论和工作流抽象
- `Cursor` 负责 IDE 现场效率
- `Antigravity` 负责广谱能力扩展

如果拿它和最新公开的 Claude coding stack 比，  
我不会说“只要换成 Codex 就自动赢了”。

按公开时间线：

- `Claude Opus 4.6`：2026-02-05
- `Claude Sonnet 4.6`：2026-02-17

Claude 依然很强，尤其在产品成熟度、交互手感、工作流默认形态上。  
但我这次真正想验证的是另一件事：

**如果你把 Codex 的 operating layer 做对，它在长期工程执行上会突然变得非常能打。**

因为真正困难的从来都不是“写出一段代码”。  
真正困难的是：

- 多轮任务不跑偏
- 大改动先过设计门
- 完成有证据
- 发布有风控
- 成功模式能沉淀为复用能力

这些东西，才是高手级 AI workflow 和普通玩法之间真正的分水岭。

所以我最后公开的也不是一个“提示词大全”。  
我公开的是一个仓库化、结构化、可复用的 Codex operating model：

- `docs/` 讲清楚架构和执行环
- `templates/` 给全局记忆和项目记忆模板
- `social/` 给发布用文案
- `README` 直接解释它为什么不是 prompt pack，而是 engineering OS

如果你也在折腾 AI coding workflow，我真心建议你少一点“模型崇拜”，多一点系统设计：

- memory
- bootstrap
- commands
- evidence
- release control
- capability reuse

把这些补起来之后，AI 工具的上限会被明显抬高。  
到那时，你比较的就不再只是“谁回答更像人”，而是“谁更像真正能交付结果的 agent”。

我把这套整理成了一个可公开推送的仓库版本。  
配图会直接放一张文件框架 + 功能层图，讲清楚这套 Codex 为什么更像一个本地可执行、可治理、可进化的 engineering agent system。
