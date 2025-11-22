# Crea una classe automobile con:
class Auto():
    # variabile di classe ruote = 4
    ruote = 4;

    # variabile di istanza modello
    def __init__(self, modello):
        self.modello = modello

    def __str__(self):
        return f"Classe istanziata con modello {self.modello} e con {self.ruote} ruote"
    
# Crea due automobili con modelli diversi e stampa il numero di ruote e i modelli
a1 = Auto("Fiat")
a2 = Auto("Seat")

print(a1)
print(a2)