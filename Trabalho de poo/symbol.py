import pygame
import random 
class Symbol(pygame.Rect):
    def __init__(self, x, y, length, width, val, reel):
        super().__init__(x, y, length, width)
        #dicionário de cores
        self.cores = {
            "A": pygame.image.load('Sprites/A.png'),
            "B": pygame.image.load('Sprites/B.png'),
            "C": pygame.image.load('Sprites/C.png'),
            "D": pygame.image.load('Sprites/D.png'),
            "E": pygame.image.load('Sprites/E.png'),
            "F": pygame.image.load('Sprites/F.png'),
            "G": pygame.image.load('Sprites/G.png')
        }
        #valor, cor e velocidade
        self.val = val
        self.cor = self.cores[self.val]
        self.vel = 0
        self.vel_max = 0
        self.acel = 0.1
        self.reel = reel
        self.parada = False
        self.pos_parada = self.y
        
    
    def setval(self, val):
        self.val = val
        self.cor = self.cores[self.val]
    def setvel(self, vel):
        self.vel = vel
    def getspr(self):
        return self.cor

    def roll(self):
        vals = ["A", "B", "C", "D", "E", "F", "G"]

        #Aceleração simples
        #Funciona durante o intervalo de giro
        if self.vel < self.vel_max:
            self.vel += 0.3
        else:
            self.vel = self.vel_max
        self.y += self.vel
        if self.y >= 700:
            self.y = 50
            self.setval(random.choice(vals))

        if self.parada:
            self.vel = 0
            if self.y != self.pos_parada:
                if self.y < self.pos_parada:
                    self.y += 10
                    if self.y > self.pos_parada:
                        self.y = self.pos_parada
                else:
                    self.y -= 10
                    if self.y < self.pos_parada:
                        self.y = self.pos_parada
            else:
                self.vel = 0
                self.parada = False