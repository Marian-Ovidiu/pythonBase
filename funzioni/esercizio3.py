#scrivere un programma che  analizza un testo e analizza varie statistiche
#conta il numero totale di parole
#calcola la frequenza di ogni parola
#estrarre le parole uniche usando i set
# mostrare le 5 parole più frequenti
#calcolare la media dei caratteri

p = 'Un giorno sono andato al mare mare mare, ma non ho toccato l\'acqua, sono rimasto a prendere il sole'

def numero_totale(parola):
    return len(set(parola.split()));

def frequenza_parole(testo):
    parole = []

    if type(testo) == str:
        parole = testo.split()

    freq = {}
    for parola in parole:
        parola = parola.lower().strip(",.!?;:")
        if parola in freq:
            freq[parola] += 1
        else:
            freq[parola] = 1
    return freq

def parole_uniche(testo):
    parole = []

    if type(testo) == str:
        parole = testo.split()
        for i, parola in enumerate(parole):
            parola = parola.lower().strip(",.!?;:")
            parole[i] = parola

    return set(parole)

def top_5(testo):
    freq = frequenza_parole(testo) 
    top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
    return top5

def lunghezza_media(freq):
    tot_car = sum(len(p) * occ for p, occ in freq.items())
    tot_parole = sum(freq.values())
    return tot_car / tot_parole

print(numero_totale(p))
print(frequenza_parole(p))
print(parole_uniche(p))
print(top_5(p))
print(lunghezza_media(frequenza_parole(p)))