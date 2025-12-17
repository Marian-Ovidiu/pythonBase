"""
Realizzare un sistema per una biblioteca digitale che gestisca:
catalogo libri, utenti registrati, prestiti dei libri

Devi usare: variabili, strutture dati, OOP (classi), funzioni, if/loop.

Parte 1 — Variabili base
Dichiara e stampa una volta queste variabili di esempio (solo per mostrare i tipi):
titolo_esempio (str) - copie_esempio (int) - prezzo_medio_esempio (float) - disponibile_esempio (bool)
Nota: queste variabili sono solo dimostrative e NON devono poi essere usate per il resto del progetto.

Parte 2 — Strutture dati
Crea una lista con almeno 5 libri, ma invece che una lista di stringhe, fai una lista di oggetti Libro 
(così non duplichi dati).

Crea un dizionario catalogo che permetta di trovare un libro velocemente:
chiave: titolo, valore: oggetto Libro
Esempio: catalogo["1984"] -> Libro(...)

Crea un set utenti_registrati che contenga gli ID utente.

Parte 3 — Classi (OOP)
Classe Libro - Attributi:
titolo autore anno copie_disponibili prezzo
Metodo:
info() → restituisce una stringa descrittiva

Classe Utente - Attributi:
nome eta id_utente
Metodo: scheda() → restituisce i dati utente

Classe Prestito - Attributi:
utente (oggetto Utente) libro (oggetto Libro) giorni
Metodo:
dettagli() → restituisce le info del prestito

Parte 4 — Funzionalità di prestito
Crea una funzione esterna chiamata: presta_libro(utente, libro, giorni)

Regole:
se libro.copie_disponibili > 0:
decrementa le copie

crea e ritorna un oggetto Prestito
altrimenti: stampa un messaggio tipo: “Libro non disponibile”
ritorna None

Parte 5 — Simulazione finale
Crea almeno:
3 utenti - 5 libri - un catalogo dizionario
Simula almeno 3 prestiti (utenti e libri diversi).

Stampa:
l’elenco dei prestiti effettuati, le copie aggiornate di ogni libro nel catalogo
"""

# Parte 1 — Variabili base
titolo_esempio = "Esempio Libro"
copie_esempio = 10
prezzo_medio_esempio = 19.99
disponibile_esempio = True
print("Titolo:", titolo_esempio)
print("Copie disponibili:", copie_esempio)
print("Prezzo medio:", prezzo_medio_esempio)
print("Disponibile:", disponibile_esempio)

# Parte 3 — Classi (OOP)
class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili, prezzo):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili
        self.prezzo = prezzo

    def __str__(self):
        return self.info()

    def info(self):
        return (
            f"{self.titolo} di {self.autore} ({self.anno}) "
            f"- Copie: {self.copie_disponibili} - Prezzo: €{self.prezzo:.2f}"
        )

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

    def dettagli(self):
        return f"Prestito: {self.libro.titolo} a {self.utente.nome} per {self.giorni} giorni"

# Parte 2 — Strutture dati
libri = [
    Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 5, 15.99),
    Libro("1984", "George Orwell", 1949, 3, 12.50),
    Libro("Il Grande Gatsby", "F. Scott Fitzgerald", 1925, 4, 10.75),
    Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry", 1943, 6, 9.99),
    Libro("Moby Dick", "Herman Melville", 1851, 2, 14.20),
]

catalogo = {libro.titolo: libro for libro in libri}
print("\nCatalogo dei libri:")
for titolo, libro in catalogo.items():
    print(libro)

#parte 4 — Funzionalità di prestito
def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili > 0:
        libro.copie_disponibili -= 1
        prestito = Prestito(utente, libro, giorni)
        return prestito
    else:
        print(f"Errore: {libro.titolo} non è disponibile per il prestito.")
        return None
    
# Parte 5 — Simulazione finale
utenti = [
    Utente("Alice", 30, 1),
    Utente("Marco", 25, 2),
    Utente("Sabrina", 28, 3),
]

utenti_registrati = {u.id_utente for u in utenti}
print("\nUtenti registrati (ID):", utenti_registrati)
print("\nSchede utenti:")
for u in utenti:
    print(u.scheda())
    

prestiti = []

prestito1 = presta_libro(utenti[0], catalogo["1984"], 14)
if prestito1:
    prestiti.append(prestito1)

prestito2 = presta_libro(utenti[1], catalogo["Moby Dick"], 7)
if prestito2:
    prestiti.append(prestito2)

prestito3 = presta_libro(utenti[2], catalogo["Il Grande Gatsby"], 21)
if prestito3:
    prestiti.append(prestito3)

print("\nElenco dei prestiti effettuati:")
for prestito in prestiti:
    print(prestito.dettagli())

print("\nCopie aggiornate di ogni libro nel catalogo:")
for cat in catalogo.values():
    print(cat)

