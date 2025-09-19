"""
Métodos e funções em Python
Método: função que pertence a um objeto
Função: retorna um valor
"""

#metodos são declarados usando def

"""
#ex: função para somar
def soma(a, b):
    return a + b
#nesse caso, ele acaba sendo uma função, pois retorna um valor

print(soma(1, 2))#retorna 3

"""


#classes também podem ter métodos. Elas agrupam

class Carro:
    def __init__(self):
        self.parado = True
        print("Carro parado")

    def ligarCarro(self):
        self.parado = False
        print("Carro ligado")


# meuCarro = Carro()
# meuCarro.ligarCarro()