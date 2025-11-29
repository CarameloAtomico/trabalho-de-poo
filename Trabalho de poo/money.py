import pygame
class Money:
    def __init__(self):
        self.saldo = 50
        self.aposta = 0
        self.fnt = pygame.font.SysFont('arial', 35)
        self.fnta = pygame.font.SysFont('arial', 50)
        self.fnt_c = (255, 255, 0)

    def get_saldo(self):
        return self.saldo
    
    def get_aposta(self):
        return self.aposta

    def aumentar_aposta(self):
        if self.saldo >= 5:
            self.aposta += 5
            self.saldo -= 5

    def reduzir_aposta(self, ):
        if self.aposta > 0:
            self.aposta -= 5
            self.saldo += 5
    
    def show_saldo(self):
        t_saldo = self.fnt.render(str(self.saldo), True, self.fnt_c)
        r_saldo = t_saldo.get_rect(center=(650, 850))
        return [t_saldo, r_saldo]
    
    def show_aposta(self):
        t_aposta = self.fnta.render(str(self.aposta), True, self.fnt_c)
        r_aposta = t_aposta.get_rect(center=(600, 650))
        return [t_aposta, r_aposta]