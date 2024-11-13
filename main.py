from tkinter import Tk, Canvas
import random
from Particules import Particule
from Vec2 import Vec2
from Terrain import Terrain

# Gestion de la fenêtre Tkinter et du canvas
root = Tk()
root.geometry("1024x512")

canvas = Canvas(root, width=1024, height=512)
canvas.pack()

# Dessiner le rectangle gris
terrains = []
coords = [[Vec2(200,100),Vec2(200,100)]]
def initTerrain():
    for t in coords:
        terrain = Terrain(t[0],t[1],"gray")
        terrain.createTerrain(canvas)
        terrains.append(terrain)

#canvas.create_rectangle(100, 100, 150, 150, fill="gray")


# Liste des particules
particules = []

# Fonction de création de particules au clic
def on_click(event):
    pos = (event.x, event.y)
    vel = (random.choice([-3, 3]), random.choice([-3, 3]))
    size = 10
    particule = Particule(canvas, pos, vel, size)
    particules.append(particule)

# Fonction pour animer les particules
def animate():
    for particule in particules:
        particule.move()
    # Appel récursif pour animer en continu
    root.after(20, animate)

# Associer l'événement de clic à la création de particules
canvas.bind("<Button-1>", on_click)
initTerrain()
# Lancer l'animation
animate()

# Exécuter la boucle principale Tkinter
root.mainloop()