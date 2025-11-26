import pygame
from symbol import Symbol
from reel import Reel
from button import Button
from b_spin import B_Spin
from b_menos import B_Menos
from b_mais import B_Mais

#atualização gráfica
def draw_game_init():
    screen.fill((100,100,100))
    #desenhar fundo branco
    pygame.draw.rect(screen, (255,255,255), (225, 50, 750, 650))
    #desenhar simbolos
    for r in symbols:
        for symbol in r:
            screen.blit(symbol.getspr(), (symbol.x, symbol.y))
    #barreira superior
    pygame.draw.rect(screen, (55,55,55), (225, 50, 750, 130))
    #barreira inferior
    pygame.draw.rect(screen, (55,55,55), (225, 570, 750, 330))
    
    for button in buttons:
        pygame.draw.rect(screen, button.cor, button)

#gerando os rodilhos
def rodilhos():
    for i in range(5):
        reels.append(Reel(225+150*i, 300*i))

#Catalogando simbolos
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
screen_size = (1200,900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Trabalho de POO")
reels = []
rodilhos()
symbols = []
simbolos()
buttons = []
buttons.append(B_Spin(reels))
buttons.append(B_Menos())
buttons.append(B_Mais())



#loop update
while not game_over:
    draw_game_init()
    tempo_atual = pygame.time.get_ticks()
    for r in reels:
        r.atualizar(tempo_atual)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.collidepoint(event.pos):
                    button.press()
    pygame.display.flip()
pygame.quit()