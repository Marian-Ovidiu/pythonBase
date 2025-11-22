#Crea una classe Libro con attributi titolo e autore
# Nel __init__, inizializza i valori
# Nel __str__, restituisci una frase tipo: "Titolo x, Autore Y"
# 
# Esempio:
# libro = Libro("1984", "George Orwell") 
# print(libro)


class Libro():
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}"

libro = Libro("1984", "George Orwell")

print(libro)