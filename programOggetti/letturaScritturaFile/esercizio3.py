"""
Crea un file libri.csv con colonne: titolo, autore, anno.
Scrivi una classe GestoreLibri che legga il file e stampi i titoli.
Aggiungi un metodo che stampi solo i libri di un certo autore.

"""

import csv

class GestoreLibri:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def leggi_libri(self):
        try:
            with open(self.nome_file) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row['titolo'])
        except FileNotFoundError:
            print("File non trovato.")

    def leggi_libri_autore(self, autore):
        try:
            with open(self.nome_file) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['autore'] == autore:
                        print(row['titolo'])
        except FileNotFoundError:
            print("File non trovato.")

# Esempio di utilizzo
gestore = GestoreLibri("libri.csv")
print("Tutti i libri:")
gestore.leggi_libri()
print("\nLibri di George Orwell:")
gestore.leggi_libri_autore("George Orwell")