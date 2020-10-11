# -*- coding: utf-8 -*-
class Pessoa:
    
    def __init__(self, nome=None, idade=36):
        # self.nome é o atributo da classe por isso self.
        # ja nome é o parametro que será atribuido ao atributo da classe
       self.nome = nome
       self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == "__main__":
    p = Pessoa('Pai')
    print(p.cumprimentar())
    print(id(p))
    print(p.nome)
    p.nome = 'Plinio'
    print(p.nome)
    print(p.idade)