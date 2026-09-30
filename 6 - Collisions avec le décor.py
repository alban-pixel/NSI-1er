"""
Défi 6 — Collisions avec le décor
Carnet de défis Pyxel — Première spécialité NSI

Les flèches déplacent le personnage dans un décor formé de murs rectangulaires.
Chaque mur est décrit par quatre variables : x, y, largeur et hauteur.
Les sprites sont lus dans "tuto.pyxres" (même dossier que ce programme).
Les questions et les modifications à réaliser sont dans le carnet (défi 6).
"""
import pyxel

pyxel.init(128, 128, title="Collisions avec le décor", fps=30)
pyxel.load("tuto.pyxres")

VITESSE = 2

# Le personnage : sprite de 8 x 8 pixels
xperso = 20
yperso = 24

# Les murs du décor : x, y (coin supérieur gauche), largeur, hauteur
x_mur1, y_mur1, largeur_mur1, hauteur_mur1 = 80, 8, 24, 8
x_mur2, y_mur2, largeur_mur2, hauteur_mur2 = 16, 32, 24, 8
x_mur3, y_mur3, largeur_mur3, hauteur_mur3 = 72, 48, 32, 8
x_mur4, y_mur4, largeur_mur4, hauteur_mur4 = 40, 64, 8, 40
x_mur5, y_mur5, largeur_mur5, hauteur_mur5 = 96, 80, 16, 8
x_mur6, y_mur6, largeur_mur6, hauteur_mur6 = 0, 120, 128, 8     # le sol


def collision(x1, y1, largeur1, hauteur1, x2, y2, largeur2, hauteur2):
    """Renvoie True si les deux rectangles se chevauchent."""
    chevauchement_horizontal = x1 < x2 + largeur2 and x2 < x1 + largeur1
    chevauchement_vertical = y1 < y2 + hauteur2 and y2 < y1 + hauteur1
    return chevauchement_horizontal and chevauchement_vertical


def position_libre(x, y):
    """Renvoie True si le personnage placé en (x, y) ne touche aucun mur."""
    if collision(x, y, 8, 8, x_mur1, y_mur1, largeur_mur1, hauteur_mur1):
        return False
    if collision(x, y, 8, 8, x_mur2, y_mur2, largeur_mur2, hauteur_mur2):
        return False
    if collision(x, y, 8, 8, x_mur3, y_mur3, largeur_mur3, hauteur_mur3):
        return False
    if collision(x, y, 8, 8, x_mur4, y_mur4, largeur_mur4, hauteur_mur4):
        return False
    if collision(x, y, 8, 8, x_mur5, y_mur5, largeur_mur5, hauteur_mur5):
        return False
    if collision(x, y, 8, 8, x_mur6, y_mur6, largeur_mur6, hauteur_mur6):
        return False
    return True


def update():
    global xperso, yperso

    # Déplacement horizontal : on calcule la position souhaitée,
    # puis on ne l'applique que si elle est libre
    if pyxel.btn(pyxel.KEY_LEFT):
        nouveau_x = xperso - VITESSE
        if position_libre(nouveau_x, yperso):
            xperso = nouveau_x
    elif pyxel.btn(pyxel.KEY_RIGHT):
        nouveau_x = xperso + VITESSE
        if position_libre(nouveau_x, yperso):
            xperso = nouveau_x

    # Déplacement vertical : ici, les murs ne sont pas encore testés !
    elif pyxel.btn(pyxel.KEY_UP):
        yperso = yperso - VITESSE
    elif pyxel.btn(pyxel.KEY_DOWN):
        yperso = yperso + VITESSE

    # Le personnage reste entièrement dans la fenêtre
    xperso = pyxel.clamp(xperso, 0, 128 - 8)
    yperso = pyxel.clamp(yperso, 0, 128 - 8)


def dessiner_mur(x, y, largeur, hauteur):
    """Remplit le rectangle avec la tuile de brique (8 x 8) de l'image 0."""
    for ligne in range(y, y + hauteur, 8):
        for colonne in range(x, x + largeur, 8):
            pyxel.blt(colonne, ligne, 0, 48, 88, 8, 8)


def draw():
    pyxel.cls(0)
    dessiner_mur(x_mur1, y_mur1, largeur_mur1, hauteur_mur1)
    dessiner_mur(x_mur2, y_mur2, largeur_mur2, hauteur_mur2)
    dessiner_mur(x_mur3, y_mur3, largeur_mur3, hauteur_mur3)
    dessiner_mur(x_mur4, y_mur4, largeur_mur4, hauteur_mur4)
    dessiner_mur(x_mur5, y_mur5, largeur_mur5, hauteur_mur5)
    dessiner_mur(x_mur6, y_mur6, largeur_mur6, hauteur_mur6)
    # Le personnage, avec le noir (couleur 0) comme couleur transparente
    pyxel.blt(xperso, yperso, 0, 16, 0, 8, 8, 0)


pyxel.run(update, draw)
