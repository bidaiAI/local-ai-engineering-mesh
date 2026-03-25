# Cross-Platform

[中文摘要](#中文摘要) | [English Summary](#english-summary) | [Русское резюме](#русское-резюме) | [日本語要約](#日本語要約) | [Résumé français](#résumé-français)

## English Summary
This repository describes one shared operating law across multiple AI coding tools. Codex is the strongest execution hub, Cursor is the IDE-native implementation layer, Antigravity is the broad capability platform, and Claude remains a strong workflow benchmark. The value is not one perfect tool, but a system that survives tool switching and keeps one quality bar.

## 中文摘要
这个仓库描述的是一套跨工具共享的 operating law。Codex 是主执行中枢，Cursor 是 IDE 原生实现层，Antigravity 是广谱能力平台，Claude 仍然是重要的工作流标杆。关键价值不在于某一个工具绝对最强，而在于整套系统在切换工具时仍然保持同一质量门槛。

## Русское резюме
Этот репозиторий описывает единую operating law для нескольких AI-инструментов разработки. Codex выступает главным центром исполнения, Cursor — IDE-native слоем реализации, Antigravity — платформой широких возможностей, а Claude остаётся сильным эталоном workflow. Ценность не в одном идеальном инструменте, а в системе, которая сохраняет единый стандарт качества при переключении между инструментами.

## 日本語要約
このリポジトリは、複数のAI開発ツールにまたがる共通の operating law を説明します。Codex は主実行ハブ、Cursor は IDE ネイティブな実装層、Antigravity は広域能力プラットフォーム、Claude は依然として強力な workflow ベンチマークです。価値は単一の最強ツールではなく、ツールを切り替えても品質基準を保てるシステムにあります。

## Résumé français
Ce dépôt décrit une operating law commune à plusieurs outils IA de développement. Codex est le hub principal d’exécution, Cursor la couche d’implémentation native à l’IDE, Antigravity la plateforme de capacités larges, et Claude reste un benchmark solide de workflow. La valeur n’est pas un outil parfait, mais un système qui conserve un même niveau de qualité malgré les changements d’outil.

## What this means

This repository describes the Codex side of a larger cross-platform AI coding system.

In the live setup:
- `$SHARED_LAW_HOME/AGENTS.md` is the shared instruction entrypoint
- `$CODEX_HOME/config.toml` loads it through `shared-law loader`
- `$CODEX_HOME/instructions.md` adds Codex-specific guidance
- `<cursor-global-rules>` and project `<project>/<project>/.cursor/rules/` carry IDE-facing policy and delivery rules
- Antigravity carries broad skill and workflow execution through its own skills, workflows, and knowledge layers

So the Codex configuration is not isolated.

It is one governed endpoint inside a broader toolchain that also includes:
- Claude Code
- Cursor
- OpenCode
- Antigravity

## Why this matters

This changes the meaning of the repository.

It is not only:
- a Codex customization

It is also:
- the Codex execution layer of a shared agent operating system

It also changes the failure mode of the user's workflow.

Without a shared system, each tool becomes its own island:
- separate instructions
- separate habits
- separate quality bars
- separate recovery cost when switching

With a shared system:
- the user keeps one operating law
- tool switching becomes less destructive
- the workflow has more resilience when one endpoint is temporarily unavailable
- Claude can remain part of the system without being the single point of dependency

## Source influence

The cross-platform philosophy and part of the organizational inspiration come from:
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)

That project is useful because it treats agent quality as a harness and operating-system problem, not only a prompt problem.

## What is tool-specific here

### Codex

Even inside the shared system, the Codex side still has its own strengths:
- local terminal-first execution
- sandbox-aware action model
- governed skill composition
- release and publish guards
- role-based orchestration

### Cursor

The Cursor side is strongest when the workflow needs:
- IDE-native rule enforcement
- project-local `<project>/<project>/.cursor/rules/*.mdc`
- fast inline coding iteration
- less friction while staying inside the editor

### Antigravity

The Antigravity side is strongest when the workflow needs:
- very broad skill coverage
- browser and artifact-heavy work
- domain expansion beyond pure coding
- workflow and knowledge layers that feel closer to an AI platform

### Claude Code

Claude remains important in this setup because it is still a strong benchmark for:
- workflow ergonomics
- polished command culture
- mature collaboration feel

But the system is intentionally designed so that Claude does not have to be the only place where the user's engineering workflow lives.

## Practical takeaway

If you publish this repository, the clean framing is:

- shared cross-platform law at the top
- tool-specific execution layers beneath it
- concrete Codex / Cursor / Antigravity examples in the templates layer
