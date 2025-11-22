#crea una classe Persona con attributo nome e metodo presentati
#Poi crea una sottoclasse studente che aggiunge l'attributo corso
#infine, rendi l'attributo privato e permetti di leggerlo solo tramite un metodo dedicato

class Persona():
    def __init__(self, nome, persona):
        self.nome = nome
        self.persona = persona

    def presentati(self):
        return f"Ciao mi chiamo {self.nome}"
    

class Studente():
    def __init__(self, corso):
        self.corso = corso;


persona = Persona("Marian", Studente('Python'))

print(f"Ciao mi chiamo {persona.nome} e frequento il corso di { persona.persona.corso }")