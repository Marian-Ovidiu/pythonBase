studente =  {"nome":"Anna", "voto": 28}
print(studente["nome"])
print(studente["voto"])

#Aggiugni campo
studente["matricola"] = "12345"
print(studente)

#usa get per sicurezza
print(studente.get("nome"))
print(studente.get("cognome", "Non presente"))

#itera su chiavi e valori
for key, value in studente.items():
    print(f"{key}: {value}")

#rimuovi un elemento
studente.pop("voto")
print(studente)
