import pygame
from button import Button

class B_Spin(Button):
    def __init__(self, reels):
        super().__init__(485, 700, 225, 75, (0, 255, 0))
        self.reels = reels
        
    def press(self):
        t = pygame.time.get_ticks()
        for i, r in enumerate(self.reels):
            if r.espera == True:
                r.tempo_inicio = t
                r.espera = False
            else:
                break