# decoratori
# @staticmethod, non riceve self
# @classmethod, metodo legato alla classe, riceve cls come parametro 
# @property, permette di trattare un metodo come se fosse un attributo
# @nome.setter, permette di definire come modificare un attributo controllato

#es con static method:

class Matematica:
    @staticmethod
    def somma(a, b):
        return a + b
    
print(Matematica.somma(3,5))

#es con @classmethod e @nome.setter:

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome  # usa il setter
        self.eta = eta

    @classmethod
    def da_stringa(cls, stringa):
        nome, eta = stringa.split('-')
        return cls(nome, int(eta))

    @property
    def nome(self):
        return self._nome

    @nome.setter #il setter non funziona senza il @property e viceversa
    def nome(self, nuovo_nome):
        if nuovo_nome.isalpha():
            self._nome = nuovo_nome
        else:
            print("Nome non valido")

# riassunto
#lui va nella classMethod che setta il nome e l'eta attraverso il return 
# cls(nome, int(eta)) richiamando cosi attraverso cls l'init. 
# Mentre l'altro metodo è p = Persona('Luca', '27') che passa per l'init,
# dove self.nome chiama @nome.setter

p = Persona.da_stringa("Marian-26")
print(p.nome, p.eta)
p = Persona('Luca', '27')
print(p.nome, p.eta)

#es con @property:
class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    
    @property
    def area(self):
        return self.base * self.altezza
    
r = Rettangolo(5, 10)
print(r.area)

