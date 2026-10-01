---
title: "Donner un cerveau à l'IA de votre équipe, l'essentiel"
graphe: ["fiche-1", "fiche-2", "fiche-3", "fiche-4", "fiche-5", "fiche-6", "fiche-7", "fiche-8", "fiche-9", "coulisses"]
---

Cette page résume les neuf fiches et mène à chacune ; toutes les sources sont en bas. Si vous n'en lisez qu'une, lisez la [[fiche-4|fiche 4]]. Pour donner un cerveau à votre IA, un dépôt git de fichiers Markdown suffit, avec n'importe quel éditeur : « Obsidian », ici, est un mot d'habitude pour ce jeu de fichiers ([[fiche-2|fiche 2]]). Pour voir comment je me suis fait accompagner par l'IA pour construire ces fiches et ce site, lisez aussi [[coulisses|les coulisses]].

**Quatre mots.** Une **règle** : une consigne que l'IA lit à chaque session, avant tout ; les règles tiennent dans un fichier, AGENTS.md. La **mémoire** : les notes du projet, le but, les sources, les hypothèses, les décisions, le vocabulaire, que l'IA lit quand la tâche en a besoin, en partant d'un sommaire. Un **skill** : une procédure écrite une fois, par exemple « préparer un PowerPoint », avec le plan que l'équipe veut, son style et ce qu'on vérifie avant d'envoyer ; l'IA la lit seulement quand la tâche l'exige. Un **agent** : une IA autorisée à modifier vos fichiers et à lancer des commandes, dont git, sous réserve des règles écrites juste au-dessus ; un chatbot ne le peut pas.

**Les mots de git.** **Git** : l'outil qui garde l'historique de vos fichiers ; **GitHub** : le site qui héberge le dépôt partagé. **Dépôt** : le dossier partagé et son historique. **Cloner** : en faire une copie sur son poste. **Commit** : l'enregistrement d'un changement, avec son auteur et une phrase qui le décrit. **Push** : envoyer ses commits aux autres. **Pull** : récupérer ceux des autres. **Conflit** : deux personnes ont modifié les mêmes lignes, et git ne sait pas laquelle garder.

## En six lignes

1. Un chatbot oublie tout ; une IA efficace travaille dans un dossier de notes partagé qui lui sert de cerveau : le **socle**, avec ses règles, sa mémoire et ses skills.
2. Ce socle est un dépôt GitHub de fichiers Markdown : un seul cerveau pour l'équipe, que chacun voit, quel que soit son outil d'IA.
3. L'IA sera votre meilleur ami ou votre pire ennemi : elle amplifie ce qu'elle trouve. Ayez peur : contrôlez ce qu'elle sait, et ne perdez pas ce que vous savez.
4. L'étape cruciale : la nourrir de tout ce que vous savez, puis réfléchir avec elle, en retouchant son plan, avant d'agir ; et ne rien laisser entrer dans le socle que vous ne compreniez. Faites-en trop.
5. Une feuille de route pour démarrer. Ensuite, l'historique partagé, c'est git : c'est l'IA qui fait les pull, les commits et les push, sous des règles écrites et des interdits bloqués dans l'outil.
6. Quand l'IA se trompe, on corrige le socle, pas seulement sa réponse : la note qui manquait, on l'écrit ; la règle floue, on la reformule ; la procédure qu'on a dû réexpliquer devient un skill. Une erreur qui revient, c'est une règle qui manque.

## Les neuf fiches

**[[fiche-1|1. Un chatbot n'est pas un collègue]]**
- Un modèle de langage oublie tout d'une conversation à l'autre : il ne voit que son contexte, une ressource finie, à remplir de peu d'informations, mais les bonnes.
- Le piège de la longue session : à chaque message, le modèle relit toute la conversation ; plus elle est longue, moins il y retrouve ce qu'il cherche, et près de la limite l'outil la résume. Une session, une idée : ce qui doit rester va dans le socle, puis la session se ferme.
- Le socle a trois couches : les **règles** (AGENTS.md, lues à chaque session), la **mémoire** (les notes du projet, lues à la demande en partant d'`index.md`), les **skills** (des procédures lues quand la tâche l'exige). Pour y travailler, il faut un **agent**, qui modifie les fichiers et lance git.
- Agnostique, « sans avoir à savoir » quel outil ni quel modèle : le cerveau est en fichiers texte, chacun garde son outil d'IA, et l'équipe change de modèle sans rien perdre. À une condition : un seul fichier de règles, AGENTS.md ; pour Claude Code, un CLAUDE.md d'une ligne, `@AGENTS.md`, un import que le programme colle au lancement, là où la phrase « Lis AGENTS.md » laisse le modèle décider.
- Le gain dépend de ce que vous écrivez. Sur des tâches de code, un fichier de règles généré par l'IA n'améliore pas la réussite de l'agent et coûte 20 % de plus ; écrit par les développeurs, il fait mieux que lui, de peu [\[5\]](source-05). Ce qui marche, ce sont les consignes précises, que l'IA suit ; une description générale du projet ne sert à rien.

**[[fiche-2|2. Le cerveau, vu dans Obsidian]]**
- Le cerveau, ce sont des fichiers texte sur votre disque, reliés par des liens écrits en clair : vous lisez exactement ce que l'IA lit, et git garde l'historique. N'importe quel éditeur convient. Obsidian, en plus, affiche les rétroliens, qui cite une note, et le graphe, où une note isolée est un souvenir que l'IA risque de ne pas trouver.
- Ce que vous ne voyez pas, vous ne le contrôlez pas : l'IA amplifie ce qu'elle trouve dans ce cerveau, il faut donc pouvoir le lire en entier. Obsidian le montre ; un simple éditeur de texte le permet aussi.

**[[fiche-3|3. Ayez peur]]**
- L'IA aide vraiment, mais ne prévient pas quand elle sort de son terrain : elle fait ce qu'on lui demande même quand elle ne sait pas, sans le dire, parce qu'elle est faite pour vous satisfaire et tend à vous donner raison [\[6\]](source-06). Harvard et le BCG l'ont mesuré sur 758 consultants. Sur les tâches que l'IA savait faire, ceux qui l'avaient allaient plus vite et faisaient mieux. Sur une tâche construite pour la piéger, où la bonne réponse demandait de lire des entretiens aussi bien que des chiffres, ce que l'IA ratait, ils ont eu raison moins souvent que sans elle, 60 à 71 % contre 84,5 %, avec des réponses fausses mieux rédigées : ils avaient repris sa réponse sans l'interroger [\[1\]](source-01). Elle amplifie ce qui existe déjà [\[3\]](source-03).
- La méthode, pour toute tâche qui compte : le contexte, vos hypothèses, les siennes, vos réponses, la décision écrite, et alors seulement l'action.
- Le plus grand danger, c'est vous : l'ingénieur risque de perdre ce qu'il sait ; qui apprend, de ne jamais l'acquérir. Déléguez la tactique, gardez la stratégie, et comprenez les principes : savoir écrire chaque ligne n'est pas le but.

**[[fiche-4|4. L'étape cruciale : nourrir, puis réfléchir]]**
- **Nourrir** : une séance où toute l'équipe verse ce qu'elle sait, chaque chose à sa place (`projet.md`, `sources/`, `hypotheses/`, `decisions/`, `glossaire.md`), le solide séparé du supposé, jamais de secret. Faites-vous interroger par l'IA, puis testez avec une session neuve. Faites-en trop.
- **Réfléchir** : ne jamais s'arrêter à sa première réponse ; six réflexes (des options, la contestation, les sources, la réfutation, un autre regard, écrire ce qui sort). Avancez quand chaque hypothèse dont dépend la décision est vérifiée ou son risque accepté par écrit, que la décision est écrite avec ses options, et qu'une session neuve sait dire pourquoi.
- **Le mode plan** : l'IA propose, vous retouchez, passe après passe ; la puissance est dans vos retouches, et c'est là que se trace la ligne entre tactique et stratégie.
- **Le questionnaire**, si l'équipe l'adopte : avant chaque commit, trois à cinq questions sur ce qui entre (des principes, des conséquences, des points clés), dont au moins une piège ; ou bien vous expliquez, et l'IA corrige.
- Nourrir et réfléchir, c'est aussi ce qui vous protège du plus gros danger, la régression : perdre ce que vous savez faire, ou, quand on apprend, ne jamais l'acquérir. Servez-vous de l'IA pour apprendre et gagner en compétences, pas pour vous en dispenser.

**[[fiche-5|5. La feuille de route]]**
Sept étapes, chacune avec son signe de réussite.
1. S'équiper : git, un éditeur, un agent et un compte GitHub, chez chacun.
2. Créer le dépôt GitHub privé ; chacun le clone sur son poste.
3. Poser les protections : fichiers ignorés, contrôle de secrets, interdits bloqués, prouvées avant le premier push par un faux secret refusé.
4. Écrire les règles : AGENTS.md et les deux premiers skills.
5. Répéter un conflit : deux membres modifient exprès la même ligne, pour voir l'IA résoudre un conflit git avant qu'un vrai n'arrive.
6. Verser ce que vous savez : la séance de la [[fiche-4#Nourrir le cerveau|fiche 4]], où toute l'équipe nourrit le cerveau.
7. Poser la première vraie question : une question qui compte pour le projet, en mode plan, avec la méthode de la [[fiche-3#La méthode|fiche 3]] ; pas un essai pour voir.

Les étapes 1 à 5 se font une fois, à la création de l'équipe ; un nouveau membre refait la 1 et une partie des suivantes sur son poste. Les étapes 6 et 7 durent tout le projet : chaque chose apprise repasse par la 6, chaque question qui compte par la 7.

**[[fiche-6|6. Le socle, par criticité]]**
- **Critique** : git réglé sur chaque poste, un dépôt GitHub privé, cloné hors de tout dossier synchronisé par un cloud, `.gitignore` et `.gitattributes` avant toute note, AGENTS.md, `index.md`, la mémoire nourrie, les skills resoudre-conflit et ecrire-decision, un contrôle de secrets prouvé sur chaque poste, les interdits bloqués, un responsable des règles.
- **Important** : les autres skills, le questionnaire si l'équipe l'adopte, un hook de démarrage si l'outil le permet. **Confort** : le plugin Git d'Obsidian.
- Trois exemples annotés, à lire avant d'écrire les vôtres : l'arborescence, AGENTS.md, un skill.

**[[fiche-7|7. Le rituel, tenu par l'IA]]**
- Le rituel, ce sont les gestes git que l'IA fait à votre place, parce qu'un humain les oublie. Au premier message : elle fait commiter ce que vous avez écrit à la main, avec votre accord ; puis un pull, pour récupérer le travail des autres ; puis elle vous dit ce qui a changé depuis votre dernière session, lit le sommaire et pose ses questions. Avant chaque modification, un pull ; après, un commit dont le message dit le fait, puis le push.
- Pour savoir ce qui a changé, l'IA pose une étiquette git, `vu`, sur le dernier commit que vous avez lu ; elle reste sur votre poste et avance après chaque point.
- Une règle écrite reste un conseil : d'où le hook, une commande que l'outil lance seul à l'ouverture, quand il le permet, et les interdits bloqués dans ses réglages. Le commit porte votre nom : votre IA, votre responsabilité.

**[[fiche-8|8. Améliorer, niveau par niveau]]**
- Six niveaux : fonctionnel, cerveau nourri, réflexion écrite, skills, automatismes, serveur. Jugez sur ces critères, pas au ressenti : 16 développeurs expérimentés croyaient avoir gagné 20 % de temps avec l'IA, et en avaient mis 19 % de plus, avec les outils de début 2025 ; les mesures de fin 2025 penchent vers une accélération, sans effet établi [\[4\]](source-04).
- Chaque erreur corrige le socle, et AGENTS.md reste court. La veille technologique est indispensable : suivre, régulièrement et avec méthode, ce qui change dans vos outils et votre domaine, pour étudier avant d'employer et ne pas vous faire dépasser. Mettez-la en place dès le début ; comment faire : [\[22\]](source-22).
- Plus tard, un serveur qui veille : il relit chaque commit, soumet les conflits au vote de l'équipe, et peut faire le point du matin.

**[[fiche-9|9. Dangers et parades]]**
Le plus gros danger reste la régression : perdre la main sur ce que vous savez faire, ou ne jamais l'acquérir. Ce cerveau est là pour vous épargner ce qui vous prend du temps alors que vous le maîtrisez déjà, jamais pour vous dispenser de comprendre. Gardez la maîtrise, sinon c'est le mur. Puis cinq dangers, à chacun son fait sourcé et sa parade : invention avec assurance, secrets poussés, agent qui détruit, consignes cachées, compétences perdues.

Commencer la lecture : [[fiche-1|1. Un chatbot n'est pas un collègue]] →

## Toutes les sources

> [!note]- Les 22 sources, par famille (cliquez pour déplier)
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
> 14. **Bien remplir le contexte d'une IA.** [Anthropic, « Effective context engineering », 29/09/25](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). La baisse avec la longueur, mesurée : [Chroma, « Context Rot », 18 modèles, 14/07/25](https://www.trychroma.com/research/context-rot) ; [Liu et al., « Lost in the Middle », TACL, 06/07/23](https://arxiv.org/abs/2307.03172)
> 15. **Les skills : des procédures lues à la demande.** [Anthropic, « Agent Skills », 16/10/25](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
> 16. **AGENTS.md, le format commun.** [agents.md](https://agents.md/). Le mot agnostique : [définition, LeMagIT, 19/04/18](https://www.lemagit.fr/definition/agnostique)
> 17. **Règles, mémoire, hooks et interdits dans Claude Code.** [Mémoire et AGENTS.md](https://code.claude.com/docs/en/memory), [bonnes pratiques](https://code.claude.com/docs/en/best-practices), [hooks](https://code.claude.com/docs/en/hooks-guide), [permissions](https://code.claude.com/docs/en/permissions), [mode plan](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode), [PowerShell](https://code.claude.com/docs/en/permissions), [les coûts d'une longue session](https://code.claude.com/docs/en/costs), [la fenêtre de contexte et le résumé](https://code.claude.com/docs/en/context-window)
>
> **Les outils** : pour installer et régler.
>
> 18. **Les outils d'IA et leurs prix.** Documentation : [skills de Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://learn.chatgpt.com/docs), [Gemini CLI](https://geminicli.com/docs), [Antigravity](https://antigravity.google/docs), [VS Code](https://code.visualstudio.com/docs), [Copilot](https://docs.github.com/en/copilot), [Cursor](https://cursor.com/docs), [Aider](https://aider.chat/docs). Modes plan : [Cursor](https://cursor.com/docs/agent/plan-mode), [Codex](https://learn.chatgpt.com/guides/best-practices), [Gemini CLI](https://geminicli.com/docs/cli/plan-mode/), [Antigravity](https://antigravity.google/docs/cli/modes/), [Copilot dans VS Code](https://code.visualstudio.com/docs/agents/run/planning), [Aider](https://aider.chat/docs/usage/modes.html). [Projets partagés de ChatGPT](https://help.openai.com/en/articles/10169521). Offres : [Obsidian](https://obsidian.md/blog/free-for-work/), [GitHub](https://docs.github.com/en/get-started/learning-about-github/githubs-products), [Claude](https://claude.com/pricing), [pack étudiant GitHub](https://education.github.com/pack)
> 19. **Obsidian, et l'autre choix.** [Où Obsidian range vos notes](https://obsidian.md/help/data-storage), [les liens](https://obsidian.md/help/links), [les rétroliens](https://obsidian.md/help/plugins/backlinks), [la vue graphe](https://obsidian.md/help/plugins/graph), [le plugin Git](https://github.com/Vinzent03/obsidian-git). Google Drive : [les fichiers .gdoc](https://knowledge.workspace.google.com/admin/drive/set-up-drive-for-desktop-for-your-organization), [les versions d'un fichier](https://support.google.com/drive/answer/2409045)
> 20. **Git, GitHub et le contrôle de secrets.** [Conflits et fusion](https://git-scm.com/docs/git-merge), [push refusé](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors), [fins de ligne](https://git-scm.com/docs/gitattributes), [pre-commit](https://pre-commit.com), [gitleaks](https://github.com/gitleaks/gitleaks), [ne pas synchroniser un dépôt par un cloud](https://git-scm.com/docs/gitfaq), [chercher dans les fichiers](https://git-scm.com/docs/git-grep), [les liens dans un fichier Markdown sur GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [les liens d'un wiki GitHub](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content)
> 21. **Les sondages par bot.** [Telegram](https://core.telegram.org/bots/api), [Discord](https://docs.discord.com/developers/resources/poll), [WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages)
>
> **Se tenir à jour** : la veille de la [[fiche-8#La veille|fiche 8]].
>
> 22. **Organiser sa veille technologique.** Ce qu'est une veille, ses étapes, et comment l'automatiser par des alertes et des flux RSS. [Bibliothèques de l'Université Rennes 2, « Organiser sa veille informationnelle », 04/05/26](https://tutos.bu.univ-rennes2.fr/c.php?g=688574)

Olivier & Mentordinator
