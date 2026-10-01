---
title: "2. Le cerveau de l'IA, vu dans Obsidian"
graphe: ["source-19", "source-20"]
---

↑ [[index|L'essentiel]] · ← [[fiche-1|1. Un chatbot n'est pas un collègue]] · [[fiche-3|3. Ayez peur]] →

> [!note] « Obsidian », un mot d'habitude
> Pour donner un cerveau à votre IA, un dépôt git de fichiers Markdown, de simples fichiers texte, suffit : aucun outil particulier n'est nécessaire, un éditeur de texte convient. J'appelle souvent ce jeu de fichiers « Obsidian » par habitude, parce que c'est l'outil avec lequel je les lis ; ce n'est absolument pas une obligation. Je le préconise parce que j'aime cet outil, et que je l'utilisais bien avant l'IA : il apporte une lecture confortable du Markdown, et le graphe des liens entre vos notes, que j'ai refait sur ce site. C'est la vue graphique, à droite sur ordinateur, en bas de page après les sources sur téléphone ; pour rester lisible, elle ne trace que les liens de L'essentiel vers les fiches et des fiches vers leurs sources, en orange.

Imaginez un collègue brillant qui perd la mémoire à chaque session : il ne sait que ce qu'il lit dans les notes laissées par l'équipe. Ces notes sont sa **mémoire**, l'une des trois couches du **socle**, le dossier de fichiers texte où l'IA travaille ([[fiche-1|fiche 1]]). Ce socle est son **cerveau** : vos notes sont ses souvenirs, leurs liens ses associations d'idées. Obsidian appelle ce dossier un *vault* ; il vous le montre, et vous permet de l'écrire et de l'entretenir [\[19\]](source-19) :
- **Des fichiers texte sur votre disque.** Chaque note est un fichier Markdown du vault : vous lisez exactement ce que l'IA lit et écrit, et ce que git versionne. Ni format fermé, ni connecteur.
- **Les liens.** `[[decision-hebergeur]]` relie à la note de ce nom, écrit en clair : l'IA suit le lien comme vous. Cette syntaxe n'est pas du Markdown standard : l'IA la lit très bien, mais GitHub ne la reconnaît que dans ses wikis [\[20\]](source-20). C'est pourquoi je conseille un lecteur Markdown qui sait suivre ces liens, Obsidian ou un autre ; pour un lien cliquable dans votre dépôt vu sur GitHub, écrivez un lien relatif, `[le choix de l'hébergeur](decisions/decision-hebergeur.md)`.
- **Les rétroliens** (*backlinks*). Les rétroliens d'une note sont la liste des notes qui contiennent un lien vers elle : ouvrez `decision-hebergeur`, et Obsidian affiche à côté chaque note qui la cite, sans que vous ayez rien à écrire, toujours à jour ([[fiche-4#Nourrir le cerveau|fiche 4]]). Sans Obsidian, une recherche de texte donne la même liste : `git grep -l decision-hebergeur` [\[20\]](source-20), où grep est la commande qui cherche un texte dans des fichiers, `git grep` sa version livrée avec git, qui fouille les fichiers du dépôt, sur Windows comme ailleurs, et `-l` ne garde que les noms des fichiers trouvés. Ou votre IA : « quelles notes citent decision-hebergeur ? ».
- **La vue graphe** : chaque note est un point, chaque lien un trait ; un point isolé est un souvenir que l'IA risque de ne pas trouver ([[fiche-4#Nourrir le cerveau|fiche 4]]). C'est la vraie différence d'Obsidian avec les autres outils Markdown, et elle montre à quel point le choix d'Obsidian compte peu : sans lui, « liste les notes que rien ne cite » se demande à l'IA, mais sans l'image.

| Sans cerveau partagé | Avec le socle |
|---|---|
| Chaque session repart de zéro : on réexplique le projet | L'IA lit le sommaire et reprend où l'équipe en est |
| Chacun a ses conversations, et sa version du projet | Un seul cerveau pour l'équipe, quel que soit l'outil de chacun |
| Le vérifié et le supposé se mélangent dans la conversation | Chaque note dit si elle est solide ou supposée, et d'où elle vient |
| Une décision se perd dans un fil de discussion | Elle a sa note : les options, le choix, le pourquoi |
| Quand une hypothèse tombe, personne ne sait ce qu'elle entraîne | Ses rétroliens montrent chaque note à revoir |
| Personne ne voit ce que sait l'IA | Vous le lisez, et le graphe montre les notes isolées |

Tout socle en fichiers texte donne les cinq premières lignes ; seule la dernière demande le graphe. Comment une note dit le solide et le supposé, et d'où elle vient : [[fiche-4#Nourrir le cerveau|fiche 4]].

**Pourquoi c'est important** : l'IA amplifie ce qu'elle trouve ([[fiche-3|fiche 3]]), c'est-à-dire ce cerveau. Ce que vous ne voyez pas, vous ne le contrôlez pas : Obsidian vous le fait voir.

**À la place de GitHub**, un Google Drive ou un autre cloud peut servir, mais la feuille de route ([[fiche-5|fiche 5]]) repose sur git : l'IA dit ce que ça change.

> [!quote] L'avis de l'IA
> Je ne vois ni Obsidian ni son graphe : je lis des fichiers et suis les liens écrits dedans. Ce qui compte, c'est le format, pas l'application.
>
> Remplacer git par un Drive change davantage. Un Google Doc n'est pas un fichier texte sur votre disque : Drive pour ordinateur n'y met qu'un raccourci, un fichier .gdoc qui pointe vers le document en ligne [\[19\]](source-19). Pour le lire, il me faut un connecteur ou un export, et la méthode me demande d'écrire et de ranger vos notes, pas seulement de les lire. Des fichiers .md dans un Drive, je les lis ; mais Drive peut effacer les anciennes versions d'un fichier au bout de 30 jours [\[19\]](source-19), et le rituel repose sur git. Surtout, ne mettez pas un dépôt git dans un dossier synchronisé par un cloud : la documentation de git le déconseille, le dépôt peut se corrompre [\[20\]](source-20).
>
> Mon conseil : l'éditeur, choisissez-le ; les fichiers texte et git, gardez-les pour le socle ; le Drive peut garder le reste. Si vous hésitez, prenez Obsidian : il vous montre ce que je sais.
>
> Mon avertissement : Obsidian n'a rien de magique. Un vault sans liens n'est qu'un dossier ; le gain vient des notes que vous écrivez et des liens que vous tissez, pas de l'outil.

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- [\[19\]](source-19) **Obsidian, et l'autre choix.** [Où Obsidian range vos notes](https://obsidian.md/help/data-storage), [les liens](https://obsidian.md/help/links), [les rétroliens](https://obsidian.md/help/plugins/backlinks), [la vue graphe](https://obsidian.md/help/plugins/graph), [le plugin Git](https://github.com/Vinzent03/obsidian-git). Google Drive : [les fichiers .gdoc](https://knowledge.workspace.google.com/admin/drive/set-up-drive-for-desktop-for-your-organization), [les versions d'un fichier](https://support.google.com/drive/answer/2409045)
- [\[20\]](source-20) **Git, GitHub et le contrôle de secrets.** [Conflits et fusion](https://git-scm.com/docs/git-merge), [push refusé](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors), [fins de ligne](https://git-scm.com/docs/gitattributes), [pre-commit](https://pre-commit.com), [gitleaks](https://github.com/gitleaks/gitleaks), [ne pas synchroniser un dépôt par un cloud](https://git-scm.com/docs/gitfaq), [chercher dans les fichiers](https://git-scm.com/docs/git-grep), [les liens dans un fichier Markdown sur GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [les liens d'un wiki GitHub](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content)

↑ [[index|L'essentiel]] · ← [[fiche-1|1. Un chatbot n'est pas un collègue]] · [[fiche-3|3. Ayez peur]] →

Olivier & Mentordinator
