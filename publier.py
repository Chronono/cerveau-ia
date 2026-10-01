# -*- coding: utf-8 -*-
"""Copie les fiches « Cerveau IA » du vault dans content/, au format du site.

    python publier.py             copie seulement (pour regarder le diff)
    python publier.py --commiter  copie et commit en local, sans push : on relit, puis git push
    python publier.py --pousser   copie, commit et push : le site se met à jour en quelques minutes

Le vault reste la seule source : on corrige les fiches dans Obsidian, jamais dans content/.
Chaque source de la liste de L'essentiel devient une page (source-01 …), et chaque [n] des fiches
un lien vers elle. Le graphe ne trace que L'essentiel → fiches et fiches → sources (clé « graphe »).
"""
import os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
FICHES = r"C:\Users\olivi\Documents\Obsidian Vault\Projets ECE Mentor\Fiches"
ICI = os.path.dirname(os.path.abspath(__file__))
CONTENU = os.path.join(ICI, "content")

V5 = "Fiche - Un environnement IA à plusieurs (Obsidian + GitHub)"
COULISSES = "Fiche - Construire avec l'IA, les coulisses d'une fiche"
NB_SOURCES = 22  # la liste de L'essentiel, numérotée de 1 à NB_SOURCES

# note du vault -> (chemin, page du site)
PAGES = {COULISSES: (os.path.join(FICHES, COULISSES + ".md"), "coulisses")}
for nom in os.listdir(os.path.join(FICHES, "Cerveau IA")):
    m = re.fullmatch(r"(Cerveau IA 0(\d) - .*)\.md", nom)
    if m:
        page = "index" if m.group(2) == "0" else "fiche-" + m.group(2)
        PAGES[m.group(1)] = (os.path.join(FICHES, "Cerveau IA", nom), page)

LIEN = re.compile(r"(!?)\[\[([^\[\]|#\\]+)(#[^\[\]|\\]+)?((?:\\?\|)[^\[\]]+)?\]\]")
CODE = re.compile(r"(```[\s\S]*?```|`[^`\n]*`)")
CITATION = re.compile(r"\\?\[(\d{1,2})\](?!\()")
TITRES, CITES = {}, {}  # page -> titre ; page -> numéros de sources cités


def hors_code(texte, fonction):
    """Applique fonction au texte hors des blocs et des bouts de code."""
    morceaux = CODE.split(texte)
    for i in range(0, len(morceaux), 2):  # les indices impairs sont du code
        morceaux[i] = fonction(morceaux[i])
    return "".join(morceaux)


def source(n):
    return f"source-{n:02d}"


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

    return hors_code(texte, lambda t: LIEN.sub(un_lien, t))


def citer(texte, page):
    """Chaque [n] (1 à NB_SOURCES) devient un lien vers la page de la source n ; on note les numéros cités."""
    cites = CITES.setdefault(page, set())

    def une(m):
        n = int(m.group(1))
        if not 1 <= n <= NB_SOURCES:
            return m.group(0)
        cites.add(n)
        return f"[\\[{n}\\]]({source(n)})"

    return hors_code(texte, lambda t: CITATION.sub(une, t))


def entete(titre, graphe):
    titre_yaml = titre.replace("\\", "\\\\").replace('"', '\\"')
    liste = ", ".join(f'"{g}"' for g in graphe)
    return f'---\ntitle: "{titre_yaml}"\ngraphe: [{liste}]\n---\n\n'


def convertir(chemin, page, erreurs):
    t = open(chemin, encoding="utf-8").read().replace("\r\n", "\n")
    t = re.sub(r"\A#\w[^\n]*\n", "", t)  # la ligne de tags (#ece #fiche #ia)
    m = re.search(r"^# (.+)\n", t, flags=re.M)
    if not m:
        erreurs.append(f"{page} : pas de titre « # »")
        return None
    TITRES[page] = m.group(1).strip()
    t = t[:m.start()] + t[m.end():]  # Quartz affiche le titre lui-même
    t = re.sub(r"^(?:> ?)*%%[\s\S]*?%%[ \t]*\n", "", t, flags=re.M)  # commentaires seuls sur leur ligne
    t = re.sub(r"%%[\s\S]*?%%", "", t)  # commentaires dans le texte
    t = relier(t, page, erreurs)
    if page == "index" or page.startswith("fiche-"):
        t = citer(t, page)
    return t.lstrip("\n")


def lire_sources(index, erreurs):
    """La liste de L'essentiel, déjà convertie : numéro -> (famille, titre en gras, reste de la ligne)."""
    _, _, liste = index.partition("## Toutes les sources")
    sources, famille = {}, ""
    for ligne in liste.splitlines():
        f = re.match(r"> \*\*(.+?)\*\* : ", ligne)
        if f:
            famille = f.group(1)
        s = re.match(r"> (\d{1,2})\. \*\*(.+?)\*\* ?(.*)$", ligne)
        if s:
            sources[int(s.group(1))] = (famille, s.group(2), s.group(3))
    if sorted(sources) != list(range(1, NB_SOURCES + 1)):
        erreurs.append(f"liste des sources de L'essentiel incomplète : {sorted(sources)}")
    return sources


def page_source(n, famille, gras, reste):
    fiches = sorted((p for p, c in CITES.items() if n in c and p != "index"), key=lambda p: int(p[6:]))
    liens = [f"[[{p}|{TITRES[p]}]]" for p in fiches]
    dans = ", ".join(liens[:-1]) + " et " + liens[-1] if len(liens) > 1 else "".join(liens)
    if n in CITES.get("index", ()):
        dans = (dans + ", ainsi que " if dans else "") + "[[index|L'essentiel]]"
    return (entete(f"[{n}] {gras.rstrip('.')}", [])
            + f"> Source [{n}] des fiches « Donner un cerveau à l'IA de votre équipe » · {famille}\n\n"
            + f"**{gras}** {reste}\n\n"
            + (f"**Citée dans** : {dans}.\n\n" if dans else "Citée dans aucune fiche pour l'instant.\n\n")
            + "Toutes les sources, par famille : [[index#Toutes les sources|L'essentiel]].\n")


def main():
    erreurs, ecrits, textes = [], set(), {}
    pages = {page for _, page in PAGES.values()}
    if len(pages) != len(PAGES) or "index" not in pages:
        sys.exit(f"pages en double ou L'essentiel absent : {sorted(pages)}")
    os.makedirs(CONTENU, exist_ok=True)
    for nom, (chemin, page) in sorted(PAGES.items(), key=lambda x: x[1][1]):
        t = convertir(chemin, page, erreurs)
        if t is not None:
            textes[page] = t
            print(f"{page:10} <- {nom}")
    fiches = sorted((p for p in textes if p.startswith("fiche-")), key=lambda p: int(p[6:]))
    sources = lire_sources(textes.get("index", ""), erreurs)
    for page, t in textes.items():
        if page == "index":
            graphe = fiches + ["coulisses"]
        elif page.startswith("fiche-"):
            graphe = [source(n) for n in sorted(CITES.get(page, ()))]
        else:
            graphe = []
        manquantes = sorted(CITES.get(page, set()) - set(sources))
        if manquantes:
            erreurs.append(f"{page} : sources citées absentes de la liste de L'essentiel {manquantes}")
        textes[page] = entete(TITRES[page], graphe) + t
    for n, (famille, gras, reste) in sources.items():
        textes[source(n)] = page_source(n, famille, gras, reste)
    print(f"{len(sources)} pages de sources ; citées par fiche : "
          + " ; ".join(f"{p[6:]} → {sorted(CITES.get(p, ()))}" for p in fiches))
    for page, t in textes.items():
        with open(os.path.join(CONTENU, page + ".md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(t)
        ecrits.add(page + ".md")
    for vieux in os.listdir(CONTENU):  # une fiche renommée ou retirée du vault quitte le site
        if vieux.endswith(".md") and vieux not in ecrits:
            os.remove(os.path.join(CONTENU, vieux))
            print(f"retiré : {vieux}")
    if erreurs:
        print("\n".join(erreurs))
        sys.exit("rien n'est poussé : corriger d'abord ces points dans le vault")
    if "--pousser" in sys.argv or "--commiter" in sys.argv:
        git = lambda *a: subprocess.run(["git", "-C", ICI, *a], check=True)
        git("add", "-A", "content")
        if subprocess.run(["git", "-C", ICI, "diff", "--cached", "--quiet"]).returncode == 0:
            print("rien n'a changé")
            return
        git("commit", "-q", "-m", "Fiches mises à jour depuis le vault")
        if "--pousser" not in sys.argv:
            print("commité en local, pas poussé : git push quand tout est relu")
            return
        git("push", "-q")
        print("poussé : https://chronono.github.io/cerveau-ia/ dans quelques minutes")


if __name__ == "__main__":
    main()
