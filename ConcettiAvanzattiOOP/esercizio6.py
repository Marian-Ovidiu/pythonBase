# Crea una classe Frazione che rappresenti una frazione con numeratore e denominatore
# Implementa i seguenti operatori:
# + (somma tra frazioni)
# == (ugualgianza tra frazioni, semplificando i valori)
# __str__ per stampare la frazione come "3/4"

class Frazione:
    def __init__(self, numeratore, denominatore):
        self.n = numeratore
        self.d = denominatore
        self._semplifica()

    def _mcd(self, a, b):
        # algoritmo per trovare il MCD
        while b != 0:
            a, b = b, a % b
        return a

    def _semplifica(self):
        # semplifica numeratore e denominatore
        m = abs(self._mcd(self.n, self.d))
        self.n //= m
        self.d //= m

    def __str__(self):
        # stampa la frazione come "n/d"
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        # formula somma frazioni: a/b + c/d = (ad + bc) / bd
        nuovo_n = self.n * other.d + other.n * self.d
        nuovo_d = self.d * other.d
        return Frazione(nuovo_n, nuovo_d)

    def __eq__(self, other):
        # due frazioni sono uguali se, una volta semplificate, hanno stessi valori
        return self.n == other.n and self.d == other.d

a = Frazione(1, 2)
b = Frazione(3, 4)
c = Frazione(2, 4)

print(a + b)      # 5/4
print(a == c)     # True
print(a)          # 1/2