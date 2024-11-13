# Classe des particules
from tkinter import Tk, Canvas
import random

class Particule:
    def __init__(self, canvas, pos, vel, size):
        self.canvas = canvas
        self.pos = pos
        self.velocity = vel
        self.size = size
        # Créer l'objet visuel de la particule
        x, y = pos
        self.id = self.canvas.create_oval(x - size, y - size, x + size, y + size, fill="blue")

    def move(self):
        # Met à jour la position
        x, y = self.pos
        vx, vy = self.velocity
        new_x, new_y = x + vx, y + vy

        # Détecter la collision avec le rectangle gris
        if 100 <= new_x <= 300 and 100 <= new_y <= 300:
            # Inverser la direction en cas de collision
            vx = -vx
            vy = -vy

        # Mettre à jour la position et la vélocité
        self.pos = (new_x, new_y)
        self.velocity = (vx, vy)

        # Déplacer le cercle sur le canvas
        self.canvas.move(self.id, vx, vy)