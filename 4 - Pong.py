"""
Défi 4 — Pong (défi expert)
Carnet de défis Pyxel — Première spécialité NSI

Le programme affiche deux raquettes et une balle en mouvement.
  - Raquette de gauche : touches W (haut) et S (bas)
  - Raquette de droite : flèches haut et bas
  - Barre d'espace : replace la balle à son point de départ
Il reste à compléter le jeu : rebonds, points, score, fin de manche...
Les questions et les modifications à réaliser sont dans le carnet (défi 4).
"""
import pyxel

LARGEUR = 160
HAUTEUR = 120
pyxel.init(LARGEUR, HAUTEUR, title="Pong", fps=30)

# Dimensions des objets
LARGEUR_RAQUETTE = 3
HAUTEUR_RAQUETTE = 16
VITESSE_RAQUETTE = 2
TAILLE_BALLE = 4

# Raquettes : x est fixe, seul y change
x_raquette_gauche = 4
y_raquette_gauche = 52
x_raquette_droite = LARGEUR - 4 - LARGEUR_RAQUETTE
y_raquette_droite = 52

# Balle : position (x_balle, y_balle) et déplacement à chaque frame (dx_balle, dy_balle)
x_balle = 60
y_balle = 40
dx_balle = 2
dy_balle = -1

score_gauche = 0
score_droite = 0


def update():
    global y_raquette_gauche, y_raquette_droite
    global x_balle, y_balle, dx_balle, dy_balle
    global score_gauche, score_droite

    # Déplacement de la raquette de gauche
    if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_Z):
        y_raquette_gauche = y_raquette_gauche - VITESSE_RAQUETTE
    if pyxel.btn(pyxel.KEY_S):
        y_raquette_gauche = y_raquette_gauche + VITESSE_RAQUETTE

    # Déplacement de la raquette de droite
    if pyxel.btn(pyxel.KEY_UP):
        y_raquette_droite = y_raquette_droite - VITESSE_RAQUETTE
    if pyxel.btn(pyxel.KEY_DOWN):
        y_raquette_droite = y_raquette_droite + VITESSE_RAQUETTE

    # Les raquettes restent dans la fenêtre
    y_raquette_gauche = pyxel.clamp(y_raquette_gauche, 0, HAUTEUR - HAUTEUR_RAQUETTE)
    y_raquette_droite = pyxel.clamp(y_raquette_droite, 0, HAUTEUR - HAUTEUR_RAQUETTE)

    # Déplacement de la balle (pour l'instant, rien ne l'arrête)
    x_balle = x_balle + dx_balle
    y_balle = y_balle + dy_balle

    if y_balle <= 0:
        y_balle = 0
        dy_balle = -dy_balle
    elif y_balle + TAILLE_BALLE >= HAUTEUR:
        y_balle = HAUTEUR - TAILLE_BALLE
        dy_balle = -dy_balle

    if (
        x_balle <= x_raquette_gauche + LARGEUR_RAQUETTE
        and x_balle + TAILLE_BALLE >= x_raquette_gauche
        and y_balle + TAILLE_BALLE >= y_raquette_gauche
        and y_balle <= y_raquette_gauche + HAUTEUR_RAQUETTE
        and dx_balle < 0
    ):
        x_balle = x_raquette_gauche + LARGEUR_RAQUETTE
        dx_balle = -dx_balle

    if (
        x_balle + TAILLE_BALLE >= x_raquette_droite
        and x_balle <= x_raquette_droite + LARGEUR_RAQUETTE
        and y_balle + TAILLE_BALLE >= y_raquette_droite
        and y_balle <= y_raquette_droite + HAUTEUR_RAQUETTE
        and dx_balle > 0
    ):
        x_balle = x_raquette_droite - TAILLE_BALLE
        dx_balle = -dx_balle

    if x_balle < 0:
        score_droite += 1
        x_balle = 60
        y_balle = 40
        dx_balle = 2
        dy_balle = 1

    if x_balle + TAILLE_BALLE > LARGEUR:
        score_gauche += 1
        x_balle = 60
        y_balle = 40
        dx_balle = -2
        dy_balle = -1

    # Barre d'espace : on replace la balle au départ
    if pyxel.btnp(pyxel.KEY_SPACE):
        x_balle = 60
        y_balle = 40
        dx_balle = 2
        dy_balle = -1


def draw():
    pyxel.cls(1)
    # Ligne centrale en pointillés : un petit trait tous les 8 pixels
    for y in range(0, HAUTEUR, 8):
        pyxel.rect(LARGEUR // 2 - 1, y, 2, 4, 5)
    # Raquettes
    pyxel.rect(x_raquette_gauche, y_raquette_gauche, LARGEUR_RAQUETTE, HAUTEUR_RAQUETTE, 7)
    pyxel.rect(x_raquette_droite, y_raquette_droite, LARGEUR_RAQUETTE, HAUTEUR_RAQUETTE, 7)
    # Balle
    pyxel.rect(x_balle, y_balle, TAILLE_BALLE, TAILLE_BALLE, 10)
    pyxel.text(LARGEUR // 2 - 20, 8, str(score_gauche), 7)
    pyxel.text(LARGEUR // 2 + 16, 8, str(score_droite), 7)


pyxel.run(update, draw)
