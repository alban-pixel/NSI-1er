"""
Défi 7 — Collisions entre sprites
Carnet de défis Pyxel — Première spécialité NSI

Les flèches déplacent le personnage, qui doit éviter trois bombes.
Au contact d'une bombe, le personnage explose et la partie s'arrête.
Les sprites sont lus dans "tuto.pyxres" (même dossier que ce programme).
Les questions et les modifications à réaliser sont dans le carnet (défi 7).
"""
import pyxel

pyxel.init(128, 128, title="Collisions entre sprites", fps=30)
pyxel.load("tuto.pyxres")

# Le personnage : sprite de 8 x 8 pixels
xperso = 60
yperso = 100
en_vie = True

# Les trois bombes : sprites de 6 x 6 pixels.
# Elles partent au-dessus de la fenêtre, à des hauteurs différentes.
x_bombe1 = pyxel.rndi(0, 128 - 6)
y_bombe1 = -8
x_bombe2 = pyxel.rndi(0, 128 - 6)
y_bombe2 = -48
x_bombe3 = pyxel.rndi(0, 128 - 6)
y_bombe3 = -88

# Numéro de la frame où l'explosion a commencé
debut_explosion = 0


def collision(r1_xmin, r1_ymin, r1_xmax, r1_ymax, r2_xmin, r2_ymin, r2_xmax, r2_ymax):
    """Renvoie True si les deux rectangles, donnés par leurs bords, se chevauchent."""
    return not (r1_xmax < r2_xmin or r1_xmin > r2_xmax or r1_ymax < r2_ymin or r1_ymin > r2_ymax)


def update():
    global xperso, yperso, en_vie, debut_explosion
    global x_bombe1, y_bombe1, x_bombe2, y_bombe2, x_bombe3, y_bombe3

    # Une fois le personnage touché, plus rien ne bouge
    if not en_vie:
        return

    # Déplacement du personnage
    if pyxel.btn(pyxel.KEY_LEFT):
        xperso = xperso - 2
    elif pyxel.btn(pyxel.KEY_RIGHT):
        xperso = xperso + 2
    elif pyxel.btn(pyxel.KEY_UP):
        yperso = yperso - 2
    elif pyxel.btn(pyxel.KEY_DOWN):
        yperso = yperso + 2
    xperso = pyxel.clamp(xperso, 0, 128 - 8)
    yperso = pyxel.clamp(yperso, 0, 128 - 8)

    # Chute des bombes : 2 pixels, une frame sur deux
    if pyxel.frame_count % 2 == 0:
        y_bombe1 = y_bombe1 + 2
        y_bombe2 = y_bombe2 + 2
        y_bombe3 = y_bombe3 + 2

    # Une bombe sortie par le bas repart du haut, à une nouvelle abscisse
    if y_bombe1 > 128:
        y_bombe1 = -8
        x_bombe1 = pyxel.rndi(0, 128 - 6)
    if y_bombe2 > 128:
        y_bombe2 = -8
        x_bombe2 = pyxel.rndi(0, 128 - 6)
    if y_bombe3 > 128:
        y_bombe3 = -8
        x_bombe3 = pyxel.rndi(0, 128 - 6)

    # Le personnage touche-t-il une bombe ?
    touche1 = collision(xperso, yperso, xperso + 7, yperso + 7,
                        x_bombe1, y_bombe1, x_bombe1 + 5, y_bombe1 + 5)
    touche2 = collision(xperso, yperso, xperso + 7, yperso + 7,
                        x_bombe2, y_bombe2, x_bombe2 + 5, y_bombe2 + 5)
    touche3 = collision(xperso, yperso, xperso + 7, yperso + 7,
                        x_bombe3, y_bombe3, x_bombe3 + 5, y_bombe3 + 5)
    if touche1 or touche2 or touche3:
        en_vie = False
        debut_explosion = pyxel.frame_count


def draw():
    pyxel.cls(0)
    # Les bombes
    pyxel.blt(x_bombe1, y_bombe1, 0, 73, 26, 6, 6, 0)
    pyxel.blt(x_bombe2, y_bombe2, 0, 73, 26, 6, 6, 0)
    pyxel.blt(x_bombe3, y_bombe3, 0, 73, 26, 6, 6, 0)

    if en_vie:
        pyxel.blt(xperso, yperso, 0, 16, 0, 8, 8, 0)
    else:
        # Explosion : 6 dessins côte à côte dans l'image (abscisses 0, 8, ..., 40),
        # on passe au dessin suivant toutes les 4 frames
        etape = (pyxel.frame_count - debut_explosion) // 4
        if etape < 6:
            pyxel.blt(xperso, yperso, 0, etape * 8, 32, 8, 8, 0)
        else:
            pyxel.text(46, 60, "Game over", 7)


pyxel.run(update, draw)
