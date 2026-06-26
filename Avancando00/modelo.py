#Filmes e Séries tem as seguintes características:

#Filme: Nome, ano, duração, curtir
#Séries: Nome, ano, temporadas, curtir

class Filmes:
    def __init__(self, nome,ano,duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__curtir = 0

    @property
    def valor_curtir(self):
        return self.__curtir

    @property
    def valor_nome(self):
        return self.__nome

    def curtida(self):
        self.curtir += 1

class Series:
    def __init__(self, nome,ano,temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__curtir = 0
    
    @property
    def valor_curtir(self):
        return self.__curtir

    @property
    def valor_nome(self):
        return self.__nome

    def curtida(self):
        self.curtir += 1


The_Boys = Series("The Boys", 2019, 5)
The_Boys.curtida()
print(f"Nome: {The_Boys.nome} - Ano: {The_Boys.ano} - Temporadas: {The_Boys.temporadas} - Curtidas: {The_Boys.curtir}")

Rei_Leao= Filmes("Rei Leão", 1994, 94)
Rei_Leao.curtida()
print(f"Nome: {Rei_Leao.nome} - Ano: {Rei_Leao.ano} - Duração: {Rei_Leao.duracao} - Curtidas: {Rei_Leao.curtir}")
