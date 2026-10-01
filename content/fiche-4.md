---
title: "4. L'étape cruciale : nourrir, puis réfléchir"
graphe: ["source-01", "source-03", "source-06", "source-09", "source-17", "source-18"]
---

↑ [[index|L'essentiel]] · ← [[fiche-3|3. Ayez peur]] · [[fiche-5|5. La feuille de route]] →

Si vous ne lisez qu'une fiche, lisez celle-ci. Deux étapes décident de tout le reste : **nourrir** l'IA de ce que vous savez, puis **réfléchir** avec elle avant d'aller plus loin. Mal faites, elles envoient le projet dans le mur, et l'IA vous y conduit avec assurance ([[fiche-3|fiche 3]]). Ici, en faire trop est la bonne dose.

## Nourrir le cerveau

L'IA ne sait de votre projet que ce qui est écrit dans le socle ; ce qui reste dans vos têtes, vos cours ou vos échanges avec le client n'existe pas pour elle, et elle le remplace par du vraisemblable. L'enquête DORA ([[fiche-3|fiche 3]]) le constate : quand l'IA accède aux données internes, les gains déclarés sont plus forts (données déclaratives) [\[3\]](source-03). Elle ne peut pas savoir à votre place : elle met en forme, vous apportez le fond.

**La séance « Verser ce que vous savez ».** Avant la première vraie question, toute l'équipe, ensemble, autour d'un agent ouvert dans le dépôt, sur un écran que tous voient. Chacun verse ce qu'il sait, en vrac : il parle, dicte, colle ses notes de cours ou ses lectures. L'IA range chaque morceau dans la bonne note, marque le supposé, et montre chaque note avant de l'écrire : rien n'entre dans le socle sans votre relecture.

| Ce que vous savez | Où ça va | Ce que la note doit dire |
|---|---|---|
| Le but, le client et son cahier des charges, les contraintes, où vous en êtes | `projet.md` ; le cahier des charges lui-même dans `sources/` | ce qu'on veut, ce qui est imposé, l'état |
| Chaque article, documentation, cours, produit existant : l'état de l'art | `sources/`, une note par source | ce qu'elle dit, ce qu'elle prouve pour vous, son lien, vos doutes |
| Ce que vous croyez sans l'avoir vérifié, et ce que vous ignorez | `hypotheses/`, une note par hypothèse | l'exemple ci-dessous |
| Ce qui est déjà tranché | `decisions/` | la question, les options, le choix, qui, pourquoi, un lien vers chaque hypothèse dont il dépend ; un choix fait avant le socle s'écrit aussi, puis se fait contester (plus bas) |
| Ce qui a été essayé et n'a pas marché | l'hypothèse, marquée réfutée | pourquoi elle est tombée, pour que personne ne la repropose comme neuve |
| Les mots du métier | `glossaire.md` | un mot, une définition : celle de l'équipe |

**Le solide et le supposé.** Solide : ce que dit une source que vous avez ouverte et lue, une mesure, une exigence écrite du client. Tout le reste est supposé, et le dit : un supposé glissé dans `projet.md` ou dans une décision devient une note d'`hypotheses/`, citée par un lien. Une supposition écrite comme un fait, c'est exactement ce que l'IA amplifiera. Dans le doute, c'est supposé.

**Jamais dans le socle** : les secrets, les données personnelles, ce qu'un client vous a confié sous confidentialité, sans son accord. Avec un modèle en ligne, tout ce que l'IA lit part chez son fournisseur.

**Une hypothèse, l'exemple** : la suite de la demande de la [[fiche-3#La méthode|fiche 3]], à lire, pas à coller.

```markdown
---
statut: à vérifier
---
# Notre trafic restera faible

**Ce qu'on suppose** : moins de <seuil> visites par jour.
**Pourquoi on le croit** : <votre raison, avec sa source s'il y en a une>.
**Comment le vérifier** : <une mesure, une source, une question au client>.
**Si c'est faux** : <ce qui ne tient plus>.

Liée à : [[projet]]
```

**Comment elle est construite.**
- **Le titre est l'hypothèse elle-même**, en une phrase : elle se lit dans une liste ou un lien sans ouvrir la note.
- **Le statut, en tête** : à vérifier, vérifiée, réfutée, ou risque accepté (la note dit qui l'accepte, et pourquoi). L'IA voit d'emblée si elle peut s'y appuyer.
- **« Pourquoi on le croit »** : une croyance sans raison écrite ne se discute pas. Un doute sans avis ? Écrivez votre meilleure supposition ; le statut dit le reste.
- **« Comment le vérifier »** : si vous ne savez pas l'écrire, l'hypothèse est un risque ; dites-le dans la note.
- **« Si c'est faux »** : ce qui ne tient plus. Chaque décision fondée sur l'hypothèse la cite par un lien : le jour où elle tombe, ses rétroliens montrent toutes ces décisions, même oubliées ([[fiche-2|fiche 2]]).
- **« Liée à »** : sans lien, la note est un point isolé du graphe. Le sommaire doit aussi mener à elle, directement ou par une note qui la cite : l'IA part d'`index.md` et suit les liens dans le sens où ils sont écrits.

**Faites-vous interroger.** Ce que vous savez sans y penser, vous ne l'écrirez pas seul ; inversez les rôles : « Interroge-moi sur notre projet, une question à la fois, jusqu'à trouver ce que je sais et que le socle ne dit pas encore. Range chaque réponse dans la bonne note, marque ce qui est supposé, et montre-moi avant d'écrire. » Une question à la fois, sinon elle en pose une série et vous n'en traitez qu'une partie ; montrer avant d'écrire, pour que rien n'entre sans relecture. Chaque membre y passe, seul : vous ne savez pas les mêmes choses. Anthropic conseille aussi de se faire interroger par l'IA avant un gros travail [\[17\]](source-17).

**Le test.** Une session neuve, sans rien lui expliquer : « Résume notre projet. Qu'est-ce qui est solide, qu'est-ce qui est supposé, que manque-t-il ? » Chaque correction que vous feriez à voix haute est une note qui manque : écrivez-la dans le socle, pas dans la conversation, puis recommencez avec une autre session neuve. Tant que vous corrigez quelque chose d'important, le cerveau n'est pas nourri.

**Faites-en trop.** Une source, une hypothèse, un mot de glossaire de plus : pour l'IA, c'est presque gratuit. Le socle peut être grand, son contexte reste petit : elle ne charge que ce que la tâche demande, en partant du sommaire ([[fiche-1|fiche 1]]). Le coût, c'est votre relecture, et c'est elle qui rend le socle juste. Le trop va dans la mémoire, jamais dans AGENTS.md ([[fiche-8#La boucle|fiche 8]]) ni dans le sommaire, qui restent courts : le sommaire mène aux notes, il ne les contient pas. Le danger n'est pas le trop, c'est le faux et l'isolé : une note fausse, l'IA la répète ; une note sans lien, elle la trouve mal. Et ça ne s'arrête pas à la séance : chaque lecture, chaque réunion, chaque échange avec le client dépose au socle ce qu'il a appris.

## Réfléchir avec l'IA

Bien nourrie, l'IA peut encore vous tromper, et elle tend à vous donner raison [\[6\]](source-06) : réfléchir avec elle, c'est ne jamais s'arrêter à sa première réponse. Six réflexes ; les phrases sont des exemples à lire, à dire avec vos mots, sur votre sujet.

| Réflexe | Par exemple | Pourquoi |
|---|---|---|
| **Des options, pas une réponse** | « Donne trois options, ce que chacune suppose, et ce qui la ferait échouer. » | Une réponse seule ne se juge pas ; trois se comparent, et leurs suppositions apparaissent. |
| **La faire contester** | « Voici notre choix. Quelle est la meilleure raison d'y renoncer ? » | Les assistants étudiés cédaient souvent à l'avis de l'utilisateur, même faux [\[6\]](source-06) : demandez-leur le contraire. |
| **Confronter aux sources** | « Pour chaque affirmation, quelle note de sources/ la soutient ? Marque celles qui n'en ont pas. » | Avec l'IA, même les réponses fausses étaient mieux rédigées [\[1\]](source-01) : le style ne prouve rien. |
| **Chercher ce qui réfuterait** | « Quelle observation prouverait que cette hypothèse est fausse ? Comment l'obtenir ? » | Un test qui ne peut pas échouer n'apprend rien. |
| **Changer de regard** | « Relis ce plan comme notre client, puis comme la personne qui devra le maintenir. Qu'est-ce qui coince ? » | Chaque regard voit d'autres failles, et vous ne les avez pas tous. |
| **Écrire ce qui sort** | « Range ce que nous venons d'établir : ce qui est devenu solide, ce qui reste supposé, ce qui est décidé. » | La conversation s'oublie ; le socle reste, pour l'équipe et pour la prochaine session ([[fiche-1\|fiche 1]]). |

**Faites-en trop, là aussi** : une option, une contestation, une source à confronter de plus. Une question de trop ne coûte presque rien ; une hypothèse jamais testée peut coûter le projet.

**Le cycle** : une hypothèse, un test, une décision, une action. Quand une hypothèse tombe, on ne continue pas comme si de rien n'était : ses rétroliens montrent les décisions à rouvrir.

**Quand avancer** : quand chaque hypothèse dont dépend la décision est vérifiée, ou son risque accepté par écrit ; quand la décision est écrite, avec ses options ; et quand une session neuve, avec le seul socle, sait expliquer pourquoi. On ne bâtit jamais sur un supposé oublié.

## Le mode plan

La plupart des agents ont un **mode plan**, où l'IA lit, explore et propose un plan sans modifier vos fichiers : Claude Code, Cursor, Codex, Gemini CLI, Antigravity et Copilot dans VS Code en ont un, Aider son mode « ask » [\[17\]](source-17) [\[18\]](source-18). Dans Claude Code, on le choisit dans le sélecteur de mode, à côté du bouton d'envoi de l'application de bureau (Maj+Tab dans le terminal), ou l'on commence un message par `/plan` [\[17\]](source-17) ; dans Codex, `/plan` ou Maj+Tab ; pour les autres, la page de leur mode plan est en [\[18\]](source-18). Ouvrez la session normalement, laissez l'IA faire son rituel ([[fiche-7|fiche 7]]), puis passez en mode plan. Anthropic conseille d'explorer, puis de planifier, puis de coder : une IA qui code tout de suite peut résoudre le mauvais problème [\[17\]](source-17).

**La puissance, ce sont vos retouches.** L'IA propose son plan ; vous le retouchez : « Pas cette étape. » « Tu as oublié la contrainte du client. » « L'étape 3 repose sur une hypothèse fausse. » Dans Claude Code, on refuse le plan en disant ce qui doit changer, et elle continue de planifier [\[17\]](source-17). Deuxième passe, troisième ; alors seulement, vous la laissez agir. Demandez ses hypothèses et ses questions en tête du plan : le mode plan l'empêche d'agir, il ne les fait pas apparaître tout seul.

Son premier plan est vraisemblable et général ; celui qui sort de vos retouches contient ce que vous seuls savez : la puissance n'est pas dans le plan de l'IA, elle est dans vos retouches ; le mode plan vous le montre, passe après passe. C'est la méthode de la [[fiche-3#La méthode|fiche 3]] dans un outil : ses hypothèses, si vous les demandez, apparaissent avant la première action, quand les corriger ne coûte rien. Une retouche qui vient d'un savoir absent du socle est une note qui manque : mettez son écriture en première étape du plan. Sans code aussi, le mode plan sert : son plan est alors le chemin vers la décision, ce qu'il faut vérifier, quelles sources confronter. Pour un changement qui se dit en une phrase, Anthropic conseille de s'en passer [\[17\]](source-17) ; pour tout ce qui compte, prenez-le.

**C'est là que se trace la ligne** entre tactique et stratégie ([[fiche-3#Le plus grand danger, vous|fiche 3]]). Chaque étape du plan est une tactique, que vous validez une à une ; la stratégie les relie : pourquoi ces étapes, dans cet ordre, pour quel but. Passe après passe, vérifiez que vous avez délégué toute la tactique et que l'IA a compris la stratégie : faites-la-lui redire avec ses mots, et si elle se trompe, une retouche de plus. Ce sont les questions que vous vous posez qui tiennent la ligne. Le plus difficile : décider de vous faire contester, quand vous pourriez simplement déléguer. Des deux chemins, le facile et le difficile, le plus difficile est, comme souvent, le meilleur.

Sans mode plan, demandez-le avec vos mots : ses hypothèses et ses questions d'abord, puis un plan étape par étape, sans rien modifier, que vous retoucherez avant qu'elle agisse. Ce que son absence coûte : la fiche [[coulisses|« Les coulisses d'une fiche »]] raconte comment la version complète de ces fiches a été faite, sans mode plan.

## Le questionnaire

Le danger de la [[fiche-3#Le plus grand danger, vous|fiche 3]] se joue à un moment précis : quand ce que l'IA a écrit entre dans le socle, et que vous ne l'avez pas compris. Le questionnaire ferme cette porte. Avant chaque commit, l'IA vous pose trois à cinq questions sur ce qui entre. Tout juste : elle commite ; sinon, elle vous corrige, explique, vérifie que vous avez compris, puis commite. « Faites-vous interroger » (plus haut) fait sortir ce que vous savez ; le questionnaire vérifie que vous avez compris ce qui entre.

**Des questions, pas une relecture** : se tester fait mieux retenir que relire. Dans une expérience de 2006, des étudiants lisaient un texte ; une semaine plus tard, ceux qui l'avaient lu quatre fois cinq minutes d'affilée en retenaient 40 %, ceux qui l'avaient lu cinq minutes puis avaient écrit trois fois de mémoire tout ce qu'ils en retenaient, 61 %. Cinq minutes après la lecture, pourtant, ceux qui avaient relu gagnaient, et ils étaient les plus sûrs de s'en souvenir [\[9\]](source-09) : c'est ce qui trompe. Relire ce que l'IA a écrit rassure ; répondre à ses questions fait retenir.

**Sur quoi l'interroger** : tout ce qui entre, pas seulement le code.

| Ce qui entre | Ce que les questions vérifient |
|---|---|
| Du code | les principes : pourquoi ce choix, quel algorithme, quelle complexité, de l'asynchrone ou non ; jamais une ligne à réciter |
| Un document rédigé par l'IA | ce qu'il dit, et ce qu'il implique pour le projet |
| Une règle ajoutée à l'IA (AGENTS.md, un skill) | ses conséquences : ce qu'elle fera faire, ou empêchera, à chaque IA de l'équipe |
| Un cahier des charges | les points clés du projet, une compréhension générale ; jamais un chiffre quelconque à retenir par cœur |

**Comment le faire bien.**
- **Faites-le écrire par l'IA, avec une ou plusieurs questions pièges**, dont la réponse évidente est fausse : elles séparent celui qui a compris de celui qui a reconnu les mots.
- **Une ou deux questions où l'on rédige**, deux ou trois phrases, pas plus : choisir parmi des réponses se fait en survolant, rédiger demande d'avoir compris. Plus long, le questionnaire devient un devoir, et on finit par le sauter.
- **Une réponse à peu près juste est fausse**, et la règle doit le dire : l'IA tend à vous donner raison [\[6\]](source-06), et accepterait une réponse floue.

**L'autre forme : expliquer.** Vous dites en deux ou trois phrases ce qui change et pourquoi ; l'IA vérifie que vous ne dites pas de bêtises, vous corrige, explique, vérifie que vous avez compris, puis se sert de votre explication pour le message de commit : le commit porte alors votre nom et votre compréhension. Si votre équipe travaille par pull requests (une demande de fusion, relue avant d'entrer dans main), c'est la description de la PR.

Oui, c'est pénible. Mais c'est moins cher que la dette technique d'un travail que personne ne comprend.

**Une règle, l'exemple**, à lire puis à adapter : ce n'est pas une obligation, et une règle conçue pour votre usage vaudra mieux.

```markdown
## Le questionnaire
Quand : avant chaque commit, sauf pour un changement qui se dit en une phrase.
1. Pose-moi 3 à 5 questions sur ce que tu vas commiter : pour du
   code, les principes (pourquoi ce choix, quel algorithme, quelle
   complexité) ; pour un document, ce qu'il implique ; pour une règle, ses
   conséquences ; pour un cahier des charges, les points clés. Jamais un
   chiffre quelconque ni une ligne à réciter.
2. Au moins une question piège, et une où je rédige deux ou trois phrases.
3. Une réponse à peu près juste est fausse. Pour chaque erreur : corrige,
   explique, puis repose la question autrement.
4. Tout juste : commite. Ne saute le questionnaire que si je te le demande.
```

**Comment elle est construite.**
- **« Quand »** : avant chaque commit, donc avant que le travail entre dans l'historique, puis parte chez les autres au push qui suit. Écrivez-le aussi là où la règle agit : dans « Pour chaque modification » d'AGENTS.md ([[fiche-6#AGENTS.md, l'exemple|fiche 6]]), « montre le changement, questionnaire, puis commite » ; sinon deux consignes se contredisent, et l'IA peut suivre l'une au hasard. Il y aura plusieurs questionnaires par session, et un contrôle passé dix fois par heure finit coupé : d'où l'exception pour ce qui se dit en une phrase.
  - *Un autre moment, si vous concevez la vôtre* : une seule fois, avant le push de fin de session. La porte reste gardée, mais le rituel change : un commit seul après chaque modification, une ligne « Quand je dis que j'ai fini : questionnaire, puis `git push` », et, au premier message, pousser ce qui ne l'a pas été. Vos coéquipiers voient votre travail plus tard, et les conflits peuvent grossir.
- **« Ce que tu vas commiter »** : l'IA le voit dans git (`git status`, `git diff`) ; rien n'entre dans l'historique sans être passé par une question.
- **« Jamais un chiffre quelconque ni une ligne à réciter »** : on vérifie la compréhension, pas le par-cœur ; l'ordre de grandeur qui engage le projet, lui, se comprend, et peut faire une bonne question.
- **« Repose la question autrement »** : à la même question, on répond de mémoire ; à une autre, on montre qu'on a compris.
- **« Ne saute le questionnaire que si je te le demande »** : rien ne vous empêche de passer outre, c'est le chemin facile (le mode plan, plus haut) ; mais il faut le demander : ce n'est plus un oubli, c'est un choix.

**Concevez la vôtre.** Une équipe qui écrit surtout du code interrogera sur les principes ; une équipe qui a un client, sur son cahier des charges ; une autre préférera l'explication au questionnaire. Demandez à votre IA : « Voici notre projet et cette règle. Quelles questions nous aideraient vraiment à rester maîtres de ce qui entre dans le socle ? Où cette règle nous gênerait-elle ? » Puis la règle entre dans AGENTS.md comme les autres, par le responsable des règles ([[fiche-6#Critique|fiche 6]]) ; si elle s'allonge, faites-en un skill, appelé par une ligne d'AGENTS.md.

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- [\[1\]](source-01) **Quand l'IA aide, et quand elle trompe sans prévenir.** 758 consultants, avec et sans GPT-4. [Dell'Acqua et al., Harvard et BCG, *Organization Science*, 11/03/26](https://doi.org/10.1287/orsc.2025.21838)
- [\[3\]](source-03) **L'IA amplifie ce qui existe déjà.** Près de 5 000 professionnels du logiciel interrogés. [DORA, Google Cloud, 23/09/25](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)
- [\[6\]](source-06) **L'IA tend à vous donner raison.** Cinq assistants d'IA de 2023 testés : ils adaptaient souvent leurs réponses à ce que l'utilisateur semblait croire, même quand il se trompait. [Sharma et al., Anthropic, ICLR 2024, 20/10/23](https://arxiv.org/abs/2310.13548)
- [\[9\]](source-09) **Se tester fait retenir, mieux que relire.** Des étudiants qui relisaient un texte ou écrivaient de mémoire ce qu'ils en retenaient, testés une semaine plus tard. [Roediger et Karpicke, *Psychological Science*, 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- [\[17\]](source-17) **Règles, mémoire, hooks et interdits dans Claude Code.** [Mémoire et AGENTS.md](https://code.claude.com/docs/en/memory), [bonnes pratiques](https://code.claude.com/docs/en/best-practices), [hooks](https://code.claude.com/docs/en/hooks-guide), [permissions](https://code.claude.com/docs/en/permissions), [mode plan](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode), [PowerShell](https://code.claude.com/docs/en/permissions), [les coûts d'une longue session](https://code.claude.com/docs/en/costs), [la fenêtre de contexte et le résumé](https://code.claude.com/docs/en/context-window)
- [\[18\]](source-18) **Les outils d'IA et leurs prix.** Documentation : [skills de Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://learn.chatgpt.com/docs), [Gemini CLI](https://geminicli.com/docs), [Antigravity](https://antigravity.google/docs), [VS Code](https://code.visualstudio.com/docs), [Copilot](https://docs.github.com/en/copilot), [Cursor](https://cursor.com/docs), [Aider](https://aider.chat/docs). Modes plan : [Cursor](https://cursor.com/docs/agent/plan-mode), [Codex](https://learn.chatgpt.com/guides/best-practices), [Gemini CLI](https://geminicli.com/docs/cli/plan-mode/), [Antigravity](https://antigravity.google/docs/cli/modes/), [Copilot dans VS Code](https://code.visualstudio.com/docs/agents/run/planning), [Aider](https://aider.chat/docs/usage/modes.html). [Projets partagés de ChatGPT](https://help.openai.com/en/articles/10169521). Offres : [Obsidian](https://obsidian.md/blog/free-for-work/), [GitHub](https://docs.github.com/en/get-started/learning-about-github/githubs-products), [Claude](https://claude.com/pricing), [pack étudiant GitHub](https://education.github.com/pack)

↑ [[index|L'essentiel]] · ← [[fiche-3|3. Ayez peur]] · [[fiche-5|5. La feuille de route]] →

Olivier & Mentordinator
