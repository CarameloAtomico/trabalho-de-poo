import pygame
from button import Button

class B_Spin(Button):
    def __init__(self, controller, reels):
        super().__init__(485, 700, 225, 75, (0, 255, 0), controller)
        self.reels = reels
        
    def press(self):
        if not self.controller.botoes_ativos:
            return

        t = pygame.time.get_ticks()

        # Realiza o giro dos rodilhos
        for r in self.reels:
            r.tempo_inicio = t
            r.espera = False
    
        self.controller.desativar_botoes()