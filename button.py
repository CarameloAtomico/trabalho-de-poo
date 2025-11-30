import pygame

class Button(pygame.Rect):
    def __init__(self, x, y, length, width, cor):
        super().__init__(x, y, length, width)
        self.cor = cor
        
    def press(self):
        pass