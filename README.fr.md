# Local AI Engineering Mesh

[中文](README.zh-CN.md) | [English](README.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md)

Transformez vos outils IA, d’assistants isolés, en un système d’ingénierie gouverné, doté de mémoire et fondé sur des preuves.

Ce dépôt n’est ni un pack de prompts ni une collection de skills. C’est un operating model présenté sous forme de dépôt pour faire passer des outils IA locaux de « sait répondre » à « sait exécuter un workflow d’ingénierie discipliné ».

L’idée centrale est simple : Codex ne doit pas fonctionner seul. Codex, Cursor, Antigravity, Claude Code et OpenCode peuvent devenir des endpoints spécialisés d’un même système d’IA de développement, coordonnés par un `AGENTS.md` unifié.

## Problème traité

La plupart des gens n’ont pas réellement un système IA. Ils ont surtout plusieurs outils entre lesquels ils basculent :
- un pour coder
- un pour la recherche
- un pour les tâches navigateur
- et un outil de secours quand le premier semble moins bon

Cela produit un schéma d’échec classique :
- changements d’outil permanents
- instructions dupliquées
- mémoire instable d’un outil à l’autre
- style et niveau de qualité variables
- dépendance au produit qui paraît le meilleur sur le moment

Ce dépôt existe pour transformer cet ensemble d’outils en un système cohérent.

## Ce que le dépôt améliore

- `shared law` : une loi commune via `AGENTS.md`
- `memory` : règles persistantes, routage et état du projet
- `bootstrap` : initialisation des commandes, de la mémoire et des limites de risque
- `orchestration` : rôles explicites pour planification, design, vérification et release
- `planning` : recherche d’abord, plan structuré ensuite
- `evidence` : la fin d’une tâche doit être prouvée, pas seulement racontée
- `release safety` : preview-first et publish gates
- `evolution` : les réussites répétées deviennent des capacités réutilisables

## Instantané du système réel

Ce dépôt s’appuie sur une configuration locale réellement opérationnelle. Au moment de la rédaction :
- `30` skills Codex dans `~/.codex/skills`
- `3` fichiers de mémoire globale dans `~/.codex/memories`
- `10` commandes de gouvernance dans `.codex/commands`
- `5` fichiers de mémoire projet dans `.codex/memory`
- des fichiers d’état actifs dans `.codex/state`

Ce n’est donc pas une simple théorie : le système fonctionne déjà au niveau des :
- règles
- skills
- runtime projet
- état
- preuves

## Évaluation des quatre outils sur cette machine

Ces notes ne sont pas des benchmarks universels. Elles reflètent une évaluation architecturale de cette configuration locale au **25 mars 2026**.

### Codex — 92/100
**Rôle :** centre principal d’exécution d’ingénierie et de gouvernance.

**Forces**
- centre d’exécution local le plus fort de cette configuration
- meilleur ensemble de skills gouvernés, commandes, discipline de release et evidence workflow
- excellent pour transformer un plan en livraison disciplinée

**Limites**
- dans certains workflows, l’expérience produit par défaut et la fluidité de l’automatisation restent moins naturelles que chez Claude

### Claude — 90/100
**Rôle :** moteur méthodologique de workflow et pile de référence.

**Forces**
- meilleur ressenti en matière de commandes et de workflow
- pensée modulaire, habitudes de review et ergonomie de collaboration très mûres
- reste un benchmark important pour le workflow de développement assisté par IA

**Limites**
- dans ce système local, il est moins profondément intégré à la gouvernance d’exécution que Codex

### Cursor — 89/100
**Rôle :** champ de bataille IDE et couche d’implémentation native à l’éditeur.

**Forces**
- le plus proche de la surface réelle du code
- forte densité de règles projet dans l’éditeur
- excellent pour réduire la friction quotidienne de développement

**Limites**
- plus faible que Codex ou Antigravity sur la gouvernance système et la sensation “operating system”

### Antigravity — 91/100
**Rôle :** plateforme d’extension de capacités.

**Forces**
- couverture large : navigateur, artifacts, knowledge, skills étendus
- ressemble davantage à une plateforme qu’à un simple outil
- très utile pour étendre les capacités et travailler sur plusieurs domaines

**Limites**
- cette largeur peut produire du bruit
- sur le chemin principal d’ingénierie, il n’est pas toujours aussi stable que Codex

### Système local global — 91/100
La vraie force de cette machine ne vient pas d’un seul AI “le meilleur”, mais du fait que les outils sont organisés en système :
- loi commune
- endpoints spécialisés multiples
- mémoire projet
- portes de contrôle d’exécution
- cohérence cross-platform

La formule la plus juste est :

**Shared Law + Multi-Tool Specialized AI System**

Ce n’est plus une configuration “choisir un seul outil”.
C’est un local AI engineering mesh coordonné.

## Structure cross-platform

Dans l’environnement réel derrière ce dépôt :
- `~/.codex/config.toml` charge `~/AGENTS.md` via `model_instructions_file`
- `~/.codex/instructions.md` ajoute le routing, les profiles et les skills spécifiques à Codex
- plusieurs outils de développement partagent la même loi de fonctionnement au sommet

Le système est donc à la fois :
- natif au niveau de l’exécution
- cohérent entre plateformes au niveau de la politique

Cela évite de redémarrer tout le workflow à zéro à chaque changement d’outil.

Voir [CROSS-PLATFORM.md](docs/CROSS-PLATFORM.md).

## Par rapport au dernier Claude

Au **23 mars 2026**, la pile publique Claude coding la plus récente chez Anthropic est menée par :
- `Claude Opus 4.6` publié le **5 février 2026**
- `Claude Sonnet 4.6` publié le **17 février 2026**

Ce dépôt ne prétend **pas** qu’un outil local bat automatiquement Claude sur la capacité brute du modèle.

Il défend une thèse plus étroite mais plus utile :

si l’on renforce l’operating layer des outils IA locaux, ils deviennent beaucoup plus compétitifs sur l’exécution d’ingénierie à long horizon, car le workflow ne dépend plus d’un prompt parfait ni d’un produit unique toujours disponible.

Voir [COMPARE-WITH-CLAUDE.md](docs/COMPARE-WITH-CLAUDE.md).
