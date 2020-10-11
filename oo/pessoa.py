# -*- coding: utf-8 -*-
class Pessoa:
    
    def __init__(self, *filhos, nome=None, idade=36):
        # argumentos com 1 asterisco '*' na frente significa que ele não é obrigatorio e também poderá ter mais que 1
        # self.nome é o atributo da classe por isso self.
        # ja nome é o parametro que será atribuido ao atributo da classe
       self.nome = nome
       self.idade = idade
       self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == "__main__":
    plinio = Pessoa(nome='Plinio')
    rafael = Pessoa(nome='Rafael')
    adair = Pessoa(rafael, plinio, nome='Adair')
    print(adair.cumprimentar())
    print(id(adair))
    print(adair.nome)
    print(adair.idade)
    print(adair.filhos)

    for filho in adair.filhos:
        print(f'O nome dos Filhos de {adair.nome} é {filho.nome}')
    