---
title: "9. Dangers et parades"
---

> Donner un cerveau à l'IA de votre équipe · fiche 9 sur 9 · version découpée du 01/10/26, d'après la version complète

↑ [[index|L'essentiel]] · ← [[fiche-8|8. Améliorer, niveau par niveau]]

| Danger | Le fait | Parade |
|---|---|---|
| Invention avec assurance | Des avocats ont cité des décisions de justice inventées par ChatGPT, qui les disait réelles, et les ont défendues une fois alertés : sanctionnés [10] | Tout fait porte sa source, vérifiée dans la source, jamais en redemandant à l'IA ([[fiche-6#AGENTS.md, l'exemple\|AGENTS.md]]) |
| Secrets poussés | Selon GitGuardian (qui vend un détecteur de secrets), les commits publics assistés par Claude Code contenaient un secret deux fois plus souvent que la moyenne, 3,2 % contre 1,5 % (corrélation) [11] | `.gitignore` en premier, contrôle de secrets jamais contourné ([[fiche-6#Critique\|fiche 6]]) |
| Agent qui détruit | Selon son utilisateur, un agent a supprimé des données de production malgré une consigne de ne rien modifier (récupérées ensuite) [12] | Aucun accès à la production, sauvegardes, interdits bloqués, accord humain avant toute destruction ([[fiche-7#Réglages par outil\|fiche 7]]) |
| Compétences perdues | Les compétences s'usent quand on ne s'en sert plus [7] ; avec l'IA, sans chercher à comprendre, on apprend moins [8] ([[fiche-3#Le plus grand danger, vous\|fiche 3]]) | Tracer la ligne en mode plan, le questionnaire ([[fiche-4#Le questionnaire\|fiche 4]]), le point sur ce qui a changé ([[fiche-7#Ce qui a changé\|fiche 7]]), la veille ([[fiche-8#La veille\|fiche 8]]) |
| Consignes cachées | Dans une démonstration, des caractères invisibles dans un fichier de règles ont fait ajouter un script malveillant, sans que l'IA le dise [13] | Relire règles et skills comme du code, avec un outil qui voit l'invisible ; droits minimaux |

## Sources de cette fiche

Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].

- \[7] **Les compétences s'usent quand la machine fait le travail.** Un essai classique sur l'automatisation des usines et des cockpits. [Bainbridge, « Ironies of Automation », *Automatica*, 1983](https://doi.org/10.1016/0005-1098(83)90046-8)
- \[8] **Apprendre avec l'IA sans chercher à comprendre, c'est moins apprendre.** 52 développeurs qui découvraient une bibliothèque Python ; pas encore relue par des pairs. [Shen et Tamkin, Anthropic, 29/01/26](https://www.anthropic.com/research/AI-assistance-coding-skills), et [l'article](https://arxiv.org/abs/2601.20245)
- \[10] **Des jurisprudences inventées, défendues devant un juge.** [Tribunal fédéral de New York, *Mata v. Avianca*, 22/06/23](https://www.nhd.uscourts.gov/sites/default/files/pdf/Mata-v-Avianca-sanctions-order.PDF)
- \[11] **Des secrets poussés sur GitHub.** [GitGuardian, « State of Secrets Sprawl 2026 », 17/03/26](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/)
- \[12] **Un agent qui efface des données de production.** [The Register, 21/07/25](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/)
- \[13] **Des consignes invisibles dans un fichier de règles.** [Pillar Security, 18/03/25](https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents)

↑ [[index|L'essentiel]] · ← [[fiche-8|8. Améliorer, niveau par niveau]]

Olivier & Mentordinator
