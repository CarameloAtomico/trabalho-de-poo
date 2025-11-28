import pygame

class Button(pygame.Rect):
    def __init__(self, x, y, length, width, cor, controller):
        super().__init__(x, y, length, width)
        self.cor = cor
        self.controller = controller
        
    def press(self):
        pass