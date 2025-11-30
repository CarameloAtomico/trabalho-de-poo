import pygame
from button import Button

class B_Mais(Button):
    def __init__(self, controller, dinheiro):
        super().__init__(920, 700, 75, 75, (0, 255, 0))
        self.controller = controller
        self.dinheiro = dinheiro
        self.fnta = pygame.font.SysFont('arial', 70)


    def show_text(self):
        t_mais = self.fnta.render("+", True, (255, 255, 0))
        r_mais = t_mais.get_rect(center=(958, 737))
        return [t_mais, r_mais]

    def press(self):
        if not self.controller.botoes_ativos:
            return

        self.dinheiro.aumentar_aposta()