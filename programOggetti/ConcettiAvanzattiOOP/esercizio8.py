# Costruire un piccolo sistema aper gestire figure geometriche
# Una classe astratta Forma con due metodi astratti
# area () perimetro()
# Due figure concerete
# Rettangolo Cerchio

# Funzionalità extra:
# @property per ottenere informazioni derivate (diametro del cerchio)
# Overloading di + per combinare due figure in una terza figura che rapprensenti la loro area totale
# Overloading di  __eq__ per confrontare figure in base all'area
# Uso poliformismo con una lista di figure diverse

from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __eq__(self, altra):
        return math.isclose(self.area(), altra.area())
    
    def __str__(self):
        return f"{self.__class__.__name__} con area {self.area():.2f} e perimetro {self.perimetro():.2f}"


class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)


class Cerchio(Forma):
    def __init__(self, raggio):
        self._raggio = raggio

    @property
    def raggio(self):
        return self._raggio
    
    @property
    def diametro(self):
        return self._raggio * 2

    def area(self):
        return math.pi * (self._raggio ** 2)

    def perimetro(self):
        return 2 * math.pi * self._raggio


class AreaTotale(Forma):
    def __init__(self, f1, f2):
        self._f1 = f1
        self._f2 = f2

    def area(self):
        return self._f1.area() + self._f2.area()
    
    def perimetro(self):
        # perimetro "totale" come somma dei perimetri delle due figure
        return self._f1.perimetro() + self._f2.perimetro()
    
    def __str__(self):
        return (
            f"AreaTotale di {self._f1.__class__.__name__} + {self._f2.__class__.__name__} "
            f"con area {self.area():.2f} e perimetro {self.perimetro():.2f}"
        )


# Overloading di +
Forma.__add__ = lambda self, altra: AreaTotale(self, altra)


# Info di base
rett = Rettangolo(4, 5)
circ = Cerchio(3)

print(f"Figure iniziali:\n{rett}\n{circ}\n")

# Poliformismo: lista con oggetti di classi diverse
print("Poliformismo")
figure = [rett, circ]
for fig in figure:  
    print(fig)

# Contfronto tra figure usando ==
print("\nConfronto tra figure:")
print(f"Rettangolo e Cerchio hanno la stessa area? {'Sì' if rett == circ else 'No'}")

# Combinazione di figure usando +
print("\nCombinazione di figure:")
area_totale = rett + circ
print(area_totale)
