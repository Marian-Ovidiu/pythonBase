""" Crea una classe Studente che chiede all'utente nome ed età e abbia un metodoto presentati().
Aggiungi a Studente un metodoto __str__ che restituisca una stringa leggibile.
Crea una classe Diario che salvi su file un messaggio passato dall'utente.
Aggiungi un metodo che legga dal file e stampi i messaggi. """

class Studente:
    def __init__(self):
        self.nome = input("Inserisci il nome dello studente: ")
        self.eta = input("Inserisci l'età dello studente: ")

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

    def __str__(self):
        return f"Studente(nome={self.nome}, età={self.eta})"
    
class Diario:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def salva_messaggio(self, messaggio):
        with open(self.nome_file, 'a') as file:
            file.write(messaggio + '\n')

    def leggi_messaggi(self):
        with open(self.nome_file, 'r') as file:
            contenuto = file.read()
            print("Messaggi nel diario:")
            print(contenuto)

# Esempio di utilizzo
studente = Studente()
studente.presentati()
print(studente)

diario = Diario("diario.txt")
messaggio = input("Inserisci un messaggio da salvare nel diario: ")
diario.salva_messaggio(messaggio)
diario.leggi_messaggi()