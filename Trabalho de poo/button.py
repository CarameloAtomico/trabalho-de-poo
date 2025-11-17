import pygame
class Button(pygame.Rect):
    def __init__(self, x, y, length, width, cor):
        super().__init__(275, 600, 225, 75)
        self.cor = cor
        
    def press(self):
        print("Foi!!")