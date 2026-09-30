"""
Défi 1 — Hello Pyxel !
Carnet de défis Pyxel — Première spécialité NSI

Affiche un texte clignotant que l'on déplace avec les flèches du clavier.
Les questions et les modifications à réaliser sont dans le carnet (défi 1).
"""
import pyxel

pyxel.init(128, 128, title="Hello Pyxel", fps=30)

# Coordonnées du coin supérieur gauche du texte affiché
x = 40
y = 30


def update():
    global x, y
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
    elif pyxel.btn(pyxel.KEY_UP):
        y = y - 1
    elif pyxel.btn(pyxel.KEY_DOWN):
        y = y + 1
    if pyxel.btnp(pyxel.KEY_R):
        x = 40
        y = 30




def draw():
    pyxel.cls(0)
    # La couleur change à chaque frame : frame_count % 16 donne un numéro entre 0 et 15
    pyxel.text(pyxel.clamp(int(1.6*x),0,128-16), pyxel.clamp(int(1.6*y),0,122), "6622", 13)


pyxel.run(update, draw)
