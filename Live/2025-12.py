# Scrivere un programma che chiede all'utente di inserire la sua età e se ha la patente (si/no)
# Il programma deve stampare true se la persona può guidare quindi eta maggiore uguale a 18 ed ha la 
# patente e deve stampare false in tutti gli altri casi

eta_input = int(input("Inserisci la tua età: "))
patente_input = input("Hai la patente? (si/no): ").strip().lower()

puo_guidare = eta_input >= 18 and patente_input == "si"
print(puo_guidare)

""" Un utente può entrare in biblioteca se: non è in ritardo con la restituizione dei libri
oppure se ha un abbonamento premium. Scrivi un programma che, date due variabili booleane (ritardo e premium),
stampi: True se l'utente può entrare in biblioteca altrimenti False """

ritardo = input("Sei in ritardo con la restituzione dei libri? (si/no): ").strip().lower() == "si"
premium = input("Hai un abbonamento premium? (si/no): ").strip().lower() == "si"

puo_entrare = not ritardo or premium
print(puo_entrare)

"""
Scrivi una funzione chiamata calcola_costo_spedizione che accetti tre parametri:

1 peso (in kg).

2 destinazione (stringa, es: "Italia", "Europa", "Mondo").

3 express (booleano, default False).

Regole:

Base: 5€ fino a 2kg, 10€ oltre i 2kg.

Se la destinazione è "Europa" aggiungi 10€, se "Mondo" aggiungi 20€.

Se express è True, raddoppia il totale finale.

La funzione deve restituire il costo finale.

"""

def calcola_costo_spedizione(peso, destinazione, express=False):
    if peso <= 2:
        costo = 5
    else:
        costo = 10

    if destinazione.lower() == "europa":
        costo += 10
    elif destinazione.lower() == "mondo":
        costo += 20

    if express:
        costo *= 2

    return costo

# Esempi di utilizzo della funzione
print(calcola_costo_spedizione(1.5, "Italia"))        
print(calcola_costo_spedizione(3, "Europa", True))    
print(calcola_costo_spedizione(4, "Mondo"))           


