class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    Renzo = Pessoa(nome='Renzo')
    Luciano = Pessoa(Renzo, nome='Luciano')
    print(Pessoa.cumprimentar(Luciano))
    print(id(Luciano))
    print(Luciano.cumprimentar())
    print(Luciano.nome)
    print(Luciano.idade)
    for filho in Luciano.filhos:
        print(filho.nome)