import pygame
from button import Button

class B_Spin(Button):
    def __init__(self, controller, reels, money):
        super().__init__(485, 700, 225, 75, (0, 255, 0))
        self.controller = controller
        self.reels = reels
        self.money = money
        self.fnta = pygame.font.SysFont('arial', 50)

    def show_text(self):
        t_spin = self.fnta.render("SPIN", False, (255, 255, 0))
        r_spin = t_spin.get_rect(center=(600, 738))
        return [t_spin, r_spin]
                
    def press(self):
        if self.controller.money.aposta == 0:
            return
        
        if not self.controller.botoes_ativos:
            return

        t = pygame.time.get_ticks()
        self.money.saldo -= self.money.aposta

        # Realiza o giro dos rodilhos
        for r in self.reels:
            r.tempo_inicio = t
            r.espera = False
            r.result = []
    
        self.controller.desativar_botoes()
        
