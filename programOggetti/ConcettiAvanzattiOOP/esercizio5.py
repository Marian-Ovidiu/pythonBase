# Crea una classe Studente che abbia:
# @classmethod per creare uno studente 
# a partire da una stringa tipo "Luca-20-Matematica"
# @property per calcolare automaticamente l'anno di 
# nascita a partire dall'età
# @property con setter per impedire età negative

class Studente:
    def __init__(self, nome, eta, corso):
        self.nome = nome
        self.eta = eta
        self.corso = corso
    
    @classmethod
    def aggiungiStudente(cls, str):
        nome, eta, corso = str.split("-")
        return cls(nome, eta, corso)
    
    @property
    def anno_nascita(self):
        return int(2025) - int(self.eta)
    
    @property
    def eta(self):
        return self._eta
    
    @eta.setter
    def eta(self, nuova_eta):
        if int(nuova_eta) < 0:
            print("Non si accettano valori negativi")
        else:
            self._eta = nuova_eta

s = Studente.aggiungiStudente("Marian-26-Informatica");
print(s.nome, s.eta, s.corso)
print(s.anno_nascita)
s.eta = 27;
print(s.eta)
print(s.anno_nascita)
