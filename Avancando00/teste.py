from abc import ABC #Abstract Base Classes

from collections.abc import MutableSequence

class Playlist(MutableSequence):
    pass

filmes = Playlist()