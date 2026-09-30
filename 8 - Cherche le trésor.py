"""
Défi 8 — Cherche le trésor (défi expert)
Carnet de défis Pyxel — Première spécialité NSI

Flèches gauche et droite : marcher. Barre d'espace : sauter.
Il faut éviter les rivières de feu et atteindre le coffre, tout à droite.
Le niveau (768 x 128 pixels) est plus large que la fenêtre (256 x 128) :
l'affichage suit le personnage.
Le décor est dessiné avec la tilemap 0 de "tuto.pyxres" (même dossier).
Le temple n'est qu'un décor : on passe devant.
Les questions et les modifications à réaliser sont dans le carnet (défi 8).
"""
import pyxel

LARGEUR_ECRAN = 256
HAUTEUR_ECRAN = 128
LARGEUR_NIVEAU = 768
pyxel.init(LARGEUR_ECRAN, HAUTEUR_ECRAN, title="Cherche le trésor", fps=30)
pyxel.load("tuto.pyxres")

# Réglages
VITESSE = 2
GRAVITE = 1
FORCE_SAUT = -8

# Le personnage : sprite de 8 x 8 pixels, positions exprimées dans le niveau
x_perso = 10
y_perso = 104
dy_perso = 0       # vitesse verticale
u_sprite = 32      # abscisse, dans l'image 0, du dessin à afficher

# Abscisse de la partie du niveau affichée à l'écran
x_camera = 0

# Obstacles infranchissables : x, y, largeur, hauteur
x_sol1, y_sol1, largeur_sol1, hauteur_sol1 = 0, 120, 128, 8
x_sol2, y_sol2, largeur_sol2, hauteur_sol2 = 144, 120, 352, 8
x_sol3, y_sol3, largeur_sol3, hauteur_sol3 = 520, 120, 96, 8
x_rondins1, y_rondins1, largeur_rondins1, hauteur_rondins1 = 208, 112, 56, 8
x_rondins2, y_rondins2, largeur_rondins2, hauteur_rondins2 = 328, 112, 40, 8
x_plateau, y_plateau, largeur_plateau, hauteur_plateau = 616, 104, 152, 24
x_rocher, y_rocher, largeur_rocher, hauteur_rocher = 744, 96, 24, 8

# Zones dangereuses (rivières de feu)
x_feu1, y_feu1, largeur_feu1, hauteur_feu1 = 128, 120, 16, 8
x_feu2, y_feu2, largeur_feu2, hauteur_feu2 = 496, 120, 24, 8

# Le trésor (le coffre dessiné dans le décor)
x_tresor = 672
y_tresor = 96

# État de la partie
perdu = False
gagne = False


def collision(x1, y1, largeur1, hauteur1, x2, y2, largeur2, hauteur2):
    """Renvoie True si les deux rectangles se chevauchent."""
    return (x1 < x2 + largeur2 and x2 < x1 + largeur1
            and y1 < y2 + hauteur2 and y2 < y1 + hauteur1)


def position_libre(x, y):
    """Renvoie True si le personnage placé en (x, y) ne touche aucun obstacle."""
    if collision(x, y, 8, 8, x_sol1, y_sol1, largeur_sol1, hauteur_sol1):
        return False
    if collision(x, y, 8, 8, x_sol2, y_sol2, largeur_sol2, hauteur_sol2):
        return False
    if collision(x, y, 8, 8, x_sol3, y_sol3, largeur_sol3, hauteur_sol3):
        return False
    if collision(x, y, 8, 8, x_rondins1, y_rondins1, largeur_rondins1, hauteur_rondins1):
        return False
    if collision(x, y, 8, 8, x_rondins2, y_rondins2, largeur_rondins2, hauteur_rondins2):
        return False
    if collision(x, y, 8, 8, x_plateau, y_plateau, largeur_plateau, hauteur_plateau):
        return False
    if collision(x, y, 8, 8, x_rocher, y_rocher, largeur_rocher, hauteur_rocher):
        return False
    return True


def deplacer_horizontalement(dx):
    """Déplace le personnage de dx pixels si la position visée est libre."""
    global x_perso
    nouveau_x = pyxel.clamp(x_perso + dx, 0, LARGEUR_NIVEAU - 8)
    if position_libre(nouveau_x, y_perso):
        x_perso = nouveau_x


def appliquer_gravite():
    """Met à jour la vitesse verticale puis la position verticale du personnage."""
    global y_perso, dy_perso
    dy_perso = dy_perso + GRAVITE
    nouveau_y = y_perso + dy_perso
    if position_libre(x_perso, nouveau_y):
        y_perso = nouveau_y
    else:
        # La position visée est dans un obstacle : on avance pixel par pixel
        # tant que c'est possible, pour finir exactement contre l'obstacle.
        if dy_perso > 0:
            pas = 1
        else:
            pas = -1
        while position_libre(x_perso, y_perso + pas):
            y_perso = y_perso + pas
        dy_perso = 0
    # Le personnage ne sort pas par le bas de l'écran (il est alors dans le feu)
    if y_perso > HAUTEUR_ECRAN - 8:
        y_perso = HAUTEUR_ECRAN - 8
        dy_perso = 0


def update():
    global dy_perso, u_sprite, x_camera, perdu, gagne

    if perdu or gagne:
        return

    # 1) Marche : on alterne entre deux dessins toutes les 5 frames
    if pyxel.btn(pyxel.KEY_RIGHT):
        deplacer_horizontalement(VITESSE)
        if (pyxel.frame_count // 5) % 2 == 0:
            u_sprite = 32
        else:
            u_sprite = 40
    elif pyxel.btn(pyxel.KEY_LEFT):
        deplacer_horizontalement(-VITESSE)
        if (pyxel.frame_count // 5) % 2 == 0:
            u_sprite = 0
        else:
            u_sprite = 8

    # 2) Saut : seulement si le personnage est posé sur quelque chose
    au_sol = not position_libre(x_perso, y_perso + 1)
    if pyxel.btnp(pyxel.KEY_SPACE) and au_sol:
        dy_perso = FORCE_SAUT

    # 3) Gravité
    appliquer_gravite()

    # 4) Fin de partie
    if collision(x_perso, y_perso, 8, 8, x_feu1, y_feu1, largeur_feu1, hauteur_feu1):
        perdu = True
    if collision(x_perso, y_perso, 8, 8, x_feu2, y_feu2, largeur_feu2, hauteur_feu2):
        perdu = True
    if collision(x_perso, y_perso, 8, 8, x_tresor, y_tresor, 8, 8):
        gagne = True

    # 5) La caméra suit le personnage sans sortir du niveau
    x_camera = pyxel.clamp(x_perso - LARGEUR_ECRAN // 3, 0, LARGEUR_NIVEAU - LARGEUR_ECRAN)


def draw():
    pyxel.cls(0)
    # Décor : la partie de la tilemap 0 qui commence à x_camera
    pyxel.bltm(0, 0, 0, x_camera, 0, LARGEUR_ECRAN, HAUTEUR_ECRAN)
    # Personnage : sa position à l'écran dépend de la caméra
    pyxel.blt(x_perso - x_camera, y_perso, 0, u_sprite, 8, 8, 8, 0)
    if perdu:
        pyxel.text(106, 60, "Game over !", 11)
    if gagne:
        pyxel.text(80, 60, "Bravo, c'est le coffre !", 11)


pyxel.run(update, draw)
