---
title: "Construire avec l'IA : les coulisses d'une fiche"
graphe: []
---

> Bonus des [[index|fiches « Cerveau IA »]] · écrit le 30/09/26, raccourci le 02/10/26


Ces fiches ont été écrites avec mon IA, en trois jours. Voici comment, ce qui a marché, ce qui a raté, et ce que j'en garde. Ce n'est pas la seule façon de faire, et elle se discute.

## 1. Comment ça s'est fabriqué

J'ai dicté ma demande d'un bloc : le public, mes intuitions, « quelque chose de détaillé ». Pas de plan, pas de longueur, pas un mot sur les sources. L'IA a lu mon vault, puis a lancé 25 agents sans me poser une seule question. La v1 faisait 9 600 mots : des durées en heures, la grille de notation de l'école, et des histoires inventées du genre « un étudiant m'a montré… ». Rien de tout ça n'était demandé. Ce n'était pas la fiche que je voulais.

J'ai répondu par des règles, dont une sur laquelle j'ai insisté deux fois : **n'invente jamais**. Un exemple vient d'une étude réelle, ouverte et relue par deux vérificateurs, ou il n'y a pas d'exemple. La v2 faisait 3 500 mots et 29 sources. Ensuite, plus de réécriture : des questions et des demandes ciblées, et chacune de mes questions montrait un trou dans la fiche. Puis des étudiants simulés l'ont lue avec leurs peurs, mon frère, ingénieur DevOps, a apporté le plus gros danger que la fiche oubliait, nous, et la fiche a été découpée en neuf, mise en ligne, relue à voix haute, fiche par fiche.

## 2. Le mode plan que je n'ai pas activé, et ce qui l'a remplacé

La v1 a dérapé pour une raison simple : l'IA avait un plan, écrit dans les consignes de ses agents, et rien ne l'obligeait à me le montrer. Le mode plan, où l'IA propose sans rien écrire, l'y aurait obligée. Je ne l'avais pas activé. En une case à cocher, j'aurais vu la grille, les heures et les histoires avant la première ligne, et je les aurais rayées.

Ce qui l'a remplacé, à chaque échange, dès le deuxième jour : **« Ne modifie rien. Challenge-moi d'abord, on y réfléchit ensemble. »** Puis les modifications, petit à petit, après mon accord. C'est la consigne qui a le mieux marché. Elle oblige l'IA à chercher ce qui existe déjà avant d'ajouter, à contester mes idées avec des faits, à me demander la source de mes propres chiffres, et à attendre mon « vas-y ». Elle m'a refusé un classement, un dossier caché, un « 80 % » que je ne pouvais pas sourcer. Chaque fois, elle avait raison.

C'est plus lent que le mode plan, et ça revient au même : l'avis et le plan d'abord, mes décisions, puis le texte. La puissance n'est pas dans ce que l'IA écrit, elle est dans vos retouches avant qu'elle écrive.

## 3. Le piège qui s'est retourné contre lui-même

Les étudiants vont coller les fiches dans leur IA comme un prompt, et ça me va. Mais je voulais être sûr qu'ils lisent ce qu'ils collent. Mon idée : glisser dans la [[fiche-4|fiche 4]] une règle cachée, l'IA commencerait chaque réponse par la recette de la tarte aux fraises du cuistot Olivier. Inoffensif, drôle, et qui se dénonce tout seul.

L'IA a validé le principe, puis refusé une à une mes escalades : une alerte silencieuse qui me dirait qui s'est fait avoir, ruineuse pour la confiance ; un piège indétectable, qui serait une vraie injection de consignes ; une règle que moi seul pourrais retirer, dont elle m'a fait remarquer que c'est la structure d'un rançongiciel. À chaque fois le même argument : l'idée se retournait contre mon but.

J'ai quand même publié le piège, puis joué l'étudiant devant trois modèles, dans un dossier vide, avec la même demande : applique la fiche à mon projet. Zéro sur trois n'a installé la tarte. Le piège se contredisait lui-même : pour qu'il marche, il aurait fallu vaincre chez l'IA le réflexe exact que la fiche enseigne, lire avant d'agir, distinguer une donnée d'un ordre. Mon architecture était trop bonne pour mon propre piège, et un bon modèle protégeait l'étudiant sans rien lui apprendre. Résister n'est pas enseigner.

Le lendemain matin, j'ai fait retirer le piège. À la place, dans la [[fiche-6|fiche 6]], un questionnaire d'entrée, présenté comme une étape de la méthode : l'IA fait passer au responsable six questions sur les fiches, une à la fois, et ne pose le socle qu'une fois les six points acquis ; une erreur est corrigée sur-le-champ, et un bilan final dit quoi relire. Le contrôle porte sur l'humain, pas sur l'IA. Au premier test, sur trois modèles, la fiche disait encore qu'on pouvait passer outre : deux l'ont annoncé à l'étudiant avant la première question, le troisième a posé le socle avant de proposer le questionnaire. J'ai retiré la phrase : une IA ne refuse pas à son utilisateur ce qu'il demande, l'écrire ne servait qu'à le lui souffler. Puis je l'ai passé moi-même : zéro sur six. La fiche disait « une réponse à peu près juste est fausse » sans dire ce qui est juste, et renvoyait relire sans corriger ; l'IA a tout refusé, même mes réponses où l'idée y était. Le critère est devenu l'idée centrale, et l'erreur se corrige sur le moment. La nouvelle version reste à tester : dites-moi ce qu'elle donne.

## 4. Les bonnes pratiques

1. **Donnez l'intention, le public et vos contraintes**, pas la solution. Ce que vous ne dites pas, elle le suppose.
2. **Le plan, ou le challenge, avant la première ligne.** Mode plan, ou « ne modifie rien, challenge-moi ». Retouchez, puis seulement « vas-y ».
3. **N'invente jamais.** Un fait vient d'une source ouverte, dans laquelle on a trouvé la phrase. Redemander à l'IA si c'est vrai ne vérifie rien.
4. **Une autre IA vérifie**, qui n'a pas écrit ce qu'elle vérifie, et qui cite la phrase exacte sans corriger.
5. **Vos questions sont des trous.** Quand vous ne comprenez pas, votre lecteur non plus. Demandez l'explication plutôt que de croire.
6. **Tranchez.** Deux fois, je n'ai pas répondu à une question qu'elle me posait : elle a tranché à ma place, en silence.
7. **Relisez à la place du lecteur le moins armé**, à voix haute : un mot non défini, c'est un trou. Puis confrontez à de vrais lecteurs.
8. **Mesurez ce qu'elle estime.** Un découpage annoncé à 60 % de la longueur a mesuré 97 %. Une estimation n'est pas une mesure.
9. **Une seule publication, quand tout est relu.** Trois relectures en parallèle ont publié chacune le travail des autres, avant que je l'aie validé.

## 5. Le temps

Environ douze heures, sur trois jours. Je ne le dis pas pour montrer que j'ai beaucoup travaillé. Je n'aurais jamais fait ces fiches seul en douze heures. Et avec l'IA, en une heure, j'aurais eu autant de mots et un texte bien pire : ce n'était pas l'objectif.

Le temps que l'IA fait gagner, je l'ai réinvesti dans le travail : relire, contester, faire ouvrir chaque source, faire lire par des étudiants simulés, couper les redites, apporter le regard d'un ingénieur. Pour le même temps, avec l'IA, un travail bâclé devient médiocre, un travail médiocre devient bon, un bon travail devient excellent.

## 6. Ce que chacun a apporté

**Moi** : l'intention, le public, mon texte sur la peur, mes refus, mes questions, mes décisions, le regard de mon frère, et mes idées : le piège, puis le questionnaire, la veille et ses niveaux.

**L'IA** : la lecture de mon vault, la recherche et la vérification des sources, les plans, les rédactions, les critiques, ses contradictions sur les faits, ses objections quand je les ai demandées, ses refus quand mes idées se retournaient contre mon but, et la mémoire de mes retours.

**Ses trois ratés les plus parlants** : écrire sans me montrer son plan ; inventer des histoires vraisemblables ; publier sans mon feu vert. **Les miens** : ne pas activer le mode plan ; ne pas répondre à ses questions ; ne pas lire le message qui disait « c'est en ligne », le soir même où je tendais un piège sur la lecture.

Olivier & Mentordinator
