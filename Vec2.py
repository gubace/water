from tkinter import Tk, Canvas
import random


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getCoords(self):
        return self.x, self.y
    
    def x(self):
        return self.x
    def y(self):
        return self.y
        
    
    def dot(v,w):
        return v.x*w.x + v.y*w.y