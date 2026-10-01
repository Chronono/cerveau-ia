---
title: "Donner un cerveau à l'IA de votre équipe, l'essentiel"
graphe: ["fiche-1", "fiche-2", "fiche-3", "fiche-4", "fiche-5", "fiche-6", "fiche-7", "fiche-8", "fiche-9", "coulisses"]
---

> Fiche d'introduction pour toute équipe qui travaille avec une IA · écrite le 30/09/26 · ici, le résumé des neuf fiches découpées le 01/10/26 d'après la version complète · comment la version complète a été construite : [[coulisses|les coulisses]]

Cette page résume les neuf fiches et mène à chacune ; toutes les sources sont en bas. Si vous n'en lisez qu'une, lisez la [[fiche-4|fiche 4]]. Pour donner un cerveau à votre IA, un dépôt git de fichiers Markdown suffit, avec n'importe quel éditeur : « Obsidian », ici, est un mot d'habitude pour ce jeu de fichiers ([[fiche-2|fiche 2]]).

## En cinq lignes

1. Un chatbot oublie tout ; une IA efficace travaille dans un dossier de notes partagé qui lui sert de cerveau : le **socle**, avec ses règles, sa mémoire et ses savoir-faire.
2. Ce socle est un dépôt GitHub de fichiers Markdown : un seul cerveau pour l'équipe, que chacun voit, quel que soit son outil d'IA.
3. L'IA sera votre meilleur ami ou votre pire ennemi : elle amplifie ce qu'elle trouve. Ayez peur : contrôlez ce qu'elle sait, et ne perdez pas ce que vous savez.
4. L'étape cruciale : la nourrir de tout ce que vous savez, puis réfléchir avec elle, en retouchant son plan, avant d'agir ; et ne rien laisser entrer dans le socle que vous ne compreniez. Faites-en trop.
5. Une feuille de route pour démarrer. Ensuite, c'est l'IA qui tient l'historique partagé, sous des règles écrites et des interdits bloqués, et chaque erreur corrige le socle.

## Les neuf fiches

**[[fiche-1|1. Un chatbot n'est pas un collègue]]**
- Un modèle de langage oublie tout d'une conversation à l'autre : il ne voit que son contexte, une ressource finie, à remplir de peu d'informations, mais les bonnes.
- Le socle a trois couches : les **règles** (AGENTS.md, lues à chaque session), la **mémoire** (les notes du projet, lues à la demande en partant d'`index.md`), les **skills** (des procédures lues quand la tâche l'exige). Pour y travailler, il faut un **agent**, qui modifie les fichiers et lance git.
- Agnostique, à une condition : un seul fichier de règles. AGENTS.md les contient toutes ; pour Claude Code, un CLAUDE.md d'une ligne, `@AGENTS.md`.
- Le gain dépend de ce que vous écrivez : sur des tâches de code, un fichier de règles écrit par l'équipe fait mieux qu'un fichier généré par l'IA [\[5\]](source-05).

**[[fiche-2|2. Le cerveau, vu dans Obsidian]]**
- Des fichiers texte sur votre disque : vous lisez exactement ce que l'IA lit et ce que git versionne. Les liens relient les notes, les rétroliens montrent qui cite qui, le graphe montre les notes isolées, que l'IA risque de ne pas trouver.
- Ce que vous ne voyez pas, vous ne le contrôlez pas. Obsidian n'est pas obligatoire : n'importe quel éditeur convient. Un Drive peut remplacer GitHub, mais la feuille de route et le rituel reposent sur git, et un dépôt git ne se met jamais dans un dossier synchronisé par un cloud.

**[[fiche-3|3. Ayez peur]]**
- L'IA aide vraiment, mais ne prévient pas quand elle sort de son terrain : sur une tâche piège, 84,5 % de bonnes réponses sans elle, 60 à 71 % avec, et des réponses fausses mieux rédigées [\[1\]](source-01). Elle amplifie ce qui existe déjà [\[3\]](source-03).
- La méthode, pour toute tâche qui compte : le contexte, vos hypothèses, les siennes, vos réponses, la décision écrite, et alors seulement l'action.
- Le plus grand danger, c'est vous : l'ingénieur risque de perdre ce qu'il sait ; qui apprend, de ne jamais l'acquérir. Déléguez la tactique, gardez la stratégie, et comprenez les principes : savoir écrire chaque ligne n'est pas le but.

**[[fiche-4|4. L'étape cruciale : nourrir, puis réfléchir]]**
- **Nourrir** : une séance où toute l'équipe verse ce qu'elle sait, chaque chose à sa place (`projet.md`, `sources/`, `hypotheses/`, `decisions/`, `glossaire.md`), le solide séparé du supposé, jamais de secret. Faites-vous interroger par l'IA, puis testez avec une session neuve. Faites-en trop.
- **Réfléchir** : ne jamais s'arrêter à sa première réponse ; six réflexes (des options, la contestation, les sources, la réfutation, un autre regard, écrire ce qui sort). Avancez quand chaque hypothèse dont dépend la décision est vérifiée ou son risque accepté par écrit, que la décision est écrite avec ses options, et qu'une session neuve sait dire pourquoi.
- **Le mode plan** : l'IA propose, vous retouchez, passe après passe ; la puissance est dans vos retouches, et c'est là que se trace la ligne entre tactique et stratégie.
- **Le questionnaire**, si l'équipe l'adopte : avant chaque commit, trois à cinq questions sur ce qui entre (des principes, des conséquences, des points clés), dont au moins une piège ; ou bien vous expliquez, et l'IA corrige.

**[[fiche-5|5. La feuille de route]]**
Sept étapes, chacune avec son signe de réussite : s'équiper ; créer le dépôt ; poser les protections, prouvées avant le premier push ; écrire les règles ; répéter un conflit ; verser ce que vous savez ; poser la première vraie question. Les cinq premières se font une fois par équipe, et un nouveau poste en refait une partie ; les deux dernières ne s'arrêtent jamais.

**[[fiche-6|6. Le socle, par criticité]]**
- **Critique** : git réglé sur chaque poste, un dépôt GitHub privé, cloné hors de tout dossier synchronisé par un cloud, `.gitignore` et `.gitattributes` avant toute note, AGENTS.md, `index.md`, la mémoire nourrie, les skills resoudre-conflit et ecrire-decision, un contrôle de secrets prouvé sur chaque poste, les interdits bloqués, un responsable des règles.
- **Important** : les autres skills, le questionnaire si l'équipe l'adopte, un hook de démarrage si l'outil le permet. **Confort** : le plugin Git d'Obsidian.
- Trois exemples annotés, à lire avant d'écrire les vôtres : l'arborescence, AGENTS.md, un skill.

**[[fiche-7|7. Le rituel, tenu par l'IA]]**
- Au premier message : faire commiter ce qui traîne, avec votre accord, puis le pull, ce qui a changé depuis l'étiquette `vu`, le sommaire, ses questions. Avant chaque modification, un pull ; après, un commit dont le message dit le fait, puis le push.
- Une règle écrite reste un conseil : d'où le hook, quand l'outil le permet, et les interdits bloqués dans l'outil. Le commit porte votre nom : votre IA, votre responsabilité.

**[[fiche-8|8. Améliorer, niveau par niveau]]**
- Six niveaux : fonctionnel, cerveau nourri, réflexion écrite, skills, automatismes, serveur. Jugez sur ces critères, pas au ressenti : 16 développeurs expérimentés croyaient avoir gagné 20 % de temps avec l'IA, et en avaient mis 19 % de plus, avec les outils de début 2025 ; les mesures de fin 2025 penchent vers une accélération, sans effet établi [\[4\]](source-04).
- Chaque erreur corrige le socle, et AGENTS.md reste court. La veille est indispensable : étudiez avant d'employer.
- Plus tard, un serveur qui veille : il relit chaque commit, soumet les conflits au vote de l'équipe, et peut faire le point du matin.

**[[fiche-9|9. Dangers et parades]]**
Invention avec assurance, secrets poussés, agent qui détruit, compétences perdues, consignes cachées : à chacun son fait sourcé et sa parade.

Commencer la lecture : [[fiche-1|1. Un chatbot n'est pas un collègue]] →

## Toutes les sources

> [!note]- Les 21 sources, par famille (cliquez pour déplier)
> Dans les fiches, un numéro entre crochets, comme [\[3\]](source-03), renvoie à la source de ce numéro ; chaque fiche reprend en bas celles qu'elle cite. Pages sans date consultées le 30/09/26.
>
> **Ce que montrent les études** : les exemples des fiches.
>
> 1. **Quand l'IA aide, et quand elle trompe sans prévenir.** 758 consultants, avec et sans GPT-4. [Dell'Acqua et al., Harvard et BCG, *Organization Science*, 11/03/26](https://doi.org/10.1287/orsc.2025.21838)
> 2. **Se méfier de l'IA rend le code plus sûr.** Des participants, surtout des étudiants, avec et sans assistant de code. [Perry et al., Stanford, ACM CCS, 26/11/23](https://arxiv.org/abs/2211.03622)
> 3. **L'IA amplifie ce qui existe déjà.** Près de 5 000 professionnels du logiciel interrogés. [DORA, Google Cloud, 23/09/25](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)
> 4. **Le ressenti ne prouve rien.** Des développeurs se croyaient plus rapides avec l'IA, et l'étaient moins. [METR, étude du 12/07/25](https://arxiv.org/abs/2507.09089), puis [son suivi du 24/02/26](https://metr.org/blog/2026-02-24-uplift-update/)
> 5. **Un fichier de règles écrit par l'IA n'aide pas.** Celui qu'écrit l'équipe fait mieux. [Gloaguen et al., ETH Zurich, 29/09/26](https://arxiv.org/abs/2602.11988v3)
> 6. **L'IA tend à vous donner raison.** Cinq assistants d'IA de 2023 testés : ils adaptaient souvent leurs réponses à ce que l'utilisateur semblait croire, même quand il se trompait. [Sharma et al., Anthropic, ICLR 2024, 20/10/23](https://arxiv.org/abs/2310.13548)
> 7. **Les compétences s'usent quand la machine fait le travail.** Un essai classique sur l'automatisation des usines et des cockpits. [Bainbridge, « Ironies of Automation », *Automatica*, 1983](https://doi.org/10.1016/0005-1098(83)90046-8)
> 8. **Apprendre avec l'IA sans chercher à comprendre, c'est moins apprendre.** 52 développeurs qui découvraient une bibliothèque Python ; pas encore relue par des pairs. [Shen et Tamkin, Anthropic, 29/01/26](https://www.anthropic.com/research/AI-assistance-coding-skills), et [l'article](https://arxiv.org/abs/2601.20245)
> 9. **Se tester fait retenir, mieux que relire.** Des étudiants qui relisaient un texte ou écrivaient de mémoire ce qu'ils en retenaient, testés une semaine plus tard. [Roediger et Karpicke, *Psychological Science*, 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
>
> **Ce qui peut mal tourner** : les dangers de la [[fiche-9|fiche 9]].
>
> 10. **Des jurisprudences inventées, défendues devant un juge.** [Tribunal fédéral de New York, *Mata v. Avianca*, 22/06/23](https://www.nhd.uscourts.gov/sites/default/files/pdf/Mata-v-Avianca-sanctions-order.PDF)
> 11. **Des secrets poussés sur GitHub.** [GitGuardian, « State of Secrets Sprawl 2026 », 17/03/26](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/)
> 12. **Un agent qui efface des données de production.** [The Register, 21/07/25](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/)
> 13. **Des consignes invisibles dans un fichier de règles.** [Pillar Security, 18/03/25](https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents)
>
> **Les bonnes pratiques** : à lire pour aller plus loin.
>
> 14. **Bien remplir le contexte d'une IA.** [Anthropic, « Effective context engineering », 29/09/25](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
> 15. **Les skills : des procédures lues à la demande.** [Anthropic, « Agent Skills », 16/10/25](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
> 16. **AGENTS.md, le format commun.** [agents.md](https://agents.md/)
> 17. **Règles, mémoire, hooks et interdits dans Claude Code.** [Mémoire et AGENTS.md](https://code.claude.com/docs/en/memory), [bonnes pratiques](https://code.claude.com/docs/en/best-practices), [hooks](https://code.claude.com/docs/en/hooks-guide), [permissions](https://code.claude.com/docs/en/permissions), [mode plan](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode), [PowerShell](https://code.claude.com/docs/en/permissions)
>
> **Les outils** : pour installer et régler.
>
> 18. **Les outils d'IA et leurs prix.** Documentation : [skills de Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://learn.chatgpt.com/docs), [Gemini CLI](https://geminicli.com/docs), [Antigravity](https://antigravity.google/docs), [VS Code](https://code.visualstudio.com/docs), [Copilot](https://docs.github.com/en/copilot), [Cursor](https://cursor.com/docs), [Aider](https://aider.chat/docs). Modes plan : [Cursor](https://cursor.com/docs/agent/plan-mode), [Codex](https://learn.chatgpt.com/guides/best-practices), [Gemini CLI](https://geminicli.com/docs/cli/plan-mode/), [Antigravity](https://antigravity.google/docs/cli/modes/), [Copilot dans VS Code](https://code.visualstudio.com/docs/agents/run/planning), [Aider](https://aider.chat/docs/usage/modes.html). [Projets partagés de ChatGPT](https://help.openai.com/en/articles/10169521). Offres : [Obsidian](https://obsidian.md/blog/free-for-work/), [GitHub](https://docs.github.com/en/get-started/learning-about-github/githubs-products), [Claude](https://claude.com/pricing), [pack étudiant GitHub](https://education.github.com/pack)
> 19. **Obsidian, et l'autre choix.** [Où Obsidian range vos notes](https://obsidian.md/help/data-storage), [les liens](https://obsidian.md/help/links), [les rétroliens](https://obsidian.md/help/plugins/backlinks), [la vue graphe](https://obsidian.md/help/plugins/graph), [le plugin Git](https://github.com/Vinzent03/obsidian-git). Google Drive : [les fichiers .gdoc](https://knowledge.workspace.google.com/admin/drive/set-up-drive-for-desktop-for-your-organization), [les versions d'un fichier](https://support.google.com/drive/answer/2409045)
> 20. **Git, GitHub et le contrôle de secrets.** [Conflits et fusion](https://git-scm.com/docs/git-merge), [push refusé](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors), [fins de ligne](https://git-scm.com/docs/gitattributes), [pre-commit](https://pre-commit.com), [gitleaks](https://github.com/gitleaks/gitleaks), [ne pas synchroniser un dépôt par un cloud](https://git-scm.com/docs/gitfaq), [chercher dans les fichiers](https://git-scm.com/docs/git-grep), [les liens dans un fichier Markdown sur GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [les liens d'un wiki GitHub](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content)
> 21. **Les sondages par bot.** [Telegram](https://core.telegram.org/bots/api), [Discord](https://docs.discord.com/developers/resources/poll), [WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages)

Olivier & Mentordinator
