# Scrivi un programma che:

# Saluta il cliente e mostra info base

# Chiedi il nome del cliente con input().

# Chiedi la sua età con input() e converti con int().

# Crea una funzione greet(name, age) che stampa un messaggio tipo:

# Ciao, <nome>! Hai <età> anni, raddoppiati fanno <età*2>.


# Chiama la funzione con i dati inseriti.

# Calcola il totale dell’ordine

# Chiedi il prezzo di un articolo (float).

# Chiedi la quantità (int).

# Calcola il totale: totale = prezzo * quantità.

# Stampa il risultato usando una f-string.

# Applica uno sconto con if / else

# Se il totale è maggiore di 50, applica uno sconto del 10%.

# Calcola lo sconto: sconto = totale * 0.10

# Calcola il totale finale: totale_finale = totale - sconto

# Stampa un messaggio tipo: "Hai diritto a uno sconto del 10%!"

# Altrimenti:

# Nessuno sconto, totale_finale = totale

# Stampa un messaggio tipo: "Niente sconto stavolta 😢"

# Alla fine stampa:
# Totale da pagare: <totale_finale>

# Gioca con una frase (stringhe + split + slicing)

# Chiedi al cliente di scrivere una frase qualsiasi.
# Dividila in parole con split().
# Crea una lista di parole invertita con parole[::-1].
# Stampa la lista di parole invertite.
# Controllo parola palindroma
# Chiedi una parola.
# Usa:
# lower() per renderla minuscola
# strip() per togliere spazi
# [::-1] per ottenere la parola al contrario
# Se la parola “pulita” è uguale alla versione invertita → stampa "La parola è palindroma".
# Altrimenti → "La parola non è palindroma".

def greet(name, age):
    print(f"Ciao {name}! Hai {age} anni, raddoppiati fanno {age * 2}.")

def calcola_totale(prezzo, quantita):
    return prezzo * quantita

def is_palindrome(parola):
    parola_pulita = parola.lower().strip()
    return parola_pulita == parola_pulita[::-1]


# 1. Dati cliente
nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))

greet(nome, eta)

# 2. Ordine
prezzo = float(input("Prezzo di un articolo: "))
quantita = int(input("Quanti articoli vuoi comprare? "))

totale = calcola_totale(prezzo, quantita)
print(f"Totale senza sconto: {totale}")

# 3. Sconto
if totale > 50:
    sconto = totale * 0.10
    totale_finale = totale - sconto
    print("Hai diritto a uno sconto del 10%!")
else:
    totale_finale = totale
    print("Niente sconto per ora :(")

print(f"Totale da pagare: {totale_finale}")


# 4. Frase invertita
frase = input("Scrivi una frase: ")
parole = frase.split()
parole_invertite = parole[::-1]
print("Parole in ordine inverso:", parole_invertite)

# 5. Palindroma
parola = input("Scrivi una parola: ")

if is_palindrome(parola):
    print("La parola è palindroma")
else:
    print("La parola non è palindroma")
