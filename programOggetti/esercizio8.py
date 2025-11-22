# Crea una classe Animale con attributo nome e metodo verso
# poi crea due classi derivate
# Cane verso stampa "bau"
# Gatto verso stampa "miao"
# Crea un oggetto di ciascuna classe e poi chiama il metodo verso
# Questo esercizio mostra chiaramente come ereditare e sovrascrivere i metodi

class Animale():
    def __init__(self, nome):
        self.nome = nome

    def verso(self):
        return print("Verso generico")

class Cane(Animale):
    def verso(self):
        return print("Bau")

class Gatto(Animale):
    def verso(self):
        return print("Miao")

a = Cane("Fido")
a.verso()

b = Gatto("Palla di neve")
b.verso()