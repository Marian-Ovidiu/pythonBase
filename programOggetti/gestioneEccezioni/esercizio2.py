# Crea una classe Studente con attributo età.
# Se l'età è negativa, solleva EtaNonValidaError.

#Crea una classe Magazzino con metodo rimuovi_prodotto(nome, quantita).
# Se non ci sono abbasatanza pezzi, solleva ProdottoEsauritoError.

# Organizza le tue eccezioni sotto una classe base ErroreScuola o ErroreMagazzino. 

class ErroreScuola(Exception):
    pass

class ErroreMagazzino(Exception):
    pass

class EtaNonValidaErrore(ErroreScuola):
    pass

class ProdottoEsauritoErrore(ErroreMagazzino):
    pass


class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        if eta < 0:
            raise EtaNonValidaErrore("L'età non può essere negativa.")
        self.eta = eta
    
    def __str__(self):
        return f"Studente: {self.nome}, Età: {self.eta}"

class Magazzino:
    prodotti = {}

    def __init__(self):
        pass

    def aggiungi_prodotto(self, nome, quantita):
        if nome in self.prodotti:
            self.prodotti[nome] += quantita
        else:
            self.prodotti[nome] = quantita
    
    def rimuovi_prodotto(self, nome, quantita):
        if nome in self.prodotti:
            if self.prodotti[nome] < quantita:
                raise ProdottoEsauritoErrore(f"Non ci sono abbastanza pezzi di {nome} in magazzino.")
            self.prodotti[nome] -= quantita
        else:
            raise ErroreMagazzino(f"Il prodotto {nome} non esiste in magazzino.")

    
try:
    nome_studente = input("Inserisci il nome dello studente:")
    eta_studente = int(input("Inserisci l'età dello studente:"))
    studente = Studente(nome_studente, eta_studente)
    print(studente)
except EtaNonValidaErrore as e:
    print(f"Errore: {e}")

try:
    magazzino = Magazzino()
    magazzino.aggiungi_prodotto("Penna", 50)
    magazzino.aggiungi_prodotto("Quaderno", 30)
    print("Prodotti aggiunti al magazzino.")
    
    nome_prodotto = input("Inserisci il nome del prodotto da rimuovere:")
    quantita_prodotto = int(input("Inserisci la quantità da rimuovere:"))
    magazzino.rimuovi_prodotto(nome_prodotto, quantita_prodotto)
    print(f"Rimossi {quantita_prodotto} pezzi di {nome_prodotto} dal magazzino.")
except ProdottoEsauritoErrore as e:
    print(f"Errore: {e}")
except ErroreMagazzino as e:
    print(f"Errore: {e}")