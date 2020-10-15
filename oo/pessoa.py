# -*- coding: utf-8 -*-
class Pessoa:
    # olhos é um atributo da classe Pessoa, como os atributos estaticos no Java
    # são atributos que acompanham as instancias da classe
    olhos = 2
    
    def __init__(self, *filhos, nome=None, idade=36):
        # argumentos com 1 asterisco '*' na frente significa que ele não é obrigatorio e também poderá ter mais que 1
        # self.nome é o atributo da classe por isso self.
        # ja nome é o parametro que será atribuido ao atributo da classe
       self.nome = nome
       self.idade = idade
       self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        # metodo estatico não recebe seld (o objeto da classe)
        # porque é um metodo da classe e por isso estatico
        # pode ser acessado pelas instancias da classe também
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == "__main__":
    plinio = Homem(nome='Plinio')
    rafael = Homem(nome='Rafael')
    adair = Pessoa(rafael, plinio, nome='Adair')
    print(adair.cumprimentar())
    print(id(adair))
    print(adair.nome)
    print(adair.idade)
    print(adair.filhos)

    for filho in adair.filhos:
        print(f'O nome dos Filhos de {adair.nome} é {filho.nome}')

    # este atributo sobrenome foi criado em tempo de execução
    # veja que ele não está no metodo construtor __init__
    adair.sobrenome = 'Correa'

    # del serve para remover atributos em tempo de execução
    # mesmo os que foram definido no metodo contrutor __init__
    del adair.filhos 
    
    print(adair.__dict__) # __dict__ apresenta todos os atributos do objeto em um dicionario
    print(plinio.__dict__)
    print(Pessoa.olhos) # acessando atributo da classe ou atributo default
    print(plinio.olhos) # acessando atributo da classe ou atributo default pela instancia da classe

    print(id(Pessoa.olhos), id(plinio.olhos))
    # Acessando o metodo da classe com a classe Pessoa
    # Acessando o metodo da classe com a instancia de Pessoa
    print(Pessoa.metodo_estatico(), plinio.metodo_estatico())

    # Acessando atributos de classe com a classe Pessoa por metodos de classe
    # Acessando atributos de classe com a instancia de Pessoa por metodos de classe
    print(Pessoa.nome_e_atributos_de_classe(), plinio.nome_e_atributos_de_classe())
    