import pygame
import random 
class Symbol(pygame.Rect):
    def __init__(self, x, y, length, width, val1, vel1):
        super().__init__(x, y, length, width)
        #dicionário de cores
        self.cores = {
            "A": (255, 255, 255),
            "B": (255, 0, 255),
            "C": (0, 0, 255),
            "D": (255, 255, 0),
            "E": (255, 0, 0),
            "F": (0, 255, 0),
            "G": (0, 255, 255)
        }
        #valor, cor e velocidade
        self.val = val1
        self.cor = self.cores[self.val]
        self.vel = vel1
    
    def setval(self, val):
        self.val = val
        self.cor = self.cores[self.val]
    def setvel(self, vel):
        self.vel = vel
    def getcor(self):
        return self.cor
    
    def roll(self):
        vals = ["A", "B", "C", "D", "E", "F", "G"]
        self.y += self.vel
        if self.y >= 575:
            self.y = 200
            self.setval(random.choice(vals))