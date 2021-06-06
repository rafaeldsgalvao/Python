#simulador de dado
#Simular o uso de um dado, gerando um valor aleatorio de 1 a 1000
import random
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Print, PrintClose  

class SimuladorDeDado:
    def __init__(self):
        self.Valor_minimo = 1
        self.Valor_maximo = 1000
        self.mensagem = 'Você gostaria de gerar um novo valor?'
        #layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]

    def Iniciar(self):
        #janela
        self.Janela = sg.Window('simualdor de dado', layout = self.layout)
        #Ler os valores da tela
        self.eventos, self.valores = self.Janela.Read()
        #Fazer algo com os valores
        try:
            if self.eventos == 'sim' or self.eventos =='s':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                PrintClose('Agradeçemos sua participação')
            else:
                Print('Por favor informe sim(s) ou Não(n)')
        except:
            Print ('Ocorreu um erro com a aplicação')
    
    def GerarValorDoDado(self):
        print(random.randint(self.Valor_minimo,self.Valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()