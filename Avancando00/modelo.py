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

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._curtir} Curtidas"

class Filmes(Programas):
    def __init__(self, nome,ano,duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} Minutos - {self._curtir} Curtidas"

class Series(Programas):
    def __init__(self, nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} - {self._curtir} Curtidas"

class Playlist:
    def __init__(self, nomePl, elementos):
        self.nomePl = nomePl
        self.elementos = elementos

    def tamanho(self):
        return len(self.programas)

#Series
The_Boys = Series("The Boys", 2019, 5)
Supernatural = Series("Supernatural", 2005, 15)


#Filmes
A_Odisseia = Filmes("A Odisseia", 2026, 173)
Homem_Aranha = Filmes("Homen-Aranha", 2002, 121)


#Curtidas
The_Boys.curtida()
The_Boys.curtida()
The_Boys.curtida()
The_Boys.curtida()
The_Boys.curtida()
The_Boys.curtida()
The_Boys.curtida()
A_Odisseia.curtida()
A_Odisseia.curtida()
A_Odisseia.curtida()
A_Odisseia.curtida()
A_Odisseia.curtida()
A_Odisseia.curtida()
Supernatural.curtida()
Supernatural.curtida()
Supernatural.curtida()
Supernatural.curtida()
Supernatural.curtida()
Supernatural.curtida()
Supernatural.curtida()
Supernatural.curtida()
Homem_Aranha.curtida()
Homem_Aranha.curtida()
Homem_Aranha.curtida()
Homem_Aranha.curtida()
Homem_Aranha.curtida()
Homem_Aranha.curtida()

filmes_series = [A_Odisseia, Homem_Aranha, The_Boys, Supernatural]
plFim_de_semana = Playlist("Fim de Semana", filmes_series)

for programas in plFim_de_semana.elementos:
    print(programas)

#nomePl = Nome da Playlist