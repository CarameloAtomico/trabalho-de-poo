import pygame
from button import Button

class B_Mais(Button):
    def __init__(self):
        super().__init__(770, 700, 75, 75, (0, 255, 0))

    def press(self):
        print("Aumentar a aposta")