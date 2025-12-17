"""
Progetto: Gestione Biblioteca Digitale

Traccia
In una biblioteca digitale si vuole realizzare un piccolo sistema software per gestire libri, utenti e prestiti.
Il programma deve sfruttare variabili, tipi di dati, strutture di controllo e soprattutto la 
orientata agli oggetti (OOP).

Consegna

Parte 1 Variabili e tipi di dati
Dichiarare e stampare alcune variabili di esempio:
Titolo di un libro (stringa) Numero di copie disponibili (intero) Prezzo medio di un libro (float) 
Stato "disponibile/non disponibile" (booleano)(Esempio: titolo = "Il Signore degli Anelli", copie = 5, ecc.)

Parte 2 Strutture dati
Creare una lista con almeno 5 titoli di libri.
Creare un dizionario che mappi il titolo del libro al numero di copie disponibili.
Creare un insieme (set) che contenga tutti gli utenti registrati alla biblioteca.

Parte 3 Classi e OOP
Creare una classe Libro con attributi:titolo autore anno copie_disponibili
Aggiungere un metodo info() che restituisca una stringa descrittiva del libro.
Creare una classe Utente con attributi:nome eta id_utente
Aggiungere un metodo scheda() che stampi i dati dell’utente.
Creare una classe Prestito che colleghi un Utente a un Libro e contenga:
utente (oggetto Utente) libro (oggetto Libro) giorni (numero di giorni del prestito)
Aggiungere un metodo dettagli() che stampi tutte le informazioni sul prestito.

Parte 4 Funzionalità
Creare una funzione presta_libro(utente, libro, giorni) che:
Verifichi se il libro ha almeno 1 copia disponibile
Se sì → riduca il numero di copie e crei un nuovo oggetto Prestito
Se no → stampi un messaggio di errore
Simulare almeno 3 prestiti con utenti e libri diversi. Stampare a video:
L’elenco aggiornato delle copie disponibili per ciascun libro, I dettagli di ogni prestito effettuato
"""

libri = ["Il Signore degli Anelli", "1984", "Il Grande Gatsby", "Moby Dick", "Orgoglio e Pregiudizio"]
disponibilta_libri = {
    "Il Signore degli Anelli": True,
    "1984": True,
    "Il Grande Gatsby": True,
    "Moby Dick": True,
    "Orgoglio e Pregiudizio": True
}
copie_disponibili = {
    "Il Signore degli Anelli": 5,
    "1984": 3,
    "Il Grande Gatsby": 4,
    "Moby Dick": 2,
    "Orgoglio e Pregiudizio": 6
}
prezzo_medio = {
    "Il Signore degli Anelli": 15.99,
    "1984": 12.50,
    "Il Grande Gatsby": 10.75,
    "Moby Dick": 14.20,
    "Orgoglio e Pregiudizio": 9.99
}

utenti_registrati = {"Alice", "Marco", "Antonio", "Sabrina", "Eve"}

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"{self.titolo} di {self.autore} ({self.anno}) - Copie disponibili: {self.copie_disponibili}"
    
class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        return f"Utente: {self.nome}, Età: {self.eta}, ID: {self.id_utente}"
    
class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def __str__(self):
        return self.dettagli()

    def dettagli(self):
        return f"Prestito: {self.libro.titolo} a {self.utente.nome} per {self.giorni} giorni."
    
    def presta_libro(utente, libro, giorni):
        if libro.copie_disponibili > 0:
            libro.copie_disponibili -= 1
            prestito = Prestito(utente, libro, giorni)
            return prestito
        else:
            print(f"Errore: {libro.titolo} non è disponibile per il prestito.")

# Esempio di utilizzo
prestito1 = Prestito.presta_libro(Utente("Alice", 30, 1), Libro("1984", "George Orwell", 1949, 3), 14)
prestito2 = Prestito.presta_libro(Utente("Marco", 25, 2), Libro("Moby Dick", "Herman Melville", 1851, 2), 7)
prestito3 = Prestito.presta_libro(Utente("Sabrina", 28, 3), Libro("Il Grande Gatsby", "F. Scott Fitzgerald", 1925, 4), 21)
print(prestito1.dettagli())
print(prestito1.libro.info())
print("--------------------")
print(prestito2.dettagli())
print(prestito2.libro.info())
print("--------------------")
print(prestito3.dettagli())
print(prestito3.libro.info())