giorni = ("lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica")
print(giorni[0])
print(giorni[-1])

print("--------------------")

for i in giorni:
    print(f"{i}")

print("--------------------")

x = (5,)
print(type(x))

x = (5)
print(type(x))

print("--------------------")

colori = ("rosso", "verde", "blu", "giallo", "nero");
print(colori.count("verde"))

print("--------------------")

#creare una tupla con 3 colori, stampa il primo e l'ultimo e conta quatnte volte compare un colore
colori2 = ("arancione", "viola", "rosa")
print(colori2[0])
print(colori2[-1])  
print(colori2.count("viola"))