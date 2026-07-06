#Filmes e Séries tem as seguintes características:

#Filme: Nome, ano, duração, curtir
#Séries: Nome, ano, temporadas, curtir

#Classe mãe/principal
#Super Classe
class Programas:
    def __init__(self, nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtir = 0
    
    @property
    def valor_curtir(self):
        return self._curtir

    @property
    def valor_nome(self):
        return self._nome

    def curtida(self):
        self._curtir += 1

    @property
    def valor_curtir(self):
        return self._curtir

    @property
    def valor_nome(self):
        return self._nome

    def curtida(self):
        self._curtir += 1

class Filmes(Programas):
    def __init__(self, nome,ano,duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Series(Programas):
    def __init__(self, nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

The_Boys = Series("The Boys", 2019, 5)
The_Boys.curtida()

Rei_Leao= Filmes("Rei Leão", 1994, 94)
Rei_Leao.curtida()

filmes_series = [The_Boys, Rei_Leao]

for programas in filmes_series:
    detalhe = programas.duracao if hasattr(programas, 'duracao') else programas.temporadas
    print(f"{programas._nome} - {programas.ano} - {detalhe}")
