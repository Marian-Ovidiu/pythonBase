# Creea una classe forma con metodo areaa():
# Crea due classi derivate:
# rettangolo => qrea= base * altezza
# cerchio => area = p grecco * r^2
# Crea una lista di forme e stampaa l'area di ciascuna usando lo stesso metodo area
import math

class Forma:
    def area():
        pass

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    def area(self):
        return self.base * self.altezza
    
class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2
    
r = Rettangolo(5, 10)
print(r.area())