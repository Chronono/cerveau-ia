---
title: "Construire avec l'IA : les coulisses d'une fiche"
---

> Compagnon de la fiche [[index|« Donner un cerveau à l'IA de votre équipe »]] · écrite le 30/09/26 · mise à jour le 01/10/26 avec la v5, puis avec son découpage en [[index|neuf fiches et un résumé]] et sa mise en ligne

Cette fiche raconte comment l'autre a été construite, entre moi et mon IA. Je ne recopie pas mes demandes : je montre les allers-retours, ce que l'IA a fait, ce qu'elle a raté, ce que j'ai raté aussi, et comment tout a été vérifié. C'est ce que j'espère être une bonne pratique quand on construit quelque chose avec l'IA. Ce n'est pas la seule, et elle se discute.

**En cinq lignes.**
1. Je suis parti d'une intention riche, sans mode plan. L'IA a lu ce qui existait, puis a écrit sans me soumettre son plan ni me poser une seule question : la v1 est partie à côté.
2. L'IA a fait vérifier son travail par d'autres agents, et m'a dit ce qui ne l'était pas.
3. J'ai répondu par des règles et par mes réactions de lecteur ; elle les a gardées en mémoire.
4. Chacune de mes questions et de mes demandes a montré un trou dans la fiche.
5. On a relu la fiche à la place de ceux qui vont la lire, et j'ai dit ce qui comptait le plus. Ensuite, pour couper les redites, ajouter l'avis d'un ingénieur ou découper la fiche, l'IA m'a soumis son plan avant d'écrire. Celle-ci a été vérifiée contre la conversation réelle.

## 1. La demande : une intention, pas un plan

J'ai dicté ma demande d'un bloc. Je commençais par « est-ce qu'on peut y réfléchir ensemble » : je voulais anticiper tous les problèmes, puis proposer une fiche aux équipes. Le fond : mes équipes ont du mal à monter un environnement IA ; j'imagine un vault Obsidian dans un dépôt GitHub, chacun pousse sur main et gère ses conflits, sans dépendre d'un modèle d'IA en particulier ; plus tard, un serveur dont l'agent enverrait au groupe WhatsApp un sondage pour trancher un conflit. Je voulais une fiche qui vulgarise : les avantages, les dangers, l'importance du contexte et des hypothèses avant d'agir, l'IA meilleur ami ou pire ennemi, des exemples concrets, une construction pas à pas, du temps investi au début puis gagné. Pour des étudiants de quatrième année, en projet de trois mois.

J'ai donné l'intention, le public et mes intuitions. Je demandais « quelque chose de détaillé », sans plan, sans longueur précise, sans parler de sources.

L'IA a d'abord lu ce que mon vault savait déjà : mes notes sur les équipes, mes notes sur la première soutenance, mon propre montage, un serveur qui lit mon vault et en tire mes fiches de réunion. Puis elle a lancé le travail, **sans me poser une seule question**. Je n'avais pas activé le mode plan, où l'IA propose son plan sans rien écrire : rien ne l'obligeait à me le montrer. Elle a écrit ses hypothèses dans la consigne de ses agents : relier la fiche à la grille de notation de l'école, ouvrir chaque section par une histoire tirée des projets de mes équipes, un calendrier en heures, 5 000 à 7 000 mots. Je n'avais demandé ni la grille, ni des histoires de mes équipes, ni des heures, et l'IA ne m'a pas demandé si c'était ce que je voulais.

> [!tip] La pratique
> Donnez l'intention, le contexte et vos contraintes : le public, la longueur, ce que vous ne voulez pas. Laissez l'IA lire ce qui existe. Puis **passez en mode plan** : demandez-lui le plan de ce qu'elle va faire, ici les fiches, leurs parties et leurs exemples, et faites vos passes dessus avant qu'elle écrive une ligne. Je ne l'ai pas fait, et c'aurait été une très bonne idée : la grille de notation, les histoires de mes équipes et les heures étaient déjà écrites dans les consignes de ses agents. En mode plan, je les aurais vues, et rayées, avant la première ligne. Tout ce que vous ne dites pas, elle le supposera ; le mode plan vous le montre à temps. L'autre fiche y consacre une partie (§ 4).

## 2. La v1 : beaucoup de travail, mais à côté

Mon outil était réglé pour répartir tout gros travail entre plusieurs agents, des instances d'IA lancées chacune avec un rôle. Pour la v1, il y en a eu 25 :
- des lecteurs, dont un qui vérifiait les faits sur le web ;
- quatre plans sous quatre angles différents, départagés par trois agents juges ;
- deux rédactions complètes, dont la meilleure a servi de base ;
- cinq critiques : un novice, un réfutateur technique, un mentor, un spécialiste de la sécurité, un chasseur d'oublis ;
- une révision, puis deux tours de vérification et de correction.

La vérification a trouvé des erreurs bloquantes avant que je voie quoi que ce soit. Par exemple, le contrôle de secrets proposé aurait refusé un fichier du plugin Git d'Obsidian, qui contient du texte ressemblant à des clés : l'équipe aurait appris à contourner le contrôle dès le premier soir.

En me livrant la v1, l'IA m'a aussi contredit, faits à l'appui. L'API officielle de WhatsApp n'envoie pas de sondage : Telegram et Discord, oui. Et un serveur qui surveille main ne voit jamais de conflit, puisque le conflit naît sur le poste dont le push est refusé. Les deux corrections sont restées dans la fiche. Elle m'a laissé une note à part : ses choix, les problèmes qu'elle anticipait, et huit questions à trancher. Je n'y ai pas répondu : j'ai répondu par mes remarques (§ 3).

Le résultat faisait environ 9 600 mots : treize sections, cinq annexes, un calendrier en heures, les critères de notation de l'école, des exemples tirés des projets de mes équipes, et des histoires racontées à ma place, du genre « un étudiant m'a montré… ». Tout avait été relu et contre-vérifié, et ce qui ne l'était pas restait marqué « à vérifier ». Mais les histoires n'étaient pas des faits : aucune vérification ne les visait, et elles étaient inventées. Surtout, ce n'était pas la fiche que je voulais.

> [!tip] La pratique
> Faites vérifier le travail de l'IA par une autre IA, qui n'a pas écrit ce qu'elle vérifie. Pas besoin de 25 agents : une seconde conversation suffit. Par exemple : « Voici un texte que tu n'as pas écrit. Cherche ce qui est faux, ce qui n'a pas de source, ce qui manque pour [votre lecteur]. Cite la phrase exacte. Ne corrige rien. » *Que tu n'as pas écrit* : elle ne défend pas son propre travail. *Cite la phrase exacte* : vous pouvez contrôler. *Ne corrige rien* : vous gardez la main. Mais une vérification ne rattrape pas une demande mal comprise : c'est à vous de lire.

## 3. Mon retour : des règles et des réactions

Juste avant ce retour, j'ai changé de modèle d'IA : l'écart entre la v1 et la v2 ne vient donc pas seulement de mes remarques. Le dossier et la conversation, eux, sont restés : c'est l'intérêt de ne dépendre d'aucun modèle.

J'ai lu la v1, puis j'ai répondu en neuf remarques. Celle sur laquelle j'ai insisté deux fois : **n'invente jamais**. Un exemple vient d'une étude réelle et prouve exactement ce qu'on veut prouver ; sinon, pas d'exemple. Les autres :
- ne pas mêler l'IA et les soutenances ;
- une fiche générale, qu'une équipe de startup pourrait suivre, sans les projets de mes équipes : un dossier de notes qui cartographie le cerveau de l'IA, pas un chatbot avec une page de mémoire ;
- aucune durée : les étapes se classent par criticité, car le temps dépend du projet ;
- plus simple : arriver à quelque chose de fonctionnel, puis l'améliorer ;
- mon propre texte sur la peur, à reprendre ;
- « meilleur ami, pire ennemi » : les exemples n'étaient pas compris ;
- un désaccord : la v1 disait que l'IA ne commite pas. Pour moi, c'est elle qui fait le pull et le commit, sous des règles écrites, parce que **l'humain oublie, pas l'IA** ;
- trop d'exemples.

Certaines remarques portaient leur raison : « ça dépend du projet », « l'humain oublie, pas l'IA ». D'autres étaient des réactions de lecteur : « on ne comprend pas tes exemples », « j'ai peur que ce soit trop complexe ». Les deux servent : la règle évite de refaire l'erreur, la réaction dit où le lecteur décroche.

J'ai aussi écrit : « je t'ai demandé de prendre des exemples concrets sur des études sur internet ». Ma première demande n'en disait rien : je le croyais dit. Ce que vous avez en tête n'est pas dans ce que vous avez dit.

L'IA a d'abord enregistré ces remarques dans sa mémoire : « n'invente jamais » comme règle pour tous mes textes, les autres comme cadre de cette fiche. Je travaille seul avec mon IA, donc sa mémoire me sert de socle ; dans une équipe, ces règles iraient dans AGENTS.md, par le responsable des règles, comme le dit l'autre fiche. Puis elle a relancé le travail, et m'a montré au même moment le plan qu'elle imposait à ses agents. Elle ne me l'a pas soumis, et je ne le lui avais pas demandé : là encore, le mode plan m'aurait laissé le retoucher avant qu'elle relance tout. Mais elle n'a pas retouché la v1 : elle l'a reconstruite.

> [!tip] La pratique
> Quand vous savez pourquoi, dites-le : une correction répare une réponse, une règle avec sa raison évite la même erreur la fois suivante. C'est la boucle du § 8 de l'autre fiche : on corrige le socle, pas seulement la réponse. Et relisez votre demande de départ : ce qui vous paraît évident n'y est peut-être pas.

## 4. La v2 : des sources ouvertes deux fois

Deuxième travail entre agents, avec une règle nouvelle. L'IA a choisi quelles études chercher ; une étude ou un incident n'entrait dans la fiche que si deux vérificateurs indépendants l'avaient ouvert et avaient confirmé ce qu'on lui fait dire, un troisième tranchant en cas de désaccord. Les faits sur les outils, eux, ont été vérifiés une fois, dans leur documentation officielle. Puis deux rédactions, une courte et une complète, fusionnées, et des critiques, dont une chargée de vérifier la fidélité à mes remarques.

La vérification a changé des chiffres. L'étude de Harvard et du BCG existe en deux versions : le document de travail annonçait environ 40 % de qualité en plus, la version publiée et relue par des pairs dit « plus de 30 % ». La fiche cite la version publiée. Onze sources ont été écartées au tri, souvent justes mais redondantes, et une autre à la relecture finale : elle ne prouvait pas le point sous lequel elle était placée.

L'IA a jugé ses propres agents, et parfois tranché seule. Un correcteur avait supprimé « meilleur ami ou pire ennemi » ; elle l'a remis, avec sa raison : je n'avais pas compris les exemples, je n'avais pas rejeté l'idée. Mais c'était une question qu'elle me posait dans sa note : elle l'a retirée de la note au lieu de me la laisser. Elle a aussi repéré que cette note contredisait une de mes propres règles, et l'a corrigée.

La v2 faisait environ 3 500 mots, avec 29 sources. En me la livrant, l'IA a commencé par une réserve : aucun des réglages proposés n'avait été exécuté pour de vrai. Au 30/09/26, ils ne l'ont toujours pas été : testez-les avec les critères du niveau 1 de l'autre fiche.

> [!tip] La pratique
> Vérifier une source, c'est l'ouvrir et y trouver la phrase. Redemander à l'IA si c'est vrai ne vérifie rien : pour ouvrir une source, il faut une IA qui accède au web, ou vous. Et une bonne IA dit ce qu'elle n'a pas vérifié, au lieu de le taire.

## 5. Les allers-retours : mes questions et mes demandes

Ensuite, je n'ai plus demandé de réécriture. J'ai lu, posé des questions et demandé des changements ciblés, dans cet ordre :

| Ma question ou ma demande | Ce que l'IA a fait | Ce qui a changé dans la fiche |
|---|---|---|
| Claude lit CLAUDE.md, les autres outils AGENTS.md : n'est-ce pas un problème pour l'agnosticité ? | Elle a repris la vérification faite le jour même par un de ses agents dans les documentations de huit outils, et relu elle-même celle de Claude Code. Sa réponse : le fichier de règles se règle presque ; la vraie dépendance à un outil est dans ses skills, ses réglages et sa mémoire. Elle a aussi trouvé deux défauts de la v2, chez Aider et chez Codex | Rien d'abord : une réponse dans la conversation. Puis, à ma demande, un encadré qui explique le piège et la parade. Les deux défauts ne sont pas encore corrigés |
| C'est quoi, les chiffres entre crochets ? | Elle a expliqué : des renvois aux sources. Elle m'a proposé deux façons de le dire au lecteur, et en recommandait une. Je n'ai pas choisi | Elle a appliqué l'autre : une phrase d'explication en tête des sources |
| Il y a trop de sources : range-les par exemples, outils et bonnes pratiques, et garde l'essentiel | Elle a suivi mes familles, et séparé les exemples en deux : les études et les dangers | 29 entrées regroupées en 17, en quatre familles : deux études retirées, les autres réunies par thème |
| Les prompts : je veux qu'ils les lisent, pas qu'ils les collent | Elle a découpé chaque exemple partie par partie, et gardé la règle en mémoire | Des exemples annotés, suivis d'une invitation à écrire le sien. L'IA ne pose plus que la partie technique : AGENTS.md et les skills, l'équipe les écrit |
| L'IA commite puis fait le pull : ce ne serait pas l'inverse ? | Elle a commencé par « tu as raison sur le principe : le pull passe d'abord », puis expliqué les deux cas où le commit passe avant, et les deux autres voies avec leur coût | Un encadré, parce que les équipes se poseront la même question |

Les deux dernières sont arrivées pendant qu'elle rangeait les sources ; elle a livré les trois changements ensemble, comme la v3. Les explications ont ajouté environ 1 100 mots, et elle m'a proposé d'en sortir une partie dans une seconde fiche. Je ne l'ai pas encore décidé.

Deux choses dans ce tableau. Sur le commit, mon doute était à moitié juste ; j'ai écrit « c'est peut-être mieux comme tu l'as dit », puis « explique-moi » : l'explication est maintenant dans la fiche. Et sur les crochets, comme sur « meilleur ami » au § 4, je n'ai pas tranché : l'IA a tranché à ma place.

> [!tip] La pratique
> Quand vous ne comprenez pas, votre lecteur non plus : chacune de vos questions montre un trou dans le travail. Ne croyez pas l'IA sur parole, demandez-lui d'expliquer. Et tranchez : l'IA propose, vous décidez, mais quand vous ne répondez pas, elle décide à votre place.

## 6. La relecture : à la place du lecteur

Avant de vous la donner, j'ai demandé à l'IA de relire la fiche à la place d'un étudiant. Un étudiant qui ne voit pas ce qu'Obsidian change, qui ne sait pas comment son équipe va s'organiser, qui a peur de l'IA et de mal faire. Je voulais savoir ce qu'il ressent, s'il gagne en confiance, s'il comprend qu'il faut du temps pour nourrir son IA, comment formuler ses questions et ses hypothèses, comment réfléchir avec elle, comment aller plus loin, et quand il en a le droit.

L'IA a fait lire la fiche par cinq étudiants simulés, chacun avec une inquiétude :
- celui qui ne voit pas ce qu'Obsidian change par rapport à ChatGPT ou à un document partagé ;
- le chef de projet d'une équipe aux niveaux et aux outils différents ;
- celui qui a peur de l'IA, de casser le dépôt, de laisser fuiter un secret ;
- le pressé, qui suit les étapes à la lettre, comme une procédure ;
- celui qui veut réfléchir avec l'IA, pas lui faire faire le travail.

Chacun a lu la fiche section par section, noté ce qu'il ressentait et sa confiance, et recopié mot pour mot chaque phrase où il bloquait. Puis un vérificateur sceptique a repris chaque rapport pour le réfuter : la phrase citée existe-t-elle ? la fiche ne répond-elle pas ailleurs ?

| Ce que les étudiants simulés ont ressenti | Après vérification |
|---|---|
| La méthode et son exemple annoté : le passage le plus utile, pour les cinq | Confirmé |
| Le tableau des niveaux dit quand avancer, et ça rassure | Confirmé, avec des réserves de détail |
| Le premier jour est flou : qui fait quoi, dans quel ordre, avec quelles commandes | Confirmé |
| Ils ne voient pas ce qu'Obsidian apporte de plus qu'un dossier ou un document partagé | Confirmé |
| Rien ne dit comment l'équipe s'organise autour du socle | Confirmé |
| Ils comprennent que tout dépend de ce qu'on écrit, pas qu'il faut y consacrer du temps : aucune séance prévue, aucun exemple de note de mémoire, aucune place pour l'état de l'art | Confirmé |

Les vérificateurs ont surtout corrigé des « seul » et des « nulle part » trop rapides, et relevé ce que les lecteurs n'avaient pas vu. Par exemple, plusieurs ont cru que l'IA attendait leur accord avant de pousser ; d'après les réglages proposés, elle pousse sans demander. Ce que j'ai fait de ce rapport est au § 7.

Cette fiche-ci a suivi le même chemin. Deux vérificateurs l'ont confrontée à la conversation réelle, et un étudiant simulé l'a lue. Sur 63 affirmations, ils en ont trouvé quatre fausses et une vingtaine d'imprécises, corrigées avant que vous la lisiez. J'avais écrit, par exemple, que tout était vérifié dans la v1, et qu'une de mes décisions avait orienté le choix de la messagerie : c'était faux.

Un étudiant simulé n'est pas un étudiant. Cette relecture prépare la vraie, elle ne la remplace pas : la vraie, ce sont vos retours.

> [!tip] La pratique
> Relisez à la place de celui qui va lire, avec ses peurs et ses questions, pas avec les vôtres. Faites vérifier aussi ce que vous racontez, pas seulement ce que vous affirmez. Puis confrontez à de vrais lecteurs.

## 7. Mon tri : insister là où tout se joue

J'ai lu le rapport des étudiants simulés, et j'ai trié. Formuler ses questions et ses hypothèses : la fiche le faisait bien. Savoir quand avancer : plutôt bien fait aussi. Mais deux étapes comptent plus que tout le reste : nourrir l'IA avec ce qu'on sait, et réfléchir avec elle pour aller plus loin. C'est l'étape cruciale : mal faite, la suite du projet va dans le mur. J'ai demandé une repasse qui insiste, avec de bonnes pratiques, et qui invite à en faire presque trop. Et trois ajouts : ce qu'Obsidian change vraiment, en disant qu'il n'est pas obligatoire et pourquoi je le préconise ; l'avis de l'IA elle-même ; une petite feuille de route pour la mise en place.

Pendant qu'elle travaillait, j'ai ajouté deux demandes. D'abord, tenir cette fiche-ci à jour au fil de mes retours. Ensuite, le mode plan : ces coulisses présentaient « exiger ses questions » comme l'étape manquée, alors que je n'avais simplement pas activé ce mode. Je lui ai demandé de le dire, et d'ajouter à l'autre fiche une partie sur le mode plan : il fait comprendre que la puissance, ce sont les retouches de l'utilisateur. La v4 a d'ailleurs été écrite, elle aussi, sans mode plan : l'IA avait son plan, elle ne me l'a pas soumis avant d'écrire.

L'IA a fait vérifier chaque fait nouveau par deux agents par sujet : un chercheur, puis un vérificateur qui rouvrait chaque page. Ce que ça a changé :
- sur Google Drive, le chercheur avait attribué une phrase à la mauvaise page d'aide ; le vérificateur a trouvé la bonne ;
- la documentation de git déconseille de synchroniser un dépôt par un cloud : l'avis de l'IA, dans l'autre fiche, le dit maintenant ;
- le mode plan de Claude Code s'ouvre avec Maj+Tab dans le terminal, mais pas dans l'application de bureau, celle que j'utilise, où c'est un sélecteur à côté du bouton d'envoi : la fiche donne les deux.

Puis la relecture, comme pour la v3. Trois étudiants simulés : un qui veut réfléchir avec l'IA, un qui ne voit pas ce qu'Obsidian change face au Drive de son équipe, un pressé qui suit la feuille de route à la lettre. Chacun a été contre-vérifié, et deux agents de plus ont vérifié les faits et la cohérence. Pour les trois, le fond, du § 2 au § 4, était la partie la plus solide. La feuille de route, elle, ne marchait pas suivie à la lettre : le contrôle de secrets n'était installé que chez un membre, et la répétition de conflit, dans l'ordre écrit, ne produisait aucun conflit, puisque le rituel fait récupérer le travail de l'autre avant de modifier. La phrase qui rendait Obsidian facultatif, écrite d'après mes mots, mélangeait deux choses : remplacer Obsidian, l'éditeur, et remplacer GitHub, le partage. Le vérificateur de faits a trouvé une image chiffrée sans source, contraire à ma règle, et une étude à qui la fiche faisait dire un peu trop. Et sous Windows, où Claude Code peut passer par PowerShell, les interdits de la fiche risquaient de ne rien bloquer. Tout a été corrigé avant que vous la lisiez.

> [!tip] La pratique
> Triez les retours : dites ce qui marche, pour qu'on n'y touche pas, et où il faut insister. L'IA ne sait pas ce qui compte le plus pour vous ; « c'est l'étape cruciale » la guide mieux qu'une liste de corrections.

## 8. Les répétitions : le plan avant les coupes

J'ai relu la v4, et je lui ai demandé : « Tu trouves pas qu'il y a beaucoup de répétitions ? » Cette fois, l'IA n'a pas touché au texte. Trois agents ont fait le relevé, chacun sous un angle : les idées qui reviennent, la partie technique, la phrase. Puis elle a écrit un plan de 36 coupes : pour chacune, la phrase avant, la phrase après, et l'endroit où l'idée reste, sa « maison ». Deux vérificateurs l'ont relu : l'un cherchait ce qu'une coupe faisait perdre, l'autre ce qu'elle trahissait de mes demandes. Ils en ont rejeté six, qui retiraient une insistance que j'avais voulue ou la raison d'être d'une puce, et en ont corrigé neuf.

Avant de couper, elle m'a montré le résultat. Oui, il y avait des redites, mais regroupées : environ 4 % du texte. L'impression venait surtout de la partie technique, qui racontait la même mise en place sous quatre angles : l'ordre, la criticité, le mécanisme, les niveaux. Elle m'a dit ce qu'elle garderait exprès : mon texte sur la peur, les « Faites-en trop », les rappels placés au moment d'agir. Et que la longueur venait du contenu, pas des redites : pour vraiment raccourcir, il faudrait couper la fiche en deux. Sur ses quatre options, j'ai choisi de couper les redites et de corriger trois défauts trouvés en chemin : deux paragraphes du mode plan qui se contredisaient, une étude à qui la fiche faisait dire plus qu'elle ne dit, une annonce devenue fausse. Couper la fiche en deux reste une question ouverte.

Une dernière relecture, par trois agents et leurs vérificateurs, a contrôlé les phrases, les renvois, les sources et mes demandes. Elle a trouvé trois accrocs, corrigés : une phrase devenue ambiguë, un test qui ne disait plus ce qu'il vérifiait, et mon paragraphe sur Obsidian, où la fusion laissait croire qu'un Drive remplace aussi Obsidian.

> [!tip] La pratique
> Quand un texte vous paraît répétitif, demandez le relevé et le plan des coupes avant les coupes. Une redite voulue, une insistance ou un rappel au moment d'agir, ressemble à une redite inutile : exigez pour chaque coupe l'endroit où l'idée reste, et gardez le dernier mot.

## 9. Un regard extérieur : l'avis avant l'écriture

J'ai parlé avec mon frère, ingénieur DevOps, qui se sert de l'IA exactement comme je la présente dans la fiche. Il distingue la tactique et la stratégie, et pour lui, le plus grand danger est la régression de nos compétences ; je voulais le mettre dans « Ayez peur ». Cette fois, avant que l'IA touche à la fiche, je lui ai demandé son avis, puis de me challenger.

Son avis tenait en trois idées. C'était un angle mort : la fiche avait peur de l'IA, jamais de nous, alors que toutes ses parades supposent un humain capable de juger. La fiche suivait déjà la distinction de mon frère sans la nommer : le rituel tenu par l'IA, c'est la tactique ; nourrir, réfléchir et décider, c'est la stratégie. Et les preuves existaient : avant de me répondre, elle avait fait ouvrir huit sources par un agent. Elle en a écarté une elle-même, l'étude la plus citée sur le sujet : pas relue par des pairs, et sa méthode est contestée. Elle a aussi refusé le « 99 % » de mon frère comme donnée : c'est son estimation, il reste dans sa bouche, dans un encadré qu'il relira.

Puis huit points pour me challenger. Le premier : mon frère peut déléguer la tactique parce qu'il l'a apprise à la main, avant l'IA ; mes étudiants, non. Pour eux, le risque n'est pas de régresser, c'est de ne jamais apprendre. J'étais d'accord, et j'ai demandé de distinguer les deux publics : les ingénieurs déjà sur le terrain, les étudiants qui apprennent. J'ai corrigé un autre point : pour du code, il ne s'agit pas de savoir refaire chaque ligne, mais de comprendre les principes. L'IA a reconnu que l'étude qu'elle citait allait dans mon sens : ceux qui se servaient de l'IA pour comprendre apprenaient aussi bien que les autres, voire mieux.

Deux points me visaient. Deux fois, aux § 4 et 5, je n'ai pas tranché, et l'IA a tranché à ma place. Ce n'était pas par dépit, comme dans la crainte de mon frère, mais par silence : c'est la même pente, en petit, et je suis prêt à la montrer. Elle m'a aussi demandé si je comprenais encore tout mon propre système. Pour l'instant, oui : chaque nouvelle technologie, comme Tailscale, je l'étudie avant de l'employer.

Mes réponses ont ajouté cinq idées : un questionnaire avant chaque push ; une explication que l'IA corrige avant de la laisser passer, comme la description d'une pull request ; la veille technologique ; le mode plan pour tracer la ligne entre tactique et stratégie ; et mon projet Bureau comme exemple de rapport. Cette fois, l'IA m'a soumis son plan avant d'écrire : où irait chaque idée, et deux choix à me laisser. Au questionnaire, elle a ajouté deux garde-fous : des questions sur les principes, jamais sur un nom de fichier ; et « une réponse à peu près juste est fausse », puisqu'elle tend à donner raison. J'ai retouché le plan : le questionnaire porte aussi sur les documents rédigés par l'IA, les règles et le cahier des charges, avec des questions pièges et un peu de rédaction ; la règle est un exemple que chaque équipe adapte ; une seule source de plus que les deux que j'avais gardées, l'effet de test. Sur l'un des deux choix, le moment du questionnaire, je n'ai pas répondu. L'IA n'a pas choisi parmi ses trois options : elle les a toutes mises dans la fiche, au choix de chaque équipe, et me l'a signalé. J'ai alors tranché : avant chaque commit, sauf pour un changement qui se dit en une phrase.

Deux vérificateurs ont ensuite relu le travail : l'un les faits et la cohérence de l'autre fiche, l'autre ce récit contre notre conversation. Ils ont trouvé une étude à qui la fiche faisait dire une cause au lieu d'une corrélation, des « débutants » qui étaient des développeurs juniors, une expérience mal décrite, une règle qui contredisait le rituel, et un point « ce qui a changé » qui, dans le cas le plus courant, n'aurait rien montré. Ici, un temps de travail surestimé, et des phrases qui me prêtaient des mots que je n'ai pas dits. Tout a été corrigé avant que vous lisiez ; ce qui demandait mon avis m'a été laissé.

Une dernière retouche, en relisant : malgré le passage du § 2 qui le disait, la fiche parlait encore d'Obsidian comme si c'était la référence. Or un dépôt de fichiers Markdown suffit. J'ai fait ajouter un encadré dès le début : j'appelle ce jeu de fichiers « Obsidian » par habitude, ce n'est absolument pas une obligation, et l'outil apporte surtout une lecture confortable du Markdown et le graphe des liens. Puis j'ai demandé si les rétroliens n'étaient pas, eux non plus, propres à Obsidian. Non : le lien est écrit dans le fichier, et une simple recherche retrouve les notes qui en citent une autre. La fiche le disait à moitié ; elle donne maintenant la commande, et le lien standard pour ceux qui veulent des liens cliquables sur GitHub, après vérification dans sa documentation. Enfin, l'encadré de mon frère se lisait comme un témoignage trouvé sur internet ; la fiche dit maintenant que je me suis entretenu avec lui et que je l'ai questionné moi-même. J'ai aussi fait ajouter à son témoignage l'importance de la veille technologique ; il le relira comme le reste.

> [!tip] La pratique
> Confrontez votre travail à quelqu'un du métier, et apportez son regard à l'IA. Puis demandez-lui son avis et ses objections avant qu'elle écrive : « Donne-moi ton avis, puis challenge-moi. » Répondez point par point, en disant où elle a tort. Ne cachez pas les objections qui vous visent. Et quand vous ne tranchez pas, vérifiez qu'elle vous le dit, au lieu de trancher à votre place.

## 10. Le découpage : le plan d'abord, la mesure ensuite

Le même jour, j'ai demandé à l'IA de résumer la v5 sans perdre d'information, d'en répartir les chapitres en plusieurs fiches, et d'écrire une fiche qui résume le tout de manière très compacte : 10 à 20 % de la taille totale, avec un lien vers chaque chapitre pour passer facilement d'une fiche à l'autre.

Je n'ai pas demandé de plan : la règle qu'elle garde en mémoire depuis le 30/09, soumettre son plan avant toute grosse production, a suffi. L'IA a lu la fiche en entier et ces coulisses, puis parcouru ma note de réflexion, qui proposait déjà de couper la fiche entre le § 5 et le § 6. Elle m'a écrit avoir lu aussi le rapport des étudiants simulés : elle ne l'avait pas ouvert. Elle s'en est aperçue en relisant notre conversation pour écrire ce paragraphe. Puis, sans rien écrire, elle m'a soumis son plan : une fiche par chapitre, une pour les sources, et le résumé, chacune avec sa longueur avant et après ; mon texte sur la peur et l'encadré de mon frère, mot pour mot ; les exemples, entiers ; et la preuve que rien ne serait perdu : un relevé de tous les points de la v5, que vérifierait un agent qui n'aurait rien écrit, et un script pour chaque lien. Elle a aussi relevé un double sens dans ma demande : « le contenu total », c'est la v5 ou les fiches résumées ? Avec environ 1 200 mots, le résumé tiendrait dans les deux lectures. Elle finissait par quatre points à retoucher.

J'ai pris une de ses propositions et refusé l'autre : le § 9, très court, rejoint le § 8 ; le § 4, 30 % du tout, qu'elle proposait de couper en trois, reste une seule fiche, parce que tout y est lié. J'ai voulu les sources au pied de chaque fiche, et toutes dans le résumé ; elle en a tiré qu'une fiche des sources ne servait plus : neuf fiches et un résumé. Ses deux derniers points, le nom des fichiers et une ligne à ajouter en tête de la v5, je ne les ai pas compris, et je l'ai dit. Elle les a réexpliqués plus simplement, puis a commencé sans attendre ma réponse : un préfixe et un numéro rangent les fiches dans l'ordre et évitent qu'une autre note du vault porte le même nom ; et la v5, elle n'y touche pas, sauf si je le demande. J'ai aussi demandé si ces coulisses étaient à jour. Non : rien n'était encore écrit, ni les fiches ni ce paragraphe, et elle me l'a dit.

Pendant qu'elle écrivait, un autre agent relevait la v5, sans voir les fiches : 924 points, un par fait, chiffre, étude, règle, commande, étape ou mise en garde. Le plan prévoyait ce relevé avant l'écriture ; il a commencé en même temps, et n'a été prêt qu'après les fiches. Puis quatre agents qui n'avaient pas écrit les fiches, dont celui du relevé, ont cherché chaque point dans les fiches. Aucun ne manquait, sauf la date où la fiche avait été écrite, le 30/09. Huit étaient déformés dans les neuf fiches : un sujet changé, une nuance perdue, un renvoi oublié, une image devenue une affirmation. Dans L'essentiel, une dizaine de phrases étaient à revoir, dont une grave : elle gardait les chiffres d'une étude et perdait ses réserves. Les deux passages à garder mot pour mot l'étaient. Tout a été corrigé. Deux scripts ont complété. L'un a suivi chaque lien jusqu'au titre visé. L'autre a cherché dans les fiches chaque bloc de code, chaque chiffre et chaque citation de la v5, et les a tous trouvés, sauf deux : une phrase d'exemple adaptée exprès, « Lis cette fiche » devenu « Lis ces deux fiches », puisque ce qu'elle désignait tient maintenant dans deux fiches ; et un bloc de code, une fausse alerte du script, puisqu'un agent l'a trouvé identique, caractère pour caractère. Enfin, en lisant les fiches dans Obsidian, j'ai vu des cases à cocher à la place de numéros de sources : en début de ligne, « - [5] » est pour Obsidian une case. Le script les avait écrits ainsi ; c'est corrigé.

Restait la longueur, mesurée dès les fiches écrites. Le plan annonçait des fiches à un peu plus de 60 % de la v5. Le script a mesuré 99 % ; l'IA a resserré les quatre premières fiches : 97 %. Son estimation était fausse, faite sans mesurer ; elle me l'a dit, mais seulement dans son bilan, plus d'une heure après l'avoir mesuré. Son explication : les redites étaient déjà coupées (§ 8), et la prose ne raccourcit pas sans perte. Mais elle avait lu le § 8 avant d'estimer, et son plan comptait déjà les exemples et les réglages comme incompressibles : c'est la prose qu'elle voyait fondre de moitié, et elle n'a pas fondu. Les neuf fiches sont donc la v5 découpée, pas résumée ; le vrai résumé, c'est L'essentiel : environ 1 100 mots, 11 % de la v5, plus toutes les sources. Elle a corrigé les en-têtes, de « version résumée » en « version découpée », et m'a proposé des pistes pour aller plus court. Je n'ai pas encore choisi.

> [!tip] La pratique
> Une règle écrite une fois sert les fois suivantes : ici, je n'ai pas eu à demander le plan. Quand vous ne comprenez pas une proposition, dites-le, sinon elle s'appliquera telle quelle. Faites mesurer ce que l'IA estime, une longueur, un temps, un gain : une estimation n'est pas une mesure. Un résumé « sans perte » se prouve point par point, par une IA qui ne l'a pas écrit. Et ce qu'elle dit avoir lu se vérifie aussi.

## 11. La mise en ligne : un lien plutôt qu'un fichier

Restait à faire lire les fiches. J'ai demandé comment les envoyer aux étudiants pour qu'ils les lisent confortablement : devaient-ils passer par un lecteur de Markdown ? Existait-il un outil en ligne gratuit, sans inscription ?

L'IA a d'abord expliqué l'obstacle. Mes fiches sont écrites dans le Markdown propre à Obsidian, avec ses liens, ses encadrés repliables et ses commentaires cachés, et les lecteurs en ligne ne le comprennent pas : les liens s'afficheraient en texte brut, et le commentaire de brouillon dans l'encadré de mon frère deviendrait visible. Puis elle a proposé quatre façons, chacune avec sa contrepartie : un petit site gratuit, mais public ; un seul fichier HTML, à renvoyer à chaque correction ; le dossier des fiches, à ouvrir dans Obsidian, qu'il faut installer avant de lire ; des PDF, sans liens d'une fiche à l'autre. Elle recommandait le site, si un site public ne me gênait pas, et listait ce qu'il fallait régler avant tout envoi : l'encadré de mon frère, encore brouillon ; le lien vers la v5, qui ferait doublon ; la vérification point par point, qui tournait encore. J'ai choisi le site : public, ça me va.

Elle avait annoncé une mise en place avec moi ; elle l'a faite seule, en un quart d'heure, avec mon compte GitHub, déjà connecté sur mon ordinateur. Un script copie les fiches de mon vault vers le site et le met à jour en deux minutes : je corrige toujours dans Obsidian, jamais sur le site. Avant de publier, elle a retiré ce qui n'avait pas à sortir, le commentaire de brouillon et le lien vers la v5 ; et, le dépôt étant public, elle a signé les commits de l'adresse que GitHub fournit pour ne pas montrer mon mail. Puis elle a ouvert chaque page en ligne et suivi chaque lien entre les fiches jusqu'au titre visé. Avant les étudiants, j'envoie le site à mon frère, pour qu'il complète son témoignage et me dise ce qu'il pense des fiches.

> [!tip] La pratique
> Demandez les options et leurs contreparties avant de choisir, et ce qu'il faut régler avant d'envoyer. Ce qui sort en public se relit : un commentaire caché, un lien vers une note privée, une adresse mail. Un agent agit avec vos accès, ici mon compte GitHub : dites-lui ce qu'il a le droit de publier. Et vérifiez le résultat là où le lecteur le verra.

## 12. Ce que j'en retiens

| Version | Longueur | Ce qui a changé |
|---|---|---|
| v1 | environ 9 600 mots | Tout ce que j'avais demandé, plus des durées, une grille de notation et des histoires inventées |
| v2 | environ 3 500 mots | Générale, par criticité, sources vérifiées deux fois, mon texte sur la peur |
| v3 | environ 4 950 mots | Le piège AGENTS.md, 17 sources en quatre familles, des exemples annotés à réécrire soi-même, l'ordre du pull et du commit expliqué |
| v4 | environ 9 000 mots | L'étape cruciale (nourrir, puis réfléchir), Obsidian avant et après, l'avis de l'IA, le mode plan, une feuille de route |
| v4, après les coupes | environ 8 450 mots | Trente redites coupées, une maison par idée, trois défauts corrigés |
| v5 | environ 11 000 mots | Le plus grand danger : vous (tactique et stratégie, l'avis d'un ingénieur, à compléter par lui), le questionnaire avant le push, le point sur ce qui a changé, la veille, trois sources de plus |
| Découpage | neuf fiches, 97 % de la v5 ; L'essentiel, environ 1 100 mots plus les sources | Un chapitre par fiche, des liens pour passer de l'une à l'autre, les sources au pied de chaque fiche et toutes dans L'essentiel |

**Le temps.** D'après l'horodatage de nos conversations, les deux fiches m'ont pris environ quatre heures, sur deux jours : un peu moins de trois heures le 30/09, environ une heure et demie le 01/10. Le découpage en a pris plus d'une heure et demie de plus, le même jour, surtout en travail de l'IA : j'y ai écrit trois messages, dont un sur la façon d'envoyer les fiches. La mise en ligne a suivi, un quart d'heure après mon choix. Je ne le dis pas pour montrer que j'ai beaucoup travaillé. L'IA peut se voir comme un outil qui fait gagner du temps ; mais ce temps peut être réinvesti dans le travail, pour le rendre encore meilleur. Ici, il est allé à relire, contester, faire vérifier les sources, faire lire par des étudiants simulés, couper les redites, apporter l'avis d'un ingénieur. Pour le même temps, avec l'IA, un travail humain bâclé devient médiocre, un travail médiocre devient bon, un bon travail devient excellent.

**Ce que j'ai apporté** : l'intention, le public, mon texte sur la peur, mes refus, mes questions, mes décisions, le tri de ce qui compte le plus, le regard d'un ingénieur, et des idées à moi : le questionnaire, la veille.

**Ce que l'IA a apporté** : la lecture de mon vault, la recherche et la vérification des sources, les plans, les rédactions, les critiques, les explications, ses contradictions sur les faits, ses objections quand je les ai demandées, et la mémoire de mes retours.

**Ce qu'elle a mal fait** : écrire sans me soumettre son plan ni me poser ses questions ; inventer des histoires vraisemblables ; mêler les soutenances, coller trop près de mes équipes, ajouter des durées et trop d'exemples ; trancher seule deux questions qu'elle m'avait posées ; laisser deux défauts signalés sans les corriger ; redire les mêmes idées d'une section à l'autre ; annoncer une longueur sans l'avoir mesurée ; déformer, en découpant, huit points des fiches et une dizaine de phrases du résumé ; dire avoir lu un document qu'elle n'avait pas ouvert.

**Ce que j'aurais pu mieux faire** : activer le mode plan et retoucher son plan avant qu'elle écrive ; répondre à ses questions, puisqu'elle m'en a laissé à chaque livraison ; dire ce que j'avais en tête, les études, au lieu de le croire dit.

La pratique, en treize points :
1. **Donnez l'intention, le contexte et vos contraintes**, pas la solution (§ 1).
2. **Passez en mode plan, et retouchez son plan** avant qu'elle écrive : la puissance est dans vos retouches (§ 1, § 3, § 7, § 8 et § 10).
3. **Laissez-la lire ce qui existe** avant d'écrire (§ 1).
4. **Faites vérifier par une autre IA**, et chaque chiffre dans sa source (§ 2 et § 4).
5. **Lisez tout, et répondez** : des règles avec leur raison, et vos réactions de lecteur (§ 3).
6. **Vos questions sont des trous dans le travail** : posez-les, et demandez l'explication plutôt que de croire (§ 5).
7. **Tranchez** : sinon, l'IA tranchera pour vous (§ 4 et § 5).
8. **Relisez à la place du lecteur**, puis confrontez à de vrais lecteurs (§ 6).
9. **Dites ce qui compte le plus**, pas seulement ce qui ne va pas (§ 7).
10. **Avant de couper, demandez le relevé et le plan des coupes**, avec l'endroit où chaque idée reste (§ 8).
11. **Avant qu'elle écrive, demandez son avis et ses objections**, et confrontez votre travail au regard de quelqu'un du métier (§ 9).
12. **Faites mesurer ce que l'IA estime**, et prouvez un résumé point par point, par une IA qui ne l'a pas écrit (§ 10).
13. **Avant de publier, relisez ce qui sort**, et vérifiez le résultat là où le lecteur le verra (§ 11).

**Et pour votre projet.** À plusieurs, les retours ne vont pas dans la mémoire d'un outil : les règles vont dans AGENTS.md, par le responsable des règles, et le reste dans une note du socle. Pour du code, vérifier, c'est un test qui tourne ou une datasheet ouverte ; le lecteur, c'est l'utilisateur.

C'est la méthode de l'autre fiche : le contexte, vos hypothèses, les siennes, vos réponses, la décision, et alors seulement l'action. Elle n'a pas été suivie tout du long : la v1 a sauté l'étape des questions : je ne les ai pas demandées, et sans mode plan, je n'ai pas vu son plan à temps. C'est là qu'elle a dérapé. Pour les répétitions, pour l'avis de mon frère, puis pour le découpage, elle l'a été : l'avis et le plan d'abord, mes décisions, puis le texte. Pour l'avis de mon frère, une décision oubliée est venue après, et le texte l'a suivie. Pour le découpage, l'IA a commencé sans attendre ma réponse sur deux points que je n'avais pas compris : ils se sont appliqués par défaut. Le raconter fait aussi partie de la pratique.

Olivier & Mentordinator
