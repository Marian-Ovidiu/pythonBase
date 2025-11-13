# Crea un dizionario che rappresenti uno studente con le seguenti chiavi:
# "nome", "eta", "corso"
# modifica il valore della chiave "eta"
# aggiungi una nuova chiave "matricola" con un valore
# usa .get() per recuperare un valore sconosciuto senza generare un errore
# itera su tutte le chiavi e i valori del dizionario e stampali

studente = {"nome": "Luca", "eta": 21, "corso": "Informatica"}
# Modifica il valore della chiave "eta"
studente["eta"] = 22
# Aggiungi una nuova chiave "matricola" con un valore
studente["matricola"] = "67890"
# Usa .get() per recuperare un valore sconosciuto senza generare un errore
cognome = studente.get("cognome", "Non presente")
print(f"Cognome: {cognome}")
# Itera su tutte le chiavi e i valori del dizionario e stampali
for key, value in studente.items():
    print(f"{key}: {value}")
print(studente)