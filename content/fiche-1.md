---
title: "1. Un chatbot n'est pas un collègue"
graphe: ["source-05", "source-14", "source-15", "source-16", "source-17", "source-18"]
---

> Donner un cerveau à l'IA de votre équipe · fiche 1 sur 9 · version découpée du 01/10/26, d'après la version complète

↑ [[index|L'essentiel]] · [[fiche-2|2. Le cerveau, vu dans Obsidian]] →

Un modèle de langage (le moteur de ChatGPT, Claude, Gemini…) oublie tout d'une conversation à l'autre. Il ne voit que son **contexte**, ce qu'on lui montre quand il répond : une ressource finie, à remplir de peu d'informations, mais les bonnes [\[14\]](source-14).

Un chatbot y ajoute une « mémoire », une page de post-it sur vous ; un projet partagé de chatbot, des fichiers et des consignes communs [\[18\]](source-18), mais dans un seul outil, et c'est vous qui le remplissez. Une équipe a besoin d'un **dossier de notes** où l'IA travaille, en trois couches :

| Couche | Ce que c'est | Quand l'IA la lit |
|---|---|---|
| Règles | Un fichier court, AGENTS.md | À chaque session, en premier |
| Mémoire | Les notes du projet : but, sources, hypothèses, décisions, vocabulaire | Quand la tâche en a besoin, depuis le sommaire, index.md |
| Skills | Des procédures écrites une fois (« résoudre un conflit ») | Seulement quand la tâche l'exige |

Anthropic conseille ce montage dans beaucoup de cas : un socle court toujours chargé, le reste cherché à la demande [\[14\]](source-14). D'un skill, l'IA ne voit d'abord que le nom et la description, et ne lit le reste que si elle le juge utile [\[15\]](source-15) ([[fiche-6#Important|fiche 6]]).

Pour y travailler, il faut un **agent** (Claude Code chez Anthropic, Codex chez OpenAI…) : un modèle autorisé à modifier des fichiers et à lancer des commandes, dont git, l'outil d'historique des fichiers. Un chatbot ne le peut pas.

**Agnostique.** Tout est en fichiers texte versionnés par git. AGENTS.md est un format ouvert, compatible selon son site avec une vingtaine d'outils [\[16\]](source-16), certains après un réglage ([[fiche-7#Réglages par outil|fiche 7]]). Chacun garde son outil, et l'on change de modèle sans perdre la mémoire, à une condition : **un seul fichier de règles**.

> [!warning]- Le piège : AGENTS.md et CLAUDE.md
> Claude Code a son CLAUDE.md, Gemini CLI son GEMINI.md, Copilot un fichier d'instructions [\[17\]](source-17) [\[18\]](source-18). Si deux fichiers divergent, par exemple par une règle ajoutée dans CLAUDE.md, ceux qui utilisent Claude ne suivent plus les mêmes règles que les autres.
>
> Claude Code ne lit AGENTS.md que **s'il ne trouve aucun CLAUDE.md ni CLAUDE.local.md** dans le dossier ou au-dessus ; sinon, il l'ignore sans prévenir [\[17\]](source-17). Un membre qui se crée un CLAUDE.local.md pour ses préférences coupe donc, chez lui seul, les règles communes.
>
> La parade :
> 1. **Seul AGENTS.md contient des règles.**
> 2. **CLAUDE.md tient en une ligne, `@AGENTS.md`**, qui l'importe tel quel : Claude le lit alors dans tous les cas, même avec un CLAUDE.local.md, et jamais deux fois [\[17\]](source-17). « Lis AGENTS.md » ne suffit pas : Claude ne l'ouvrirait que s'il le décide [\[17\]](source-17).
> 3. **Pas de lien symbolique** entre les deux dès qu'un membre est sous Windows : git peut le récupérer comme un fichier texte d'une ligne, et Claude perd les règles [\[17\]](source-17).
> 4. **Même logique pour les autres outils** : leur fichier ne contient qu'un renvoi, ou l'outil est réglé pour lire AGENTS.md ([[fiche-7#Réglages par outil|fiche 7]]).
>
> Deux précautions encore : AGENTS.md n'utilise rien de propre à un outil (ni syntaxe d'import, ni nom de commande interne) ; et ce qui doit être retenu va dans le socle, jamais dans la mémoire automatique d'un outil, qui reste sur la machine du membre [\[17\]](source-17). Sur chaque poste, le test de la [[fiche-6#Critique|fiche 6]] prouve que l'IA lit les règles communes.

**Coût et gain.** Le socle coûte au début ; ensuite, chaque note écrite une fois sert à toutes les sessions de l'équipe. Rien n'est automatique pour autant : sur des tâches de code, un fichier de règles généré par l'IA n'améliore pas la réussite d'un agent et coûte plus cher ; écrit par l'équipe, il fait mieux [\[5\]](source-05). Le gain dépend de ce que vous écrivez.

> [!tip] Git en six mots
> **Dépôt** : le dossier partagé et son historique. **Cloner** : en faire une copie sur son poste. **Commit** : l'enregistrement d'un changement, avec son auteur et une phrase qui le décrit. **Push** : envoyer ses commits aux autres. **Pull** : récupérer ceux des autres. **Conflit** : deux personnes ont modifié les mêmes lignes, et git ne sait pas laquelle garder.

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- [\[5\]](source-05) **Un fichier de règles écrit par l'IA n'aide pas.** Celui qu'écrit l'équipe fait mieux. [Gloaguen et al., ETH Zurich, 29/09/26](https://arxiv.org/abs/2602.11988v3)
- [\[14\]](source-14) **Bien remplir le contexte d'une IA.** [Anthropic, « Effective context engineering », 29/09/25](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [\[15\]](source-15) **Les skills : des procédures lues à la demande.** [Anthropic, « Agent Skills », 16/10/25](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [\[16\]](source-16) **AGENTS.md, le format commun.** [agents.md](https://agents.md/)
- [\[17\]](source-17) **Règles, mémoire, hooks et interdits dans Claude Code.** [Mémoire et AGENTS.md](https://code.claude.com/docs/en/memory), [bonnes pratiques](https://code.claude.com/docs/en/best-practices), [hooks](https://code.claude.com/docs/en/hooks-guide), [permissions](https://code.claude.com/docs/en/permissions), [mode plan](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode), [PowerShell](https://code.claude.com/docs/en/permissions)
- [\[18\]](source-18) **Les outils d'IA et leurs prix.** Documentation : [skills de Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://learn.chatgpt.com/docs), [Gemini CLI](https://geminicli.com/docs), [Antigravity](https://antigravity.google/docs), [VS Code](https://code.visualstudio.com/docs), [Copilot](https://docs.github.com/en/copilot), [Cursor](https://cursor.com/docs), [Aider](https://aider.chat/docs). Modes plan : [Cursor](https://cursor.com/docs/agent/plan-mode), [Codex](https://learn.chatgpt.com/guides/best-practices), [Gemini CLI](https://geminicli.com/docs/cli/plan-mode/), [Antigravity](https://antigravity.google/docs/cli/modes/), [Copilot dans VS Code](https://code.visualstudio.com/docs/agents/run/planning), [Aider](https://aider.chat/docs/usage/modes.html). [Projets partagés de ChatGPT](https://help.openai.com/en/articles/10169521). Offres : [Obsidian](https://obsidian.md/blog/free-for-work/), [GitHub](https://docs.github.com/en/get-started/learning-about-github/githubs-products), [Claude](https://claude.com/pricing), [pack étudiant GitHub](https://education.github.com/pack)

↑ [[index|L'essentiel]] · [[fiche-2|2. Le cerveau, vu dans Obsidian]] →

Olivier & Mentordinator
