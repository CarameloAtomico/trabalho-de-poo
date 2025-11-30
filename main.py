import pygame
from symbol import Symbol
from reel import Reel
from button import Button
from b_info import B_Info
from b_spin import B_Spin
from b_menos import B_Menos
from b_mais import B_Mais
from money import Money
from controller import Controller

#atualização gráfica
def draw_game_init():
    screen.fill((100,100,100))
    #desenhar fundo branco
    pygame.draw.rect(screen, (255,255,255), (bx, 50, 750, 650))
    #desenhar simbolos
    for r in symbols:
        for symbol in r:
            screen.blit(symbol.getspr(), (symbol.x, symbol.y))
    #barreira superior
    pygame.draw.rect(screen, (55,55,55), (bx, 50, 750, 130))
    #barreira inferior
    pygame.draw.rect(screen, (55,55,55), (bx, 570, 750, 330))
    #saldo
    screen.blit(money.show_saldo()[0], money.show_saldo()[1])
    screen.blit(texto, texto_rect)
    #aposta
    screen.blit(money.show_aposta()[0], money.show_aposta()[1])
    #desenha os botões
    for button in buttons:
        pygame.draw.rect(screen, button.cor, button)
    screen.blit(info.get_sprite(), (info.x, info.y))
    screen.blit(b_mais.show_text()[0], b_mais.show_text()[1])
    screen.blit(b_menos.show_text()[0], b_menos.show_text()[1])
    screen.blit(b_spin.show_text()[0], b_spin.show_text()[1])
    
    if info.info_showing == True:
        screen.blit(info.lines, (100, 600))

#gerando os rodilhos
def rodilhos():
    for i in range(5):
        reels.append(Reel(bx+150*i, 150*i, controller))

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
screen_size = (1500,900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Trabalho de POO")
bx = 375
money = Money()
controller = Controller(money)
reels = []
rodilhos()
symbols = []
simbolos()
buttons = []
info = B_Info()
b_mais = B_Mais(controller, money)
b_menos = B_Menos(controller, money)
b_spin = B_Spin(controller, reels, money)
buttons.append(info)
buttons.append(b_spin)
buttons.append(b_menos)
buttons.append(b_mais)


fnt = pygame.font.SysFont('arial', 35)
fnt_c = (255, 255, 0)
texto = fnt.render("Saldo:", True, fnt_c)
texto_rect = texto.get_rect(center=(750, 810))



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
    controller.atualizar()
    pygame.display.flip()
pygame.quit()