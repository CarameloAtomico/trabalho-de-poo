class Money:
    def __init__(self):
        self.saldo = 50
        self.aposta = 5

    def get_saldo(self):
        return self.saldo
    
    def get_aposta(self):
        return self.aposta

    def aumentar_aposta(self):
        if self.aposta + 5 <= self.saldo:
            self.aposta += 5

    def reduzir_aposta(self, ):
        if self.aposta - 5 >= 5:
            self.aposta -= 5

    # Não sei se esta função seria feita aqui ou em algum outro lugar
    def apostar(self):
        pass