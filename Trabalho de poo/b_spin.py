import pygame
from button import Button
class B_Spin(Button):
    def __init__(self):
        super().__init__(275, 600, 225, 75, (0, 255, 0))
        
    def press(self):
        print("Botar pra rodar")