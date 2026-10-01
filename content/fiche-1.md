---
title: "1. Un chatbot n'est pas un collègue"
graphe: ["source-05", "source-14", "source-15", "source-16", "source-17", "source-18"]
---

↑ [[index|L'essentiel]] · [[fiche-2|2. Le cerveau, vu dans Obsidian]] →

Un modèle de langage (le moteur de ChatGPT, Claude, Gemini…) oublie tout d'une conversation à l'autre. Il ne voit que son **contexte**, ce qu'on lui montre quand il répond : une ressource finie, à remplir de peu d'informations, mais les bonnes [\[14\]](source-14).

> [!warning] Le piège de la longue session
> Beaucoup gardent une même session ouverte des jours durant, persuadés qu'elle connaît le projet de mieux en mieux. C'est l'inverse, pour trois raisons.
>
> 1. **Elle coûte de plus en plus.** À chaque message, le modèle relit toute la conversation : une question d'une ligne, dans une session ouverte depuis le matin, se paie au prix de toute la conversation. Le cache rend cette relecture moins chère, pas gratuite, et sur un abonnement c'est la limite d'usage que l'on atteint plus vite [\[17\]](source-17).
> 2. **Elle retrouve de moins en moins.** Plus le contexte est long, moins le modèle y retrouve ce qu'il cherche [\[14\]](source-14). Sur 18 modèles, dont Claude, GPT et Gemini, la réussite baisse avec la longueur, même pour recopier un texte ; et une longue conversation est mieux traitée réduite au passage utile qu'entière [\[14\]](source-14).
> 3. **Elle oublie en silence.** Près de la limite, l'outil résume l'historique : ce qui n'était dit que dans la conversation disparaît, quand la règle écrite dans un fichier est relue après le résumé [\[17\]](source-17). La « mémoire » d'une longue session est un résumé, écrit par le modèle. La vraie mémoire, c'est le socle.
>
> **Une session, une idée.** Tant que l'idée dure, l'historique a de la valeur : gardez-le [\[17\]](source-17). Quand elle est finie, rangez dans le socle ce qui doit rester, le réflexe « écrire ce qui sort » de la [[fiche-4#Réfléchir avec l'IA|fiche 4]], puis fermez la session. La suivante repart propre, et lit le socle.

Un chatbot y ajoute une « mémoire », une page de post-it sur vous ; un projet partagé de chatbot, des fichiers et des consignes communs [\[18\]](source-18), mais dans un seul outil, et c'est vous qui le remplissez. Une équipe a besoin d'un **dossier de notes** où l'IA travaille, en trois couches :

| Couche | Ce que c'est | Quand l'IA la lit |
|---|---|---|
| Règles | Un fichier court, AGENTS.md | À chaque session, en premier ; de nouveau après chaque résumé de la conversation |
| Mémoire | Les notes du projet : but, sources, hypothèses, décisions, vocabulaire | Quand la tâche en a besoin, depuis le sommaire, index.md |
| Skills | Des procédures écrites une fois (« résoudre un conflit ») | Seulement quand la tâche l'exige |

Anthropic conseille ce montage dans beaucoup de cas : un socle court toujours chargé, le reste cherché à la demande [\[14\]](source-14). D'un skill, l'IA ne voit d'abord que le nom et la description, et ne lit le reste que si elle le juge utile [\[15\]](source-15) ([[fiche-6#Important|fiche 6]]).

Pour y travailler, il faut un **agent** (Claude Code chez Anthropic, Codex chez OpenAI…) : un modèle autorisé à modifier des fichiers et à lancer des commandes, dont git, l'outil d'historique des fichiers. Un chatbot ne le peut pas.

> [!tip] Les mots de git
> **Git** : l'outil qui garde l'historique de vos fichiers ; **GitHub** : le site qui héberge le dépôt partagé. **Dépôt** : le dossier partagé et son historique. **Cloner** : en faire une copie sur son poste. **Commit** : l'enregistrement d'un changement, avec son auteur et une phrase qui le décrit. **Push** : envoyer ses commits aux autres. **Pull** : récupérer ceux des autres. **Conflit** : deux personnes ont modifié les mêmes lignes, et git ne sait pas laquelle garder.

**Agnostique.** Du grec *a-*, « sans », et *gnôsis*, « connaissance » : qui n'a pas besoin de savoir. En informatique, une ressource est agnostique quand elle fonctionne sans connaître le système qui l'utilise, donc sans dépendre d'un fournisseur [\[16\]](source-16). Ici, le cerveau de l'équipe ne dépend ni du modèle, Claude, GPT ou Gemini, ni de l'outil, Claude Code, Codex ou Cursor : tout est en fichiers texte versionnés par git, et AGENTS.md est un format ouvert, compatible selon son site avec une vingtaine d'outils [\[16\]](source-16), certains après un réglage ([[fiche-7#Réglages par outil|fiche 7]]). Chacun garde son outil, et l'on change de modèle sans perdre la mémoire, à une condition : **un seul fichier de règles**. L'agnosticité vaut pour les fichiers, pas pour les outils : chacun garde ses réglages et ses commandes.

> [!warning]- Le piège : AGENTS.md et CLAUDE.md
> Claude Code a son CLAUDE.md, Gemini CLI son GEMINI.md, Copilot un fichier d'instructions [\[17\]](source-17) [\[18\]](source-18). Si deux fichiers divergent, par exemple par une règle ajoutée dans CLAUDE.md, ceux qui utilisent Claude ne suivent plus les mêmes règles que les autres.
>
> Sans CLAUDE.md, un Claude Code à jour lit AGENTS.md de lui-même, et le dit au lancement : « no CLAUDE.md found; AGENTS.md loaded ». Mais dès qu'il trouve un CLAUDE.md ou un CLAUDE.local.md dans le dossier ou au-dessus, il ne lit que celui-là et ignore AGENTS.md sans prévenir [\[17\]](source-17). Un membre qui se crée un CLAUDE.local.md pour ses préférences coupe donc, chez lui seul, les règles communes.
>
> **Le piège.** Un CLAUDE.md qui dit « Lis AGENTS.md » ne suffit pas. C'est une phrase adressée au modèle : pour lire le fichier, il doit choisir d'appeler son outil de lecture, et un choix se saute, sur une tâche jugée simple, dans un contexte déjà chargé, après un résumé. Le modèle n'est pas déterministe, et la documentation le dit sans détour : Claude ne voit AGENTS.md que s'il décide de l'ouvrir [\[17\]](source-17). Même piège avec un lien symbolique dès qu'un membre est sous Windows : git peut le récupérer comme un fichier texte d'une ligne, et Claude perd les règles [\[17\]](source-17).
>
> **La parade.** Seul AGENTS.md contient des règles, et CLAUDE.md tient en une ligne, un **import** :
>
> ```
> @AGENTS.md
> ```
>
> Cette ligne n'est pas lue par le modèle : c'est le programme Claude Code qui, au lancement, colle le contenu d'AGENTS.md dans le contexte, avant que le modèle voie quoi que ce soit. C'est ce que fait le préprocesseur C avec `#include "regles.h"` : il colle le fichier à cet endroit, avant que le compilateur lise une ligne. Rien à décider, rien à espérer : les règles sont là dès le premier message, à chaque session, même avec un CLAUDE.local.md à côté, et jamais en double [\[17\]](source-17).
>
> D'où le principe : **ce qui doit être lu à chaque fois passe par le programme ; ce qui se lit à la demande passe par une phrase.** Le sommaire index.md et les skills se lisent sur une phrase, et c'est voulu : c'est ce qui garde le contexte petit ; rater une note coûte de la qualité, rater les règles coûte un push qui casse le travail des autres. La même logique fait d'un interdit un hook plutôt qu'une règle ([[fiche-7|fiche 7]]).
>
> Un réglage de Claude Code fait aussi lire les deux fichiers, mais il vit sur le poste de chacun, pas dans le dépôt [\[17\]](source-17) : l'import est la seule parade que git transporte. **Même logique pour les autres outils** : leur fichier ne contient qu'un renvoi, ou l'outil est réglé pour lire AGENTS.md ([[fiche-7#Réglages par outil|fiche 7]]).
>
> Deux précautions encore : AGENTS.md n'utilise rien de propre à un outil (ni syntaxe d'import, ni nom de commande interne) ; et ce qui doit être retenu va dans le socle, jamais dans la mémoire automatique d'un outil, qui reste sur la machine du membre [\[17\]](source-17). Sur chaque poste, le test de la [[fiche-6#Critique|fiche 6]] prouve que l'IA lit les règles communes.

**Coût et gain.** Le socle coûte au début ; ensuite, chaque note écrite une fois sert à toutes les sessions de l'équipe. Rien n'est automatique pour autant : sur des tâches de code, un fichier de règles généré par l'IA n'améliore pas la réussite d'un agent et le fait coûter 20 % de plus ; écrit par les développeurs, il fait mieux que lui, de peu [\[5\]](source-05). Ce qui marche, ce sont les consignes précises, que l'IA suit ; une description générale du projet ne sert à rien [\[5\]](source-05). Le gain dépend de ce que vous écrivez.

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- [\[5\]](source-05) **Un fichier de règles écrit par l'IA n'aide pas.** Celui qu'écrit l'équipe fait mieux. [Gloaguen et al., ETH Zurich, 29/09/26](https://arxiv.org/abs/2602.11988v3)
- [\[14\]](source-14) **Bien remplir le contexte d'une IA.** [Anthropic, « Effective context engineering », 29/09/25](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). La baisse avec la longueur, mesurée : [Chroma, « Context Rot », 18 modèles, 14/07/25](https://www.trychroma.com/research/context-rot) ; [Liu et al., « Lost in the Middle », TACL, 06/07/23](https://arxiv.org/abs/2307.03172)
- [\[15\]](source-15) **Les skills : des procédures lues à la demande.** [Anthropic, « Agent Skills », 16/10/25](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [\[16\]](source-16) **AGENTS.md, le format commun.** [agents.md](https://agents.md/). Le mot agnostique : [définition, LeMagIT, 19/04/18](https://www.lemagit.fr/definition/agnostique)
- [\[17\]](source-17) **Règles, mémoire, hooks et interdits dans Claude Code.** [Mémoire et AGENTS.md](https://code.claude.com/docs/en/memory), [bonnes pratiques](https://code.claude.com/docs/en/best-practices), [hooks](https://code.claude.com/docs/en/hooks-guide), [permissions](https://code.claude.com/docs/en/permissions), [mode plan](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode), [PowerShell](https://code.claude.com/docs/en/permissions), [les coûts d'une longue session](https://code.claude.com/docs/en/costs), [la fenêtre de contexte et le résumé](https://code.claude.com/docs/en/context-window)
- [\[18\]](source-18) **Les outils d'IA et leurs prix.** Documentation : [skills de Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://learn.chatgpt.com/docs), [Gemini CLI](https://geminicli.com/docs), [Antigravity](https://antigravity.google/docs), [VS Code](https://code.visualstudio.com/docs), [Copilot](https://docs.github.com/en/copilot), [Cursor](https://cursor.com/docs), [Aider](https://aider.chat/docs). Modes plan : [Cursor](https://cursor.com/docs/agent/plan-mode), [Codex](https://learn.chatgpt.com/guides/best-practices), [Gemini CLI](https://geminicli.com/docs/cli/plan-mode/), [Antigravity](https://antigravity.google/docs/cli/modes/), [Copilot dans VS Code](https://code.visualstudio.com/docs/agents/run/planning), [Aider](https://aider.chat/docs/usage/modes.html). [Projets partagés de ChatGPT](https://help.openai.com/en/articles/10169521). Offres : [Obsidian](https://obsidian.md/blog/free-for-work/), [GitHub](https://docs.github.com/en/get-started/learning-about-github/githubs-products), [Claude](https://claude.com/pricing), [pack étudiant GitHub](https://education.github.com/pack)

↑ [[index|L'essentiel]] · [[fiche-2|2. Le cerveau, vu dans Obsidian]] →

Olivier & Mentordinator
