import pygame
import random 
class Symbol(pygame.Rect):
    def __init__(self, x, y, length, width, val, reel):
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
    def getcor(self):
        return self.cor

    def roll(self):
        vals = ["A", "B", "C", "D", "E", "F", "G"]

        #Aceleração simples
        if self.vel < self.vel_max:
            self.vel += 0.004
        else:
            self.vel = self.vel_max
        self.y += self.vel
        if self.y >= 525:
            self.y = self.y - 375
            self.setval(random.choice(vals))

        #Retornando os simbolos para os lugares.
        #PROBLEMA: eles só retornam depois que o botão de spin é precionado novamente!!
        #Acho que o problema se encontra aqui abaixo, mas pode estar também no arquivo reel
        if self.parada:
            if self.y != self.pos_parada:
                if self.y < self.pos_parada:
                    # Fazer estes com self.y = self.pos_parada funciona
                    # Velocidade por algum motivo é o problema
                    self.vel_max = 1
                else:
                    self.vel_max = -1
            else:
                self.vel = 0
                self.parada = False