#schrivi un programma che
#ha una lista di nomi
#stampa i nomi preceduti dal proprio numero d'ordine
#usa enumare() numero e nome
nomi = ["Alice", "Bob", "Charlie", "Diana"]
for indice, nome in enumerate(nomi, start=1):
    print(f"{indice}. {nome}")


#scrivere una lista di numeri fino a 100
#ciclarli e stampare solamente i numeri primi
for i in range(100):
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if (i % j) == 0:
                break
        else:
            print(i)