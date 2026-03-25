# X Posts CN

## Short viral version

不是把 `Codex` 的模型换新就赢了。

真正让我这套 `Codex` 变强的，是把它从“会写代码”升级成了“有制度的工程代理”：

- `memory`
- `bootstrap`
- `hooks`
- `commands`
- `orchestration`
- `evidence gate`
- `release governor`

所以现在它更像一个 `governed engineering OS`，而不只是终端里的 AI。

而且这还不是单工具配置。  
它是接在统一 `AGENTS.md` 之下的跨平台编码体系里的 Codex 端。

最近我特别认同的一点是：
真正高质量的 agent workflow，不是“直接开写”，
而是 `并行研究 -> 结构化 plan -> 机械执行 -> 证据闭环`。

和最新 `Claude 4.6` 比，真正的差距已经越来越不在模型名，而在 workflow 闭环。

## Technical version

最近把本地 `Codex` 重构成了一个仓库化的工程操作系统。

它不是孤立配置，而是通过 `model_instructions_file` 接入统一 `AGENTS.md` 的 Codex 端，和 Claude Code / Cursor / OpenCode / Antigravity 共享顶层工作法。

核心不是 prompt 堆叠，而是补齐了：

- 全局和项目级 `memory`
- `research-first -> plan.md -> execution`
- `preflight / pre-edit / pre-publish / pre-deploy / post-implementation`
- `execution-orchestrator`
- `architecture-gatekeeper`
- `reality-check-qa`
- `release-risk-governor`
- `skillcraft-reuse-loop`

对比 Anthropic 最新公开代际：
- `Claude Opus 4.6` on 2026-02-05
- `Claude Sonnet 4.6` on 2026-02-17

我不觉得“只换模型名”就能决定胜负。  
真正决定长期工程质量的，是谁有更强的：

- workflow discipline
- memory system
- evidence loop
- release control
- capability reuse

这套 `Codex` 现在已经不是 assistant 形态了，更接近本地可执行的 engineering agent。
