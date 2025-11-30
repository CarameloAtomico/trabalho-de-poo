import pygame
from collections import Counter

class Money:
    def __init__(self):
        self.saldo = 50
        self.aposta = 0
        self.fnt = pygame.font.SysFont('arial', 35)
        self.fnta = pygame.font.SysFont('arial', 50)
        self.fnt_c = (255, 255, 0)
        self.result = []
        self.paylines = [
            # 1, 2, 3
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2],
            # 4, 5
            [0, 1, 2, 1, 0],
            [2, 1, 0, 1, 2],
            # 6, 7
            [0, 0, 1, 0, 0],
            [2, 2, 1, 2, 2],
            # 8, 9
            [1, 2, 2, 2, 1],
            [1, 0, 0, 0, 1],
            # 10
            [1, 0, 1, 0, 1],
        ]
        self.payvalues = {
            "symbol" : {
                "A": { "3": 50, "4": 200, "5": 1250 },
                "B": { "3": 25, "4": 60, "5": 600 },
                "C": { "3": 10, "4": 25, "5": 300 },
                "D": { "3": 8, "4": 20, "5": 250 }
                }}
    
    def set_saldo(self, saldo):
        self.saldo = saldo
    
    def set_aposta(self, aposta):
        self.aposta = aposta

    def aumentar_aposta(self):
        if self.saldo > self.aposta:
            self.aposta += 5

    def reduzir_aposta(self):
        if self.aposta > 0:
            self.aposta -= 5
    
    def show_saldo(self):
        t_saldo = self.fnt.render(str(str(self.saldo)), True, self.fnt_c)
        r_saldo = t_saldo.get_rect(center=(750, 860))
        return [t_saldo, r_saldo]
    
    def show_aposta(self):
        t_aposta = self.fnta.render(str(self.aposta), True, self.fnt_c)
        r_aposta = t_aposta.get_rect(center=(750, 630))
        return [t_aposta, r_aposta]
    
    # Faz a verificação de símbolos conforme paylines
    def verificar_simbolos(self, line):
        for a in range(3):
            simbolo = line[a]
            n = 0

            for b in range(a, 5):
                if line[b] == simbolo:
                    n += 1
                else:
                    break
        
            if n >= 3:
                print(line, n)
                return n
        print(line, 0)
        return 0
    
    def processar_aposta(self):
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
                    n = self.verificar_simbolos(line)
                    
                    #Se houverem três ou mais seguidos, o triguinho vai pagar $$$
                    if n >= 3:
                        cont = Counter(line)
                        val = cont.most_common(1)[0][0]
                        pays.append({"val":val, "n":str(n)})
                        
                m = int(self.aposta/5)
                for i in pays:
                    #Calculando o valor da aposta
                    self.saldo += self.payvalues["symbol"][i["val"]][i["n"]]*m
                

                self.aposta = 0
