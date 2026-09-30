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

point_player1 = 0
point_player2 = 0

def update():
    global y_raquette_gauche, y_raquette_droite
    global x_balle, y_balle, dx_balle, dy_balle

    # Déplacement de la raquette de gauche
    if pyxel.btn(pyxel.KEY_W):
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

    # Barre d'espace : on replace la balle au départ
    if pyxel.btnp(pyxel.KEY_SPACE):
        x_balle = 60
        y_balle = 40
        dx_balle = 2
        dy_balle = -1

    end_of_round()

def end_of_round():
    global x_balle, point_player1, point_player2

    if x_balle <= 0:
        point_player2 +=1
        init_round()
    elif x_balle >= 160- TAILLE_BALLE:   
        point_player1 += 1
        init_round()

def init_round():
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
    #point
    pyxel.text(60,12,str(point_player1),10)
    pyxel.text(100,12,str(point_player2),10)

pyxel.run(update, draw)
