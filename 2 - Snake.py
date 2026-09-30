"""
Défi 2 — Snake
Carnet de défis Pyxel — Première spécialité NSI

Un serpent de longueur fixe (une tête et quatre segments) avance sur une grille.
Les flèches changent sa direction. Une pomme est posée sur la grille.
Les questions et les modifications à réaliser sont dans le carnet (défi 2).
"""
import pyxel

# Le jeu se déroule sur une grille de 32 colonnes et 32 lignes.
# Chaque case de la grille mesure 8 x 8 pixels.
TAILLE_GRILLE = 32
TAILLE_CASE = 8
pyxel.init(TAILLE_GRILLE * TAILLE_CASE, TAILLE_GRILLE * TAILLE_CASE, title="Snake", fps=10)

# Position de la tête et des segments, en numéros de colonne (x) et de ligne (y).
# Le segment 2 suit la tête, le segment 3 suit le segment 2, etc.
x_tete, y_tete = 5, 2
x_segment2, y_segment2 = 4, 2
x_segment3, y_segment3 = 3, 2
x_segment4, y_segment4 = 2, 2
x_segment5, y_segment5 = 1, 2

# Direction du déplacement : nombre de cases parcourues par la tête à chaque frame
dx = 1
dy = 0

# Position de la pomme
pomme_x = 12
pomme_y = 7


def update():
    global x_tete, y_tete, x_segment2, y_segment2, x_segment3, y_segment3
    global x_segment4, y_segment4, x_segment5, y_segment5, dx, dy

    # 1) Choix de la direction
    if pyxel.btnp(pyxel.KEY_LEFT):
        dx, dy = -1, 0
    elif pyxel.btnp(pyxel.KEY_RIGHT):
        dx, dy = 1, 0
    elif pyxel.btnp(pyxel.KEY_UP):
        dx, dy = 0, -1
    elif pyxel.btnp(pyxel.KEY_DOWN):
        dx, dy = 0, 1

    # 2) Les segments suivent : chacun prend l'ancienne place de celui qui le précède.
    #    On commence par la queue, sinon on perdrait des positions.
    x_segment5, y_segment5 = x_segment4, y_segment4
    x_segment4, y_segment4 = x_segment3, y_segment3
    x_segment3, y_segment3 = x_segment2, y_segment2
    x_segment2, y_segment2 = x_tete, y_tete

    # 3) La tête avance dans la direction choisie
    x_tete = x_tete + dx
    y_tete = y_tete + dy


def dessiner_case(colonne, ligne, couleur):
    pyxel.rect(colonne * TAILLE_CASE, ligne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE, couleur)


def draw():
    pyxel.cls(0)
    # La pomme
    dessiner_case(pomme_x, pomme_y, 8)
    # Les segments du corps
    dessiner_case(x_segment2, y_segment2, 15)
    dessiner_case(x_segment3, y_segment3, 15)
    dessiner_case(x_segment4, y_segment4, 15)
    dessiner_case(x_segment5, y_segment5, 15)
    # La tête, dessinée en dernier pour rester visible
    dessiner_case(x_tete, y_tete, 14)


pyxel.run(update, draw)
