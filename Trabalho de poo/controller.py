import pygame

class Controller:
    def __init__(self):
        self.botoes_ativos = True
        self.tempo_espera = 0
        self.cooldown = 5000

    def desativar_botoes(self):
        self.botoes_ativos = False
        self.tempo_espera = pygame.time.get_ticks() + self.cooldown
    
    # Verifica se passou tempo o suficiente para que os botões sejam ativados novamente
    def atualizar(self):
        if not self.botoes_ativos:
            if self.tempo_espera < pygame.time.get_ticks():
                self.botoes_ativos = True