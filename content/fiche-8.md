---
title: "8. Améliorer, niveau par niveau"
graphe: ["source-04", "source-17", "source-20", "source-21"]
---

↑ [[index|L'essentiel]] · ← [[fiche-7|7. Le rituel, tenu par l'IA]] · [[fiche-9|9. Dangers et parades]] →

Les niveaux suivent la criticité de la [[fiche-6|fiche 6]] ; le niveau 3 fait de la méthode une habitude.

| Niveau | Ce qu'on ajoute | Passez au suivant quand… |
|---|---|---|
| 1. Fonctionnel | Le critique technique ([[fiche-5\|fiche 5]], étapes 1 à 5) | les signes de réussite des étapes 1 à 5 sont vus chez chacun, et chaque IA fait pull, commit et push sans rappel |
| 2. Cerveau nourri | La mémoire : la séance de la [[fiche-4#Nourrir le cerveau\|fiche 4]] | le test de la fiche 4 passe |
| 3. Réflexion écrite | La méthode et les réflexes ([[fiche-3#La méthode\|fiche 3]], [[fiche-4#Réfléchir avec l'IA\|fiche 4]]), à chaque question qui compte ; le questionnaire, si vous l'avez adopté | chaque décision a sa note, avec ses options et un lien vers les hypothèses qui la fondent |
| 4. Skills | Toute consigne répétée devient un skill | plus personne ne réexplique la même procédure |
| 5. Automatismes | Hook (déjà posé à l'étape 3 pour Claude Code), plugin Git | chez chacun, l'ouverture d'une session fait le pull sans qu'on le demande |
| 6. Le serveur | Plus bas, « Plus tard, un serveur qui veille » | — |

## La boucle

Jugez sur ces critères, pas au ressenti : 16 développeurs expérimentés croyaient que l'IA leur avait fait gagner 20 % de temps, alors qu'ils en avaient mis 19 % de plus (outils de début 2025) [\[4\]](source-04) ; les mesures de fin 2025 penchent vers une accélération, sans effet établi [\[4\]](source-04). Quand l'IA se trompe, ne corrigez pas seulement sa réponse : corrigez le socle. Une note manquait ? Écrivez-la. Une règle était floue ? Reformulez-la. Une procédure a été réexpliquée ? Elle devient un skill. Une erreur qui revient, c'est une règle qui manque [\[17\]](source-17) ; vérifiez ensuite que le comportement change [\[17\]](source-17).

**Gardez AGENTS.md court**, puisqu'un fichier long est moins bien suivi [\[17\]](source-17) ; d'où une règle simple : une qui entre en fait sortir une. Anthropic conseille moins de 200 lignes, et de tailler sans pitié : si la retirer ne fait faire aucune erreur à l'IA, elle sort [\[17\]](source-17). Le détail vit dans les notes et les skills ; archivez les notes périmées.

**La veille** ([[fiche-7#La veille|fiche 7]]) nourrit la boucle : chaque jour, les nouveautés des technologies du projet, classées de la régression à la révolution ; un niveau −1, 3 ou 4 devient une étude, puis une note ou une règle du socle.

## Plus tard, un serveur qui veille

Quand le socle tient, un serveur peut garder une copie du dépôt toujours à jour, où un agent relit chaque commit. Un conflit n'apparaît jamais sur GitHub : le push est refusé, et les deux versions se rencontrent sur le poste de celui qui fait le pull [\[20\]](source-20). L'IA de ce membre envoie donc sa version sur une branche à part ; le serveur voit les deux et envoie au groupe de l'équipe un sondage : le conflit, les résolutions possibles, sa proposition. Chacun vote sous son nom. L'agent propose, l'équipe tranche. Il repère aussi les contradictions que git fusionne sans alerte, sur des lignes différentes.

Messagerie : un bot Telegram peut envoyer un sondage non anonyme dans un groupe, Discord aussi, pas l'API officielle de WhatsApp [\[21\]](source-21).

**À explorer, sans obligation.** Le serveur peut aussi faire la veille seul, chaque matin, et vous l'envoyer par mail ou dans le groupe de l'équipe ; tenir un journal des changements du projet ; rappeler qui a commité quoi. C'est possible, pas une étape à franchir. Telegram s'y prête bien : un bot se crée en quelques minutes [\[21\]](source-21), le serveur lui fait envoyer des messages à l'heure voulue, et on peut lui écrire en retour. Le mien m'envoie mes rappels et ma newsletter du matin, et je lui en programme un nouveau d'un simple `/rappel`.

**Le point du matin, en vrai.** Mon propre serveur fait déjà, pour moi seul, le rapport de la [[fiche-7#Ce qui a changé|fiche 7]] : c'est mon projet Bureau. Chaque matin, un script relève les commits et les fichiers modifiés de chaque projet. Pour chaque projet qui a bougé, une IA en écrit une fiche où chaque affirmation pointe vers sa preuve ; une dernière IA lit ces fiches, avec mes décisions en attente, et en tire un résumé de 250 mots au plus. Ce que ça ajoute au point de la fiche 7 : un seul résumé pour toute l'équipe, preuves à l'appui, même pour qui n'a pas ouvert de session ce jour-là.

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- [\[4\]](source-04) **Le ressenti ne prouve rien.** Des développeurs se croyaient plus rapides avec l'IA, et l'étaient moins. [METR, étude du 12/07/25](https://arxiv.org/abs/2507.09089), puis [son suivi du 24/02/26](https://metr.org/blog/2026-02-24-uplift-update/)
- [\[17\]](source-17) **Règles, mémoire, hooks et interdits dans Claude Code.** [Mémoire et AGENTS.md](https://code.claude.com/docs/en/memory), [bonnes pratiques](https://code.claude.com/docs/en/best-practices), [hooks](https://code.claude.com/docs/en/hooks-guide), [permissions](https://code.claude.com/docs/en/permissions), [mode plan](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode), [PowerShell](https://code.claude.com/docs/en/permissions), [les coûts d'une longue session](https://code.claude.com/docs/en/costs), [la fenêtre de contexte et le résumé](https://code.claude.com/docs/en/context-window)
- [\[20\]](source-20) **Git, GitHub et le contrôle de secrets.** [Conflits et fusion](https://git-scm.com/docs/git-merge), [push refusé](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors), [fins de ligne](https://git-scm.com/docs/gitattributes), [pre-commit](https://pre-commit.com), [gitleaks](https://github.com/gitleaks/gitleaks), [ne pas synchroniser un dépôt par un cloud](https://git-scm.com/docs/gitfaq), [chercher dans les fichiers](https://git-scm.com/docs/git-grep), [les liens dans un fichier Markdown sur GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [les liens d'un wiki GitHub](https://docs.github.com/en/communities/documenting-your-project-with-wikis/editing-wiki-content)
- [\[21\]](source-21) **Les sondages par bot.** [Telegram](https://core.telegram.org/bots/api), [Discord](https://docs.discord.com/developers/resources/poll), [WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages)
↑ [[index|L'essentiel]] · ← [[fiche-7|7. Le rituel, tenu par l'IA]] · [[fiche-9|9. Dangers et parades]] →

Olivier & Mentordinator
