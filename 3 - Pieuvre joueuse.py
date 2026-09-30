"""
Défi 3 — Pieuvre joueuse
Carnet de défis Pyxel — Première spécialité NSI

Un clic gauche déplace le diamant ; la pieuvre se met aussitôt à le poursuivre.
Les sprites sont lus dans le fichier de ressources "tuto.pyxres",
qui doit se trouver dans le même dossier que ce programme.
Les questions et les modifications à réaliser sont dans le carnet (défi 3).
"""
import pyxel

pyxel.init(128, 128, title="Pieuvre joueuse", fps=30)

# "tuto.pyxres" contient une grande image dans laquelle on découpe les sprites.
# La pieuvre existe en 3 dessins affichés à tour de rôle pour donner l'impression
# qu'elle nage ; le diamant aussi, pour donner l'impression qu'il scintille.
pyxel.load("tuto.pyxres")

x_pieuvre = 60
y_pieuvre = 60
choix_img_pieuvre = 0   # abscisse, dans l'image, du dessin de pieuvre à afficher

x_diamant = 20
y_diamant = 20
choix_img_diamant = 8   # abscisse, dans l'image, du dessin de diamant à afficher

pyxel.mouse(True)


def update():
    global x_pieuvre, y_pieuvre, x_diamant, y_diamant
    global choix_img_pieuvre, choix_img_diamant

    # Un clic gauche place le diamant sous la souris (centré : le sprite fait 8 x 8)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        x_diamant = pyxel.mouse_x - 4
        y_diamant = pyxel.mouse_y - 4

    # Animation : on change de dessin toutes les 5 frames
    choix_img_pieuvre = (pyxel.frame_count // 5) % 3 * 8
    choix_img_diamant = ((pyxel.frame_count // 5) % 3 + 1) * 8

    # La pieuvre parcourt un dixième de la distance qui la sépare du diamant
    x_pieuvre -= (x_pieuvre - x_diamant) / 10
    y_pieuvre -= (y_pieuvre - y_diamant) / 10


def draw():
    pyxel.cls(0)
    pyxel.blt(x_pieuvre, y_pieuvre, 0, choix_img_pieuvre, 48, 8, 8, 0)
    pyxel.blt(x_diamant, y_diamant, 0, choix_img_diamant, 72, 8, 8, 0)
    # Affiche dans la console la position de la souris dans la fenêtre
    print(pyxel.mouse_x, pyxel.mouse_y)


pyxel.run(update, draw)
