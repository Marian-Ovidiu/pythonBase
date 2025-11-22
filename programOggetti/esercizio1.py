#scrivere una classe Studente con attributi nome e corso, e un metodo 
#presentati() che stampa una frase di presentazione

class Studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

    def presentati(self):
         return f"Ciao mi chiamo {self.nome} e frequento il corso {self.corso}"
    

studente = Studente('Marian', 'Python from Hero to Zero')

print(studente.presentati())