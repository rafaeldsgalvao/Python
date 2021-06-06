#Projeto3 Chute o numero
#Nesse projeto o sistema irá informar ao usuario o numero para mais ou menos, até que o usuario acerte o numero.

import random

class ChuteONumero:
    def __init__ (self):
        self.Valor_aleatorio = 0
        self.Valor_minimo = 1
        self.Valor_maximo = 1000
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.Valor_aleatorio:
                print('Chute um valor mais Baixo!')
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) < self.Valor_aleatorio:
                print('Chute um valor mais Alto!')
                self.PedirValorAleatorio()
            if int(self.valor_do_chute) == self.Valor_aleatorio:
                self.tentar_novamente = False
            print('PARABÉNS VOCÊ ACERTOU ! !')

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um numero: ')

    def GerarNumeroAleatorio(self):
        self.Valor_aleatorio = random.randint(self.Valor_minimo, self.Valor_maximo)

chute = ChuteONumero()
chute.Iniciar()