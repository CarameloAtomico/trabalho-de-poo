import pygame
from button import Button

class B_Mais(Button):
    def __init__(self, controller, dinheiro):
        super().__init__(770, 700, 75, 75, (0, 255, 0), controller)
        self.dinheiro = dinheiro

    def press(self):
        if not self.controller.botoes_ativos:
            return

        self.dinheiro.aumentar_aposta()
        print("Nova aposta: ", self.dinheiro.get_aposta())