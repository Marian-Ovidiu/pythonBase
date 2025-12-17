"""
Crea una classe Appunti che salvi in un file ogni riga scritta dall'utente.
Aggiungi un metodo mostra() che stampi il contenuto del file.
Estendi la classe con un metodo cancella che svuoti il file.

"""

class Appunti:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def salva(self, testo):
        with open(self.nome_file, "a") as file:
            file.write(testo + "\n")

    def mostra(self):
        with open(self.nome_file, "r") as file:
            contenuto = file.read()
            print("Contenuto del diario:")
            print(contenuto)

    def cancella(self):
        with open(self.nome_file, "w") as file:
            file.write("")

# Esempio di utilizzo
appunti = Appunti("appunti.txt")
while True:
    riga = input("Scrivi una riga da salvare negli appunti (o 'esci' per terminare): ")
    if riga.lower() == 'esci':
        break
    appunti.salva(riga)

appunti.mostra()
# appunti.cancella()
# print("Appunti cancellati.")
appunti.mostra()