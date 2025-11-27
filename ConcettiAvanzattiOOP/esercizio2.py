# esempio di classe astratta

from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def verso(self):
        pass

class Cane(Animale):
    def verso(self):
        print('Bau')

class Gatto(Animale):
    def verso(self):
        print('Miao')

c  = Cane()
c.verso();

g = Gatto();
g.verso()