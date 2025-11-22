
#Crea una classe Studente 
class Studente():
    # Attributo di classe scuola = "Liceo Classico"
    scuola = "Liceo Classico"
    # Attributo di istanza nome
    def __init__(self,  nome):
        self.nome = nome

    # Medodo di classe cambia_scuola(csl nuova_scuola) che modificia scuola per tutti gli studenti
    @classmethod
    def cambia_scuola(cls, nuova_scuola = "Liceo Classico"):
        cls.scuola = nuova_scuola

    # Metodo istanza presentati() che stampa Sono X e frequento Y
    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e frequento {self.scuola}")


studente1 = Studente("Marian");
studente1.cambia_scuola("Liceo Scientifico");
studente1.presentati();

studente2 = Studente("Andreea");
studente2.presentati();