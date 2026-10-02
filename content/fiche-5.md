---
title: "5. La feuille de route"
graphe: ["source-20"]
---

↑ [[index|L'essentiel]] · ← [[fiche-4|4. Nourrir, puis réfléchir]] · [[fiche-6|6. Le socle, par criticité]] →

Voici l'ordre ; le détail est dans les fiches [[fiche-4|4]], [[fiche-6|6]] et [[fiche-7|7]], celui du dépôt à l'étape 2. Chaque étape a son signe de réussite : ne passez à la suivante qu'après l'avoir vu.

| Étape | Qui | Ce qu'on fait | C'est réussi quand |
|---|---|---|---|
| 1. S'équiper | Chacun | Git, Obsidian (ou votre éditeur), un agent, un compte GitHub ([[fiche-6#Les gestes, un par un\|fiche 6]]). L'équipe désigne le responsable des règles et son suppléant | chacun a ouvert son agent dans un dossier, et il répond |
| 2. Créer le dépôt | Le responsable des règles | Le dépôt privé, créé avec un README (sur un dépôt vide, le premier pull échoue), et les invitations. Chacun accepte l'invitation, clone hors de tout dossier synchronisé par un cloud (sous Windows, Documents l'est souvent par OneDrive) [\[20\]](source-20), ouvre le dossier et règle git ([[fiche-6#Les gestes, un par un\|fiche 6]]) | chacun a vu son IA réussir un premier pull |
| 3. Poser les protections | Le responsable, avec son IA | L'arborescence, `.gitignore`, `.gitattributes`, le contrôle de secrets et les interdits bloqués (fiches [[fiche-6#Les gestes, un par un\|6]] et [[fiche-7#Réglages par outil\|7]]) | sur son poste, un faux secret est refusé au commit, et l'outil bloque `git push --force --dry-run` (un essai qui n'envoie rien) avec son propre message : un refus de l'IA ne compte pas. Alors seulement, le premier push |
| 4. Écrire les règles | Toute l'équipe ; le responsable tient la plume | AGENTS.md et les skills resoudre-conflit et ecrire-decision, à partir des exemples annotés ([[fiche-6#Trois exemples à lire, avant d'écrire les vôtres\|fiche 6]]), et, si l'équipe l'adopte, le questionnaire ([[fiche-4#Le questionnaire\|fiche 4]]). Puis chacun fait brancher par son IA le contrôle de secrets sur son poste et, hors Claude Code, les réglages de son outil ([[fiche-7#Réglages par outil\|fiche 7]]), et ouvre une nouvelle session | chez chacun, l'IA cite la première règle, et les deux preuves de l'étape 3 passent |
| 5. Répéter un conflit | Deux membres, A et B | A crée une note de test, son IA la pousse ; B la récupère. A fait modifier une ligne par son IA, qui commite sans pousser. B fait modifier la même ligne ; son IA commite et pousse. A demande alors le push : il est refusé, son IA fait le pull | l'IA de A ouvre le skill resoudre-conflit, et les deux versions restent lisibles dans l'historique |
| 6. Verser ce que vous savez | Toute l'équipe | La séance, puis chacun se fait interroger par l'IA ([[fiche-4#Nourrir le cerveau\|fiche 4]]) | une nouvelle session résume le projet, et vous n'avez rien d'important à corriger |
| 7. La première vraie question | Toute l'équipe | Une question qui compte, en mode plan, avec la méthode et les réflexes ([[fiche-3#La méthode\|fiche 3]], [[fiche-4#Réfléchir avec l'IA\|fiche 4]]) | les trois conditions de « Quand avancer » (fiche 4) sont remplies |

Déjà lancés dans le projet ? Pendant les étapes 1 à 5, rassemblez ce que vous verserez à l'étape 6 : cahier des charges, lectures, choix faits, doutes.

Les étapes 1 à 5 se font une fois par équipe ; un nouveau poste refait l'étape 1, le clone, le contrôle de secrets et les tests de l'étape 4. Les étapes 6 et 7 ne s'arrêtent jamais : chaque chose apprise, chaque nouvelle question y repasse. Ces sept étapes mènent au niveau 3 de la [[fiche-8|fiche 8]] ; la suite, ce sont les niveaux 4 à 6.

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- [\[20\]](source-20) **Git, GitHub et le contrôle de secrets.** [Conflits et fusion](https://git-scm.com/docs/git-merge), [push refusé](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors), [fins de ligne](https://git-scm.com/docs/gitattributes), [pre-commit](https://pre-commit.com), [gitleaks](https://github.com/gitleaks/gitleaks), [ne pas synchroniser un dépôt par un cloud](https://git-scm.com/docs/gitfaq), [chercher dans les fichiers](https://git-scm.com/docs/git-grep), [les liens dans un fichier Markdown sur GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [les liens d'un wiki GitHub](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content), [les worktrees](https://git-scm.com/docs/git-worktree), [les pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), [verrouiller un fichier avec Git LFS](https://github.com/git-lfs/git-lfs/wiki/File-Locking), [pandoc, du Markdown au PDF](https://pandoc.org/MANUAL.html)

↑ [[index|L'essentiel]] · ← [[fiche-4|4. Nourrir, puis réfléchir]] · [[fiche-6|6. Le socle, par criticité]] →

Olivier & Mentordinator
