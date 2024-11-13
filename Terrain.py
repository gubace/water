from tkinter import Tk, Canvas


class Terrain :
    def __init__(self,c1,c2,color = "gray") :
        self.c1 = c1
        self.c2 = c2
        self.color = color
        
        
    def createTerrain(self,canvas):
        canvas.create_rectangle(self.c1.x,self.c1.y,self.c2.x,self.c2.y, fill=self.color)