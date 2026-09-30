"""
Défi 5 — Saute !
Carnet de défis Pyxel — Première spécialité NSI

Appuyer sur la barre d'espace pour faire sauter le carré vert.
Le but est de comprendre comment une vitesse et une gravité simulent un saut.
Pendant un saut, la console affiche les couples (dyrect, yrect).
Les questions et les modifications à réaliser sont dans le carnet (défi 5).
"""
import pyxel

pyxel.init(160, 100, title="Saute !", fps=30)

# Réglages du saut
gravité = 1        # augmentation de la vitesse verticale à chaque frame
force_saut = -10   # vitesse verticale donnée au début d'un saut (négative = vers le haut)

# Le sol est la ligne d'ordonnée 100 (le bas de la fenêtre)
sol = 100

# Le joueur est un carré de 8 x 8 pixels
xrect = 0      # abscisse du coin supérieur gauche
yrect = 92     # ordonnée du coin supérieur gauche : posé sur le sol
dyrect = 0     # vitesse verticale : déplacement vertical à chaque frame


def update():
    global xrect, yrect, dyrect

    # Défilement horizontal : en sortant à droite, le carré revient à gauche
    xrect = (xrect + 1) % 160

    # Saut : seulement si la barre d'espace vient d'être enfoncée
    # et si le carré est posé sur le sol
    if pyxel.btnp(pyxel.KEY_SPACE):
        if yrect + 8 >= sol:
            dyrect = force_saut

    # À chaque frame : la gravité modifie la vitesse, puis la vitesse modifie la position
    dyrect = dyrect + gravité
    yrect = yrect + dyrect

    # Collision avec le sol : on replace le carré sur le sol et on arrête sa chute
    if yrect + 8 >= sol:
        yrect = sol - 8
        dyrect = 0
    else:
        print(dyrect, yrect)


def draw():
    pyxel.cls(0)
    pyxel.rect(xrect, yrect, 8, 8, 11)


pyxel.run(update, draw)
