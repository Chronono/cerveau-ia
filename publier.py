# -*- coding: utf-8 -*-
"""Copie les fiches « Cerveau IA » du vault dans content/, au format du site.

    python publier.py             copie seulement (pour regarder le diff)
    python publier.py --pousser   copie, commit et push : le site se met à jour en deux minutes

Le vault reste la seule source : on corrige les fiches dans Obsidian, jamais dans content/.
"""
import os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
FICHES = r"C:\Users\olivi\Documents\Obsidian Vault\Projets ECE Mentor\Fiches"
ICI = os.path.dirname(os.path.abspath(__file__))
CONTENU = os.path.join(ICI, "content")

V5 = "Fiche - Un environnement IA à plusieurs (Obsidian + GitHub)"
COULISSES = "Fiche - Construire avec l'IA, les coulisses d'une fiche"

# note du vault -> (chemin, page du site)
PAGES = {COULISSES: (os.path.join(FICHES, COULISSES + ".md"), "coulisses")}
for nom in os.listdir(os.path.join(FICHES, "Cerveau IA")):
    m = re.fullmatch(r"(Cerveau IA 0(\d) - .*)\.md", nom)
    if m:
        page = "index" if m.group(2) == "0" else "fiche-" + m.group(2)
        PAGES[m.group(1)] = (os.path.join(FICHES, "Cerveau IA", nom), page)

LIEN = re.compile(r"(!?)\[\[([^\[\]|#\\]+)(#[^\[\]|\\]+)?((?:\\?\|)[^\[\]]+)?\]\]")
CODE = re.compile(r"(```[\s\S]*?```|`[^`\n]*`)")


def relier(texte, page, erreurs):
    """Récrit les liens [[note#titre|alias]] vers les pages du site, hors du code."""
    def un_lien(m):
        embed, cible, ancre, alias = m.group(1), m.group(2).strip(), m.group(3) or "", m.group(4) or ""
        cible = os.path.basename(cible)
        cible = cible[:-3] if cible.endswith(".md") else cible
        if embed:
            erreurs.append(f"{page} : intégration non gérée {m.group(0)}")
            return m.group(0)
        if not alias:
            alias = "|" + cible + (" > " + ancre[1:] if ancre else "")
        if cible in PAGES:
            return f"[[{PAGES[cible][1]}{ancre}{alias}]]"
        if cible == V5:  # la version complète n'est pas publiée : on mène à L'essentiel
            return alias.lstrip("\\|") if page == "index" else f"[[index{alias}]]"
        erreurs.append(f"{page} : lien vers une note non publiée {m.group(0)}")
        return m.group(0)

    morceaux = CODE.split(texte)
    for i in range(0, len(morceaux), 2):  # les indices impairs sont du code
        morceaux[i] = LIEN.sub(un_lien, morceaux[i])
    return "".join(morceaux)


def convertir(chemin, page, erreurs):
    t = open(chemin, encoding="utf-8").read().replace("\r\n", "\n")
    t = re.sub(r"\A#\w[^\n]*\n", "", t)  # la ligne de tags (#ece #fiche #ia)
    m = re.search(r"^# (.+)\n", t, flags=re.M)
    if not m:
        erreurs.append(f"{page} : pas de titre « # »")
        return None
    titre = m.group(1).strip()
    t = t[:m.start()] + t[m.end():]  # Quartz affiche le titre lui-même
    t = re.sub(r"^(?:> ?)*%%[\s\S]*?%%[ \t]*\n", "", t, flags=re.M)  # commentaires seuls sur leur ligne
    t = re.sub(r"%%[\s\S]*?%%", "", t)  # commentaires dans le texte
    t = relier(t, page, erreurs)
    titre_yaml = titre.replace("\\", "\\\\").replace('"', '\\"')
    return f'---\ntitle: "{titre_yaml}"\n---\n\n' + t.lstrip("\n")


def main():
    erreurs, ecrits = [], set()
    pages = {page for _, page in PAGES.values()}
    if len(pages) != len(PAGES) or "index" not in pages:
        sys.exit(f"pages en double ou L'essentiel absent : {sorted(pages)}")
    os.makedirs(CONTENU, exist_ok=True)
    for nom, (chemin, page) in sorted(PAGES.items(), key=lambda x: x[1][1]):
        sortie = convertir(chemin, page, erreurs)
        if sortie is None:
            continue
        with open(os.path.join(CONTENU, page + ".md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(sortie)
        ecrits.add(page + ".md")
        print(f"{page:10} <- {nom}")
    for vieux in os.listdir(CONTENU):  # une fiche renommée ou retirée du vault quitte le site
        if vieux.endswith(".md") and vieux not in ecrits:
            os.remove(os.path.join(CONTENU, vieux))
            print(f"retiré : {vieux}")
    if erreurs:
        print("\n".join(erreurs))
        sys.exit("rien n'est poussé : corriger d'abord ces liens dans le vault")
    if "--pousser" in sys.argv:
        git = lambda *a: subprocess.run(["git", "-C", ICI, *a], check=True)
        git("add", "-A", "content")
        if subprocess.run(["git", "-C", ICI, "diff", "--cached", "--quiet"]).returncode == 0:
            print("rien n'a changé")
            return
        git("commit", "-q", "-m", "Fiches mises à jour depuis le vault")
        git("push", "-q")
        print("poussé : https://chronono.github.io/cerveau-ia/ dans deux minutes environ")


if __name__ == "__main__":
    main()
