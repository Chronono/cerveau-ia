---
title: "2. Le cerveau de l'IA, vu dans Obsidian"
---

> Donner un cerveau à l'IA de votre équipe · fiche 2 sur 9 · version découpée du 01/10/26, d'après la version complète

↑ [[index|L'essentiel]] · ← [[fiche-1|1. Un chatbot n'est pas un collègue]] · [[fiche-3|3. Ayez peur]] →

> [!note] « Obsidian », un mot d'habitude
> Pour donner un cerveau à votre IA, un dépôt git de fichiers Markdown, de simples fichiers texte, suffit : aucun outil n'est nécessaire, un éditeur de texte convient. J'appelle souvent ce jeu de fichiers « Obsidian » par habitude, parce que c'est l'outil avec lequel je les lis ; ce n'est absolument pas une obligation. Obsidian apporte une lecture confortable du Markdown, et le graphe des liens entre vos notes.

Imaginez un collègue brillant qui perd la mémoire à chaque session : il ne sait que ce qu'il lit dans le carnet laissé par l'équipe. Ce carnet est le socle, son cerveau : vos notes sont ses souvenirs, leurs liens ses associations d'idées. Obsidian vous le montre, et vous permet de l'écrire et de l'entretenir [19] :
- **Des fichiers texte sur votre disque.** Chaque note est un fichier Markdown du dossier, le vault : vous lisez exactement ce que l'IA lit et écrit, et ce que git versionne. Ni format fermé, ni connecteur.
- **Les liens.** `[[decision-hebergeur]]` relie à la note de ce nom, écrit en clair : l'IA suit le lien comme vous. Hors du Markdown standard, cette syntaxe, que l'IA lit très bien, n'est prévue par GitHub que pour ses wikis ; pour un lien cliquable dans votre dépôt sur GitHub, écrivez un lien relatif, `[le choix de l'hébergeur](decisions/decision-hebergeur.md)` [20].
- **Les rétroliens** (*backlinks*) : les notes qui pointent vers une note ([[fiche-4#Nourrir le cerveau|fiche 4]]). Ce n'est qu'une recherche de son nom, enregistrée nulle part, qu'Obsidian affiche seul et à jour ; sans lui, `git grep -lF "[[decision-hebergeur"` [20], ou votre IA (« quelles notes citent decision-hebergeur ? »), donne la même liste.
- **La vue graphe** : chaque note est un point, chaque lien un trait ; un point isolé est un souvenir que l'IA risque de ne pas trouver ([[fiche-4#Nourrir le cerveau|fiche 4]]). C'est le seul vrai propre de l'outil : sans lui, « liste les notes que rien ne cite » se demande à l'IA, mais sans l'image.

| Sans cerveau partagé | Avec le socle |
|---|---|
| Chaque session repart de zéro : on réexplique le projet | L'IA lit le sommaire et reprend où l'équipe en est |
| Chacun a ses conversations, et sa version du projet | Un seul cerveau pour l'équipe, quel que soit l'outil de chacun |
| Le vérifié et le supposé se mélangent dans la conversation | Chaque note dit si elle est solide ou supposée, et d'où elle vient |
| Une décision se perd dans un fil de discussion | Elle a sa note : les options, le choix, le pourquoi |
| Quand une hypothèse tombe, personne ne sait ce qu'elle entraîne | Ses rétroliens montrent chaque note à revoir |
| Personne ne voit ce que sait l'IA | Vous le lisez, et le graphe montre les notes isolées |

Tout socle en fichiers texte donne les cinq premières lignes, les rétroliens par une simple recherche, qu'Obsidian affiche sans qu'on les demande ; seul le graphe, en image, lui est propre.

**Pourquoi c'est important** : l'IA amplifie ce qu'elle trouve ([[fiche-3|fiche 3]]), c'est-à-dire ce cerveau. Ce que vous ne voyez pas, vous ne le contrôlez pas : Obsidian vous le fait voir.

**Obsidian n'est pas obligatoire** (encadré) ; je le préconise parce que je l'utilise depuis longtemps et que j'aime beaucoup l'outil. **À la place de GitHub**, un Google Drive ou un autre cloud peut servir, mais la feuille de route ([[fiche-5|fiche 5]]) repose sur git : l'IA dit ce que ça change.

> [!quote] L'avis de l'IA
> Je ne vois ni Obsidian ni son graphe : je lis des fichiers et suis les liens écrits dedans. Ce qui compte, c'est le format, pas l'application. N'importe quel éditeur de texte remplace Obsidian sans rien changer au socle ni au rituel ; vous perdez l'affichage des rétroliens et le graphe, et c'est à moi, ou à une recherche, de trouver quelles notes en citent une autre.
>
> Remplacer git par un Drive change davantage. Un Google Doc n'est pas un fichier texte sur votre disque : Drive pour ordinateur n'y met qu'un raccourci, un fichier .gdoc qui pointe vers le document en ligne [19]. Pour le lire, il me faut un connecteur ou un export, et la méthode me demande d'écrire et de ranger vos notes, pas seulement de les lire. Des fichiers .md dans un Drive, je les lis ; mais Drive peut effacer les anciennes versions d'un fichier au bout de 30 jours [19], et le rituel repose sur git. Surtout, ne mettez pas un dépôt git dans un dossier synchronisé par un cloud : la documentation de git le déconseille, le dépôt peut se corrompre [20].
>
> Mon conseil : l'éditeur, choisissez-le ; les fichiers texte et git, gardez-les pour le socle ; le Drive peut garder le reste. Si vous hésitez, prenez Obsidian : il vous montre ce que je sais.
>
> Mon avertissement : Obsidian n'a rien de magique. Un vault sans liens n'est qu'un dossier ; le gain vient des notes que vous écrivez et des liens que vous tissez, pas de l'outil.

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- \[19] **Obsidian, et l'autre choix.** [Où Obsidian range vos notes](https://obsidian.md/help/data-storage), [les liens](https://obsidian.md/help/links), [les rétroliens](https://obsidian.md/help/plugins/backlinks), [la vue graphe](https://obsidian.md/help/plugins/graph), [le plugin Git](https://github.com/Vinzent03/obsidian-git). Google Drive : [les fichiers .gdoc](https://knowledge.workspace.google.com/admin/drive/set-up-drive-for-desktop-for-your-organization), [les versions d'un fichier](https://support.google.com/drive/answer/2409045)
- \[20] **Git, GitHub et le contrôle de secrets.** [Conflits et fusion](https://git-scm.com/docs/git-merge), [push refusé](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors), [fins de ligne](https://git-scm.com/docs/gitattributes), [pre-commit](https://pre-commit.com), [gitleaks](https://github.com/gitleaks/gitleaks), [ne pas synchroniser un dépôt par un cloud](https://git-scm.com/docs/gitfaq), [chercher dans les fichiers](https://git-scm.com/docs/git-grep), [les liens dans un fichier Markdown sur GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [les liens d'un wiki GitHub](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content)

↑ [[index|L'essentiel]] · ← [[fiche-1|1. Un chatbot n'est pas un collègue]] · [[fiche-3|3. Ayez peur]] →

Olivier & Mentordinator
