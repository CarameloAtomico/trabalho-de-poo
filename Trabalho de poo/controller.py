import pygame
from collections import Counter

class Controller:
    def __init__(self, money):
        self.botoes_ativos = True
        self.tempo_espera = 0
        self.cooldown = 5000
        self.money = money
        self.result = []
        self.paylines = [
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2],
            [0, 1, 2, 1, 0],
            [2, 1, 0, 1, 2],
            [0, 0, 1, 0, 0],
            [2, 2, 1, 2, 2],
            [1, 2, 2, 2, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1]
        ]
        self.payvalues = {
            "symbol" : {
                "A": { "3": 50, "4": 200, "5": 1250 },
                "B": { "3": 25, "4": 60, "5": 600 },
                "C": { "3": 10, "4": 25, "5": 300 },
                "D": { "3": 8, "4": 20, "5": 250 },
                "E": { "3": 7, "4": 15, "5": 200 },
                "F": { "3": 5, "4": 10, "5": 125 },
                "G": { "3": 5, "4": 10, "5": 125 }
                }}
        

    def desativar_botoes(self):
        self.botoes_ativos = False
        self.tempo_espera = pygame.time.get_ticks() + self.cooldown
        self.result = []
    
    # Verifica se passou tempo o suficiente para que os botões sejam ativados novamente
    def atualizar(self):
        if not self.botoes_ativos:
            if self.tempo_espera < pygame.time.get_ticks():
                self.botoes_ativos = True
                #Transpondo a matriz
                matriz = [[], [], []]
                for i in range(5):
                        for j in range(1, 4):
                            matriz[j-1].append(self.result[i][j])
                #conferindo linhas de pagamento, uma por uma 
                pays = []
                for i in self.paylines:
                    line = []
                    for j in range(5):
                        payline = i[j]
                        line.append(matriz[payline][j])
                        
                    #número de simbolos seguidos
                    pnt = 0
                    #conferindo sequências de simbolos
                    #pela direita
                    for k in range(1,5):
                        if line[k] == line[k-1]:
                            pnt += 1
                            if pnt >= 3:
                                n = pnt
                        else:
                            pnt = 1
                    
                    #pela esquerda *Não funciona*
                    for k in range(4):
                        pnt = 1
                        for k in range(0,4):
                            if line[k] == line[k+1]:
                                pnt += 1
                                if pnt >= 3:
                                    n = pnt
                            else:
                                pnt = 1
                    
                    #Se houverem mais de três seguidos, o triguinho vai pagar $$$
                    if pnt >= 3:
                        cont = Counter(line)
                        val = cont.most_common(1)[0][0]
                        pays.append({"val":val, "n":str(n)})
                        
                m = int(self.money.aposta/5)
                for i in pays:
                    #Calculando o valor da aposta
                    self.money.saldo += self.payvalues["symbol"][i["val"]][i["n"]]*m
                
                self.money.aposta = 0
                
                    
                    
                        
