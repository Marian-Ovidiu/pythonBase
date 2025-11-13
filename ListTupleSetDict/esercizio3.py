A = {"Anna", "Luca", "Marco"}
B = {"Luca", "Sara", "Marco"}
print(A & B)
print(A - B)
print(B - A)
print(len(A | B))

print("-------------------")

import random

numeri = {random.randint(1,20) for _ in range(10)}
print(numeri)

print("--------------------")

frase = "ciao come stai ciao tutto bene"
parole = frase.split()
print(parole)
conteggio = {}
for p in parole:
    conteggio[p] = conteggio.get(p, 0) + 1
print(conteggio)

print("--------------------")

d = {"A": 1, "B":2, "C": 3}
inverso = {v:k for k,v in d.items()}
print(inverso)

print("--------------------")

chiavi = ["nome", "eta", "citta"] 
valori =  ["Anna", 25, "Roma"]
d = dict(zip(chiavi, valori))
print(d)

print("---------------------")

parola = ["ciao", "come", "va", "oggi"]
gruppi = {};

for p in parola:
    gruppi.setdefault(len(p), []).append(p)
print(gruppi)

print("---------------------")

testo = "programmazione"
frequenza = {}
for c in testo:
    frequenza[c] = frequenza.get(c,0)+1
print(frequenza)