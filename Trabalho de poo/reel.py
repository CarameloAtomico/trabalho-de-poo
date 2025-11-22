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

        self.duracao_giro = 2200
        self.duracao_parada = 1200

        vals = ["A", "B", "C", "D", "E", "F", "G"]

        for i in range(5):
            val = random.choice(vals)
            s = Symbol(self.x, 200+75*i, 75, 75, val, self)
            self.symbols.append(s)

    def atualizar(self, tempo_atual):
        if self.espera:
            return
        
        if tempo_atual >= self.tempo_inicio + self.delay:
            for s in self.symbols:
                s.vel_max = 5

        tempo_passado = tempo_atual - (self.tempo_inicio + self.delay)

        if not (tempo_passado < self.duracao_giro or tempo_passado < self.duracao_giro + self.duracao_parada):
            for s in self.symbols:
                s.vel_max = 0
                s.vel = 0
                self.espera = True
            #criando uma nova lista, odenada por y dos simbolos
            #O sinal parada é acionado
            #Talvez o erro esteja aqui, mas é improvavel
            sym_y = sorted(self.symbols, key=lambda symbol: symbol.y)
            for i in range(5):
                sym_y[i].pos_parada = 200+75*i
                sym_y[i].parada = True
            return

        for s in self.symbols:
            s.roll()