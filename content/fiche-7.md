---
title: "7. Le rituel, tenu par l'IA"
---

> Donner un cerveau à l'IA de votre équipe · fiche 7 sur 9 · version découpée du 01/10/26, d'après la version complète

↑ [[index|L'essentiel]] · ← [[fiche-6|6. Le socle, par criticité]] · [[fiche-8|8. Améliorer, niveau par niveau]] →

L'humain oublie le pull avant de travailler ; l'IA relit la règle à chaque session, en tête d'AGENTS.md ([[fiche-6#AGENTS.md, l'exemple|fiche 6]]). Mais une consigne écrite reste un conseil ; un hook s'exécute quoi que décide le modèle [17]. D'où trois étages : la règle pour tous, le hook quand l'outil le permet, les interdits bloqués dans ses réglages.

**Au premier message**, l'IA montre ce qui n'est pas commité (vos notes écrites dans Obsidian) et le fait commiter avec votre accord ; alors seulement, elle fait le pull, vous dit ce qui a changé, lit le sommaire et pose ses questions. **Avant chaque modification**, nouveau pull : un coéquipier a pu pousser. **Après**, commit des seuls fichiers touchés, avec un message qui dit le fait (« Ajoute la décision sur le fournisseur », pas « maj »), puis push ; si votre équipe a adopté le questionnaire, il passe avant le commit ([[fiche-4#Le questionnaire|fiche 4]]). DORA associe des commits fréquents à de meilleurs gains avec l'IA [3].

> [!question] Pourquoi commiter avant le pull, et pas l'inverse ?
> Dans le cas normal, l'IA fait bien le pull d'abord : avant chaque modification, sur un dossier propre, rien ne peut entrer en conflit. Le commit passe avant le pull dans deux cas seulement : il reste des notes écrites à la main, ou le push a été refusé parce qu'un coéquipier a poussé entre-temps. Le travail existe déjà ; il faut le mettre à l'abri avant de récupérer celui des autres.
> - **Un commit reste sur votre poste.** Le conflit se règle chez vous, jamais sur GitHub ([[fiche-8#Plus tard, un serveur qui veille|fiche 8]]).
> - **Un commit est un point de retour.** Si la fusion tourne mal, `git merge --abort` vous ramène exactement à ce commit.
> - **Des modifications non commitées sont fragiles.** Si le pull touche les mêmes fichiers, git refuse de le faire ; s'il le fait et que la fusion rate, il ne sait pas toujours les reconstruire [20].

## Ce qui a changé

Le socle sait tout ce que l'équipe y a écrit ; vous, seulement ce que vous avez lu. D'où ce point, au premier message : ce qui a changé depuis votre dernière session, regroupé par auteur et par sujet. L'IA s'y retrouve grâce à une étiquette git, `vu`, qui ne quitte pas votre poste : elle marque ce que vous avez déjà vu, et l'IA la déplace après chaque point. À tout moment, demandez aussi un rapport de ce que le socle dit d'un sujet, ou de ce qui a bougé en dernier. Lisez-le comme si un coéquipier vous parlait, et posez vos questions ; le questionnaire peut s'y appliquer aussi ([[fiche-4#Le questionnaire|fiche 4]]). Tant que vous continuez de nourrir le socle vous-mêmes et de lire ce qu'y versent les autres, vous gardez la main dessus. Un serveur peut faire ce rapport chaque matin ([[fiche-8#Plus tard, un serveur qui veille|fiche 8]]).

**Pour revenir en arrière**, décrivez le résultat voulu, pas la commande : « remets cette note comme avant ma dernière modification ». L'IA choisit la commande ; celles qui détruisent sont bloquées ou soumises à votre accord (réglages ci-dessous). Demandez-lui ce qu'elle va lancer, et pourquoi, avant de dire oui.

**En cas de conflit**, git s'arrête et inscrit les deux versions dans le fichier, entre des marqueurs `<<<<<<<` et `>>>>>>>` [20] ; l'IA suit le skill resoudre-conflit ([[fiche-6#Un skill, l'exemple, resoudre-conflit|fiche 6]]). Un conflit signalé par Obsidian ne se résout ni à la main ni sur téléphone : ouvrez votre IA.

**Le blocage des interdits** arrête l'erreur courante, pas un contournement : selon la documentation de Claude Code, sa liste n'est « pas une barrière de sécurité » [17].

**Responsabilité.** Le commit porte le nom du membre : son IA, sa responsabilité. Plusieurs outils (Claude Code, Cursor, Aider…) ajoutent une ligne `Co-authored-by` qui nomme l'IA [18] : gardez-la.

## Réglages par outil

> [!note]- Au 30/09/26 : lisez-les, puis faites-les poser par votre IA
> - **Claude Code**, `.claude/settings.json`, versionné [17] :
> ```json
> {"hooks": {"SessionStart": [{"matcher": "startup|resume",
>    "hooks": [{"type": "command", "command": "git pull --ff-only"}]}]},
>  "permissions": {
>    "allow": ["Bash(git status*)", "Bash(git diff*)", "Bash(git log*)",
>      "Bash(git tag -f vu)", "Bash(git pull*)", "Bash(git add *)",
>      "Bash(git commit *)", "Bash(git push)"],
>    "ask": ["Bash(git stash*)", "Bash(git clean*)", "Bash(git restore*)",
>      "Bash(git checkout -- *)", "Bash(rm *)"],
>    "deny": ["Bash(git push *--force*)", "Bash(git push -f*)", "Bash(git push * -f*)",
>      "Bash(git reset --hard*)", "Bash(git commit *--no-verify*)",
>      "Bash(git commit -n*)", "Bash(git commit * -n*)"]}}
> ```
> Comment c'est construit. `hooks` : le pull lancé à chaque ouverture ; avec `--ff-only`, s'il fallait fusionner, le pull échoue sans rien toucher, et l'IA suit le rituel. `allow` : le quotidien, sans demander. `ask` : l'outil demande votre accord. `deny` : jamais. Ces listes reprennent les interdits d'AGENTS.md : la règle écrite, puis son blocage. `-n` est la forme courte de `--no-verify`. Sous Windows, Claude Code peut lancer ses commandes en PowerShell : si un membre est sous Windows, le responsable fait doubler par son IA chaque règle `Bash(...)` d'une règle `PowerShell(...)` [17], et chacun refait le test du push à blanc.
> - **Autres outils** : le responsable valide, d'après leur documentation [18], la lecture d'AGENTS.md, le hook et les permissions. Deux pièges : Codex ne charge le hook du projet que si le dossier est déclaré de confiance, sinon pas de pull automatique, sans message ; Aider ne fait ni pull ni push seul, et demande votre accord à chaque commande (exception au « sans rappel » du niveau 1, [[fiche-8|fiche 8]]).

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- \[3] **L'IA amplifie ce qui existe déjà.** Près de 5 000 professionnels du logiciel interrogés. [DORA, Google Cloud, 23/09/25](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)
- \[17] **Règles, mémoire, hooks et interdits dans Claude Code.** [Mémoire et AGENTS.md](https://code.claude.com/docs/en/memory), [bonnes pratiques](https://code.claude.com/docs/en/best-practices), [hooks](https://code.claude.com/docs/en/hooks-guide), [permissions](https://code.claude.com/docs/en/permissions), [mode plan](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode), [PowerShell](https://code.claude.com/docs/en/permissions)
- \[18] **Les outils d'IA et leurs prix.** Documentation : [skills de Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://learn.chatgpt.com/docs), [Gemini CLI](https://geminicli.com/docs), [Antigravity](https://antigravity.google/docs), [VS Code](https://code.visualstudio.com/docs), [Copilot](https://docs.github.com/en/copilot), [Cursor](https://cursor.com/docs), [Aider](https://aider.chat/docs). Modes plan : [Cursor](https://cursor.com/docs/agent/plan-mode), [Codex](https://learn.chatgpt.com/guides/best-practices), [Gemini CLI](https://geminicli.com/docs/cli/plan-mode/), [Antigravity](https://antigravity.google/docs/cli/modes/), [Copilot dans VS Code](https://code.visualstudio.com/docs/agents/run/planning), [Aider](https://aider.chat/docs/usage/modes.html). [Projets partagés de ChatGPT](https://help.openai.com/en/articles/10169521). Offres : [Obsidian](https://obsidian.md/blog/free-for-work/), [GitHub](https://docs.github.com/en/get-started/learning-about-github/githubs-products), [Claude](https://claude.com/pricing), [pack étudiant GitHub](https://education.github.com/pack)
- \[20] **Git, GitHub et le contrôle de secrets.** [Conflits et fusion](https://git-scm.com/docs/git-merge), [push refusé](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors), [fins de ligne](https://git-scm.com/docs/gitattributes), [pre-commit](https://pre-commit.com), [gitleaks](https://github.com/gitleaks/gitleaks), [ne pas synchroniser un dépôt par un cloud](https://git-scm.com/docs/gitfaq), [chercher dans les fichiers](https://git-scm.com/docs/git-grep), [les liens dans un fichier Markdown sur GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [les liens d'un wiki GitHub](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content)

↑ [[index|L'essentiel]] · ← [[fiche-6|6. Le socle, par criticité]] · [[fiche-8|8. Améliorer, niveau par niveau]] →

Olivier & Mentordinator
