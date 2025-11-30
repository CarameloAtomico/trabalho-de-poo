import pygame
from button import Button

class B_Menos(Button):
    def __init__(self, controller, dinheiro):
        super().__init__(350, 700, 75, 75, (0, 255, 0))
        self.controller = controller
        self.dinheiro = dinheiro
        self.fnta = pygame.font.SysFont('arial', 80)
    
    def show_text(self):
        t_menos = self.fnta.render("-", True, (255, 255, 0))
        r_menos = t_menos.get_rect(center=(388, 730))
        return [t_menos, r_menos]
        
    def press(self):
        if not self.controller.botoes_ativos:
            return

        self.dinheiro.reduzir_aposta()
