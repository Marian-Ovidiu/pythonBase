# Crea una classe Studente con attributi nome ed età
class Studente():
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    # aggiungi alla classe Studente un metodo presentati che stampi un messaggio con nome ed età
    def presentati(self):
        print(f"Ciao sono {self.nome} e ho {self.eta} anni")        

# istanzia due studenti diversi e stampane i dati
s1 = Studente("Marian", 26)
s2 = Studente("Andrea", 21)

print(f"{s1.nome} {s1.eta}")
print(f"{s2.nome} {s2.eta}")

s1.presentati()

# Prova ad aggiunggere un attributo al volo a uno studente ad esempio corso, e stampalo
s2.corso = "Python"
print(s2.corso)