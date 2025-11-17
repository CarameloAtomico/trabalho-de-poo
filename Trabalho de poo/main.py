import pygame
from symbol import Symbol
from reel import Reel
from button import Button
from b_spin import B_Spin
from b_menos import B_Menos

#atualização gráfica
def draw_game_init():
    screen.fill((0,0,0))
    for button in buttons:
        pygame.draw.rect(screen, button.cor, button)
    for r in symbols:
        for symbol in r:
            pygame.draw.rect(screen, symbol.getcor(), symbol)

#gerando os rodilhos
def rodilhos():
    for i in range(5):
        reels.append(Reel(200+75*i))

def simbolos():
    for i in reels:
        l = []
        for j in i.symbols:
            l.append(j)
        symbols.append(l)

#movimento
def roll():
    for r in symbols:
        for symbol in r:
            symbol.roll()

#inicializando o jogo 
pygame.init()
game_over = False
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Trabalho de POO")
reels = []
rodilhos()
symbols = []
simbolos()
buttons = []
buttons.append(B_Spin())
buttons.append(B_Menos())
#buttons.append(B_Mais())



#loop update
while not game_over:
    draw_game_init()
    roll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.collidepoint(event.pos):
                    button.press()
    pygame.display.flip()
pygame.quit()