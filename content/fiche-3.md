---
title: "3. Ayez peur"
graphe: ["source-01", "source-02", "source-03", "source-06", "source-07", "source-08"]
---

↑ [[index|L'essentiel]] · ← [[fiche-2|2. Le cerveau, vu dans Obsidian]] · [[fiche-4|4. Nourrir, puis réfléchir]] →

Vous l'avez sans doute déjà remarqué : l'IA vous rend plus productifs. La mesure existe. Dans une expérience de Harvard et du BCG (758 consultants), ceux qui avaient GPT-4 ont fini, sur les tâches que l'IA savait faire, environ 12 % de tâches en plus, 25 % plus vite, avec un travail jugé plus de 30 % meilleur [\[1\]](source-01).

La même expérience a une seconde moitié, une tâche d'apparence aussi difficile, mais construite pour que l'IA se trompe : dire au PDG laquelle de trois marques développer, avec un tableur de chiffres et des entretiens d'initiés ; le tableur seul semblait suffire, mais un détail des entretiens renversait la conclusion, et GPT-4, nourri de tout, le ratait. 84,5 % de bonnes réponses sans IA, 60 à 71 % avec, et des réponses fausses mieux rédigées ; ceux qui s'étaient trompés avaient repris sa réponse sans l'interroger [\[1\]](source-01). L'IA ne prévient pas quand elle sort de son terrain : elle fait ce qu'on lui demande même quand elle ne sait pas, sans le dire, parce qu'elle est faite pour vous satisfaire, au point de vous donner raison ([[fiche-4#Réfléchir avec l'IA|fiche 4]]) [\[6\]](source-06).

Alors vous pouvez avoir peur de construire ce cerveau : peur de perdre la main, de vous retrouver avec des dizaines, voire des centaines de notes écrites par l'IA sans vraiment savoir ce qui se passe, de ne plus pouvoir dire pourquoi votre projet est fait comme il est. Vous avez raison. Je vous recommande même d'être absolument effrayés. Si vous avez peur, vous allez vouloir contrôler ce que votre socle sait, travailler avec l'IA sur vos incertitudes et vos hypothèses, répondre aux siennes, et ensuite décider. Plus vous avez peur, plus ce sera solide.

Mais avoir peur n'est pas tout relire. Un manager qui vérifie chaque ligne de son équipe est un micro-manager : il perd plus de temps qu'il ne gagne de contrôle. Un commandant ne suit pas chaque soldat ; il s'assure que les ordres portent la stratégie et que chacun les a compris. Avec l'IA, la peur utile porte sur ce qu'elle sait, sur vos hypothèses et sur vos décisions, pas sur chaque ligne qu'elle écrit. Un ingénieur DevOps le dit plus bas, en termes de tactique et de stratégie.

Deux peurs, donc, et cette fiche répond aux deux : d'abord ce que l'IA sait et suppose, par une méthode ; puis ce que vous pourriez perdre en travaillant avec elle.

## La méthode

Pour toute tâche qui engage le projet : un choix d'architecture, un fournisseur, une semaine de travail. Pas pour un changement qui se dit en une phrase.
1. **Le contexte** : l'IA lit ce que le socle sait du sujet ; vous complétez, et ce qui manquait entre dans le socle ([[fiche-4#Nourrir le cerveau|fiche 4]]).
2. **Vos hypothèses et incertitudes.**
3. **Ses hypothèses et ses questions**, qu'elle liste à votre demande avant d'agir ([[fiche-4#Le mode plan|fiche 4, mode plan]]).
4. **Vos réponses** ; l'inconnu va dans `hypotheses/`.
5. **La décision**, humaine. L'IA l'écrit dans `decisions/`, avec les options et vos raisons, et range l'inconnu dans `hypotheses/`, statut « à vérifier » ([[fiche-4#Réfléchir avec l'IA|fiche 4, « Écrire ce qui sort »]]). Vous relisez ce qu'elle a écrit : une minute, et c'est elle qui vous garde la main.
6. **Alors seulement, l'action.** À la tâche suivante, l'étape 1 relira ces notes : votre décision d'hier est le contexte d'aujourd'hui.

> [!example] Une demande, vue de l'intérieur
> Un exemple à lire, pas à coller :
>
> « Nous devons choisir notre fournisseur d'hébergement. Lis d'abord index.md et les notes de decisions/ qui en parlent. Nous supposons que notre trafic restera faible ; nous ne savons pas ce que coûtent les sauvegardes. Avant d'agir, liste ce que tu supposes et ce qu'il te faut savoir. Ne propose rien avant nos réponses. »
>
> | Partie | Pourquoi elle est là |
> |---|---|
> | « Nous devons choisir… » | Le but, en une phrase ; sans lui, l'IA devine ce que vous voulez. |
> | « Lis d'abord index.md… » | Étape 1 : le contexte vient du socle, pas de votre mémoire ; toute l'équipe part de la même base. |
> | « Nous supposons… nous ne savons pas… » | Étape 2 : écrites, vos hypothèses se discutent au lieu d'être confirmées. |
> | « Avant d'agir, liste… » | Étape 3 : ses hypothèses deviennent visibles ; c'est là qu'on attrape l'erreur qu'elle ne signale pas (ci-dessus, la tâche piège). |
> | « Ne propose rien avant nos réponses. » | La porte fermée à l'action trop tôt : sans elle, rien ne l'empêche de répondre tout de suite. |
>
> Sans cerveau, cette demande est tout ce que l'IA sait de vous : chaque mot compte, et bien l'écrire est crucial. Avec un socle et des règles, trois de ses cinq parties n'ont plus à être dites : « lis d'abord index.md » est une règle, « liste ce que tu supposes avant d'agir » en est une autre, « ne propose rien avant nos réponses » est le mode plan ([[fiche-4#Le mode plan|fiche 4]]). Il vous reste le but et vos hypothèses du jour, que le socle ne peut pas deviner ; le reste, l'IA le reconstruit avec vos règles et votre contexte, et une demande écrite vite tient. C'est le socle qui se soigne, plus que la demande. Écrivez tout de même la vôtre une fois avec ces cinq parties, pour voir ce que vos règles lui épargneront ; ou retravaillez-la avec votre IA : « Voici ma demande. Que te manque-t-il pour bien la faire ? » Une demande comprise se répare ; une demande collée, non.

**La méfiance paie.** À Stanford (47 participants, surtout des étudiants), ceux qui avaient un assistant de code ont écrit un code moins sûr sur 4 tâches sur 5, en le croyant plus souvent sûr ; ceux qui se méfiaient de l'IA et retravaillaient leurs demandes écrivaient un code plus sûr (corrélation) [\[2\]](source-02).

**L'IA amplifie ce qui existe déjà** : pour l'enquête DORA de Google Cloud (près de 5 000 professionnels du logiciel), elle grossit les forces des organisations performantes, et les dysfonctionnements des autres [\[3\]](source-03).

**Meilleur ami ou pire ennemi.** Nourrie de notes justes, de décisions écrites et de règles claires, l'IA démultiplie votre travail ; nourrie d'hypothèses jamais vérifiées, elle démultiplie vos erreurs, avec assurance et dans un style impeccable. La peur vous pousse vers le premier cas ; la [[fiche-4|fiche 4]] dit comment.

## Le plus grand danger, vous

Jusqu'ici, la peur visait l'IA ; la plus utile vise ce que vous pourriez perdre en travaillant avec elle. Je me suis entretenu avec un ingénieur DevOps qui se sert de l'IA exactement comme le proposent ces fiches, et je l'ai questionné sur sa pratique :

> [!quote] Ce que m'a dit un ingénieur DevOps
> Je distingue la tactique et la stratégie, comme la bataille et la guerre. Je délègue à l'IA 99 % de la tactique, mais seulement quand la stratégie est bien posée : c'est là que moi, humain, j'ai le plus d'impact. J'ai totalement délégué la tactique pour rester concentré sur la stratégie. Je ne veux pas perdre mon contrôle, ni commencer à ne plus comprendre certaines parties de mon travail. Je contrôle, je me fais challenger par l'IA, et je valide.
>
> De mon expérience professionnelle, le plus gros danger est la facilité avec laquelle on peut tomber, avec l'IA, dans la régression intellectuelle et dans celle de nos compétences. C'est le piège d'aujourd'hui pour tous les utilisateurs, et surtout pour les ingénieurs. Si on régresse, on perd la connaissance qui nous aidait justement à concevoir une stratégie robuste. La technologie, elle, continue d'évoluer, et l'écart se creuse. C'est pour ça qu'une veille technologique est indispensable : suivre l'avancée de l'IA, pour rester à jour et continuer de gagner en compétences. Sinon, on finit par déléguer la stratégie à l'IA, par dépit : alors tout le système perd le contact avec l'humain à l'origine de la solution, et il peut prendre des chemins ambigus, sans notre contrôle.
>
> — <Prénom>, ingénieur DevOps

**Tactique et stratégie.** La tactique est l'exécution : écrire le code, poser une configuration, ranger une note. La stratégie relie les tactiques : le but, les choix qui engagent, les hypothèses sur lesquelles tout repose. La ligne entre les deux bouge d'un projet à l'autre ; elle se trace en mode plan ([[fiche-4#Le mode plan|fiche 4]]).

**La régression n'est pas nouvelle.** Lisanne Bainbridge l'écrivait en 1983 de l'automatisation des usines et des cockpits : les gestes se perdent quand on ne s'en sert pas, un savoir se retrouve d'autant mieux qu'on s'en sert souvent, et qui surveille longtemps une machine peut redevenir débutant. Or c'est quand la machine flanche qu'on lui rend la main : il faudrait alors être plus compétent, pas moins [\[7\]](source-07). Pour vous, ce sera le bug que l'IA ne sait pas corriger, ou la question « pourquoi avez-vous fait ça ? ». La dernière crainte de l'ingénieur, la stratégie déléguée par dépit, est une hypothèse ([[fiche-4#Nourrir le cerveau|fiche 4]]) que personne n'a mesurée jusqu'au bout : mieux vaut ne pas attendre qu'elle soit vérifiée.

**Deux formes du même danger.**
- **Ingénieur**, vous risquez de perdre ce que vous savez : le cas que décrit Bainbridge.
- **En apprentissage**, de ne jamais l'acquérir. Dans une étude d'Anthropic, 52 développeurs, surtout juniors, découvraient une bibliothèque Python : avec l'IA, 50 % au quiz final, contre 67 % à la main, sans gain de temps significatif ; mais ceux qui s'en servaient pour comprendre (questions de principe, explications avec le code) ont eu de 65 à 86 % (corrélation) [\[8\]](source-08). Ce qui semble coûter, ce n'est pas l'IA, c'est de sauter la compréhension. L'étude n'est pas encore relue par des pairs, ses groupes sont petits et le quiz suivait juste la tâche ; mais c'est votre situation, puisque vous apprenez.

**Comprendre, pas savoir écrire.** Le but n'est pas de savoir écrire chaque ligne à la main, mais de comprendre ce qui est mis en place : pourquoi de l'asynchrone ici, par exemple (le détail par type de contenu : [[fiche-4#Le questionnaire|fiche 4]]). Les parades : tracer la ligne en mode plan, le questionnaire (fiche 4), le point sur ce qui a changé ([[fiche-7#Ce qui a changé|fiche 7]]), la veille ([[fiche-8#La veille|fiche 8]]).

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- [\[1\]](source-01) **Quand l'IA aide, et quand elle trompe sans prévenir.** 758 consultants, avec et sans GPT-4. [Dell'Acqua et al., Harvard et BCG, *Organization Science*, 11/03/26](https://doi.org/10.1287/orsc.2025.21838)
- [\[2\]](source-02) **Se méfier de l'IA rend le code plus sûr.** Des participants, surtout des étudiants, avec et sans assistant de code. [Perry et al., Stanford, ACM CCS, 26/11/23](https://arxiv.org/abs/2211.03622)
- [\[3\]](source-03) **L'IA amplifie ce qui existe déjà.** Près de 5 000 professionnels du logiciel interrogés. [DORA, Google Cloud, 23/09/25](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)
- [\[6\]](source-06) **L'IA tend à vous donner raison.** Cinq assistants d'IA de 2023 testés : ils adaptaient souvent leurs réponses à ce que l'utilisateur semblait croire, même quand il se trompait. [Sharma et al., Anthropic, ICLR 2024, 20/10/23](https://arxiv.org/abs/2310.13548)
- [\[7\]](source-07) **Les compétences s'usent quand la machine fait le travail.** Un essai classique sur l'automatisation des usines et des cockpits. [Bainbridge, « Ironies of Automation », *Automatica*, 1983](https://doi.org/10.1016/0005-1098(83)90046-8)
- [\[8\]](source-08) **Apprendre avec l'IA sans chercher à comprendre, c'est moins apprendre.** 52 développeurs qui découvraient une bibliothèque Python ; pas encore relue par des pairs. [Shen et Tamkin, Anthropic, 29/01/26](https://www.anthropic.com/research/AI-assistance-coding-skills), et [l'article](https://arxiv.org/abs/2601.20245)

↑ [[index|L'essentiel]] · ← [[fiche-2|2. Le cerveau, vu dans Obsidian]] · [[fiche-4|4. Nourrir, puis réfléchir]] →

Olivier & Mentordinator
