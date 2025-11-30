import pygame
from button import Button

class B_Info(Button):
    def __init__(self):
        super().__init__(375, 50, 50, 50, (255, 255, 255))
        self.sprite = pygame.image.load('Sprites/Info.png')
        self.lines = pygame.image.load('Sprites/Cabecalho.png')
        self.info_showing = False


    def get_sprite(self):
        return self.sprite

    def press(self):
        if not self.info_showing:
            self.info_showing = True
        else:
            self.info_showing = False