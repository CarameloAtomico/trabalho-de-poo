import pygame
from button import Button
class B_Menos(Button):
    def __init__(self):
        super().__init__(0, 600, 75, 75, (0, 255, 0))
        
    def press(self):
        print("Reduzir a aposta")