import pygame
from button import Button

class B_Info(Button):
    def __init__(self, controller):
        super().__init__(225, 50, 50, 50, (255, 255, 255))
        self.sprite = pygame.image.load('Sprites/Info.png')
        self.controller = controller
        self.info_showing = False


    def get_sprite(self):
        return self.sprite

    def press(self):
        return
        if not self.info_showing:
            self.info_showing = True
        else:
            pass