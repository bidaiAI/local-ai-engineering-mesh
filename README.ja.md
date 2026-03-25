# Local AI Engineering Mesh

[中文](README.zh-CN.md) | [English](README.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md)

分断されたAIツールを、ガバナンス・記憶・証拠ベースの完了条件を備えたエンジニアリングシステムへアップグレードするためのリポジトリです。

これはプロンプト集でも skill の寄せ集めでもありません。ローカルAIツールを「答えられる」状態から「規律あるエンジニアリング運用ができる」状態へ引き上げる operating model です。

重要なのは、Codex を単独で使わないことです。Codex、Cursor、Antigravity、Claude Code、OpenCode を、共通の `AGENTS.md` の下で動くクロスプラットフォームAIコーディングシステムの各エンドポイントとして扱います。

## このリポジトリが解決する課題

多くの人は、実は本当の意味での AI システムを持っていません。あるのは複数ツールの行き来だけです。
- コーディング用
- 調査用
- ブラウザ操作用
- そして、最初のツールが弱く感じた時の予備ツール

その結果として起こるのは:
- ツール切り替えの多発
- 指示の重複
- ツール間での記憶の断絶
- 出力スタイルや品質基準のズレ
- その時いちばん便利な単一製品への依存

このリポジトリの目的は、そうしたローカルAIツール群を一つのシステムへ組み替えることです。

## 何を強化するのか

- `shared law`: `AGENTS.md` による共通上位ルール
- `memory`: 永続的な作業ルール、ルーティング、プロジェクト状態
- `bootstrap`: コマンド、記憶、リスク境界の初期化
- `orchestration`: 計画・設計・検証・リリースの明示的な役割分担
- `planning`: 先に調査し、その後に構造化された実行計画を作る
- `evidence`: 完了は物語ではなく証拠で定義する
- `release safety`: preview-first と publish gates
- `evolution`: 繰り返し成功した方法を再利用可能な能力へ昇格させる

## 実環境のスナップショット

このリポジトリは、実際に動いているローカル環境をもとにしています。README執筆時点での構成は次の通りです。
- `~/.codex/skills` に `30` 個の Codex skills
- `~/.codex/memories` に `3` 個のグローバル memory ファイル
- `.codex/commands` に `10` 個の governance commands
- `.codex/memory` に `5` 個の project memory ファイル
- `.codex/state` に state ファイル群

つまり、これは単なるアイデアではなく、すでに以下の層で稼働しています。
- rules layer
- skill layer
- project runtime layer
- state layer
- evidence layer

## このマシンにおける4ツール評価

以下のスコアは一般的なベンチマークではなく、**2026年3月25日** 時点のこのローカル構成に対するアーキテクチャ評価です。

### Codex — 92/100
**役割:** メインのエンジニアリング実行ハブ兼ガバナンス中枢。

**強み**
- この構成でもっとも強いローカル実行中心
- skills、commands、release discipline、evidence workflow が最も整っている
- 計画を規律ある実装と納品に変えるのに最適

**弱み**
- デフォルトの製品体験や自動化の滑らかさは、一部の場面で Claude に及ばない

### Claude — 90/100
**役割:** ワークフロー方法論エンジン兼リファレンススタック。

**強み**
- command-and-workflow 感が最も強い
- モジュール的思考、レビュー習慣、協調体験が成熟している
- AI coding workflow の基準として依然重要

**弱み**
- このローカルシステムでは、Codex ほど深く execution governance に組み込まれていない

### Cursor — 89/100
**役割:** IDE 主戦場と editor-native 実装層。

**強み**
- 実際のコーディング面に最も近い
- エディタ内 project rules の密度が高い
- 日常開発の摩擦を減らすのに非常に向いている

**弱み**
- system governance や operating-system 感は Codex / Antigravity より弱い

### Antigravity — 91/100
**役割:** 広域能力拡張プラットフォーム。

**強み**
- browser、artifacts、knowledge、拡張 skills までカバーが広い
- 単一ツールというよりプラットフォームに近い
- 能力拡張やクロスドメイン作業に強い

**弱み**
- 広さゆえにノイズが増えやすい
- コアなエンジニアリング主線では Codex ほど安定しない場合がある

### ローカル統合システム全体 — 91/100
このマシンの強さは、単一AIが最強だからではなく、複数ツールが一つのシステムとして編成されている点にあります。
- shared operating law
- 複数の specialized endpoints
- project memory
- execution gates
- cross-platform consistency

もっとも正確な表現は:

**Shared Law + Multi-Tool Specialized AI System**

これは「一つ選ぶ」構成ではありません。
協調的な local AI engineering mesh です。

## クロスプラットフォーム構成

実環境では:
- `~/.codex/config.toml` が `model_instructions_file` 経由で `~/AGENTS.md` を読み込む
- `~/.codex/instructions.md` が Codex 固有の routing、profiles、skills guidance を加える
- 複数の coding tools が同じ上位 operating law を共有する

つまり:
- 実行はツールネイティブ
- 方針はクロスプラットフォームで一貫

そのため、ツールを切り替えても workflow を最初からやり直す必要がありません。

詳細は [CROSS-PLATFORM.md](docs/CROSS-PLATFORM.md) を参照してください。

## 最新Claudeとの比較

**2026年3月23日** 時点で、Anthropic が公開している最新の Claude coding stack は次の通りです。
- `Claude Opus 4.6` — **2026年2月5日** 公開
- `Claude Sonnet 4.6` — **2026年2月17日** 公開

このリポジトリは、ローカルツールが生のモデル能力で自動的に Claude を上回るとは主張しません。

主張しているのは、もっと狭く、しかし実用的なことです。

ローカルAIツールの operating layer を強化すれば、長いエンジニアリング実行においては大きく競争力が増します。なぜなら、workflow が一つの完璧な prompt や、一つの常時利用可能な製品に依存しなくなるからです。

詳細は [COMPARE-WITH-CLAUDE.md](docs/COMPARE-WITH-CLAUDE.md) を参照してください。
