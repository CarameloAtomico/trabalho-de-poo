import pygame
import random 
from symbol import Symbol

class Reel:
    def __init__(self, x, delay):
        self.x = x
        self.delay = delay
        self.tempo_inicio = 0
        self.espera = True
        self.symbols = []

        self.duracao_giro = 4200
        self.duracao_parada = 1200

        vals = ["A", "B", "C", "D", "E", "F"]
        
        #cirando os simbolos
        for i in range(5):
            val = random.choice(vals)
            s = Symbol(self.x, 50+130*i, 75, 75, val, self)
            self.symbols.append(s)

    def atualizar(self, tempo_atual):
        for s in self.symbols:
            if self.espera and s.parada:
                s.roll()
        if self.espera:
            for s in self.symbols:
                if s.y == s.pos_parada and not s.parada:
                    s.vel_max = 0
            return

        #Enviando a velocidade máxima
        if tempo_atual >= self.tempo_inicio + self.delay:
            for s in self.symbols:
                s.vel_max = 32

        tempo_passado = tempo_atual - (self.tempo_inicio + self.delay)

        #Ao fim da duração do giro...
        if not (tempo_passado <= self.duracao_giro):
            for s in self.symbols:
                s.vel = 0
                self.espera = True
                
            sym_y = sorted(self.symbols, key=lambda symbol: symbol.y)
            for i in range(5):
                sym_y[i].pos_parada = 50+130*i
                sym_y[i].parada = True

        for s in self.symbols:
            s.roll()