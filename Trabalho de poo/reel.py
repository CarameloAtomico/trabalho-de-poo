import pygame
import random 
from symbol import Symbol
class Reel:
    def __init__(self, x1):
        self.x = x1
        self.ativado = False
        self.symbols = []
        vals = ["A", "B", "C", "D", "E", "F", "G"]
        for i in range(5):
            val = random.choice(vals)
            s = Symbol(self.x, 200+75*i, 75, 75, val, 0)
            self.symbols.append(s)