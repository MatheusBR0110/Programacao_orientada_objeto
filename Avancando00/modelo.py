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

    def imprime(self):
        print(f"{self._nome} - {self.ano} - {self._curtir} Curtidas")

class Filmes(Programas):
    def __init__(self, nome,ano,duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f"{self._nome} - {self.ano} - {self.duracao} Minutos - {self._curtir} Curtidas")

class Series(Programas):
    def __init__(self, nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f"{self._nome} - {self.ano} - {self.temporadas} - {self._curtir} Curtidas")

The_Boys = Series("The Boys", 2019, 5)
The_Boys.curtida()

A_Odisseia= Filmes("A Odisseia", 2026, 173)
A_Odisseia.curtida()

filmes_series = [The_Boys, A_Odisseia]

for programas in filmes_series:
    programas.imprime()