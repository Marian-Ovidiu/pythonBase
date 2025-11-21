numeri = [12, 7 , 9 ,18, 24, 5, 2]
somma_pari = sum([n for n in numeri if n % 2 == 0])
print("La somma dei numeri pari è:", somma_pari)

print('--------------------------')

lista = [1, 2, 2, 3, 4, 4, 5]
lista_dup = [];
for x in  lista:
    if x not in lista_dup:
        lista_dup.append(x)

print("Lista senza duplicati:", lista_dup)
print('--------------------------')

lista = [1,2,3,4,5]
k = 2;

lista_rotata = lista[-k:] + lista[:-k]
print("Lista ruotata di", k, "posizioni:", lista_rotata)

print('--------------------------')

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersezione = [x for x in a if x in b]
print("Intersezione tra le due liste:", intersezione)

print('--------------------------')

coppie = [("a", 1), ("b", 2), ("c", 3)]
diz = dict(coppie)
print("Dizionario creato dalle coppie:", diz)

print('--------------------------')

tuples = [(1,2), (3,4), (5,6)];
somma = sum([sum(t) for t in tuples])
print("Somma di tutti gli elementi nelle tuple:", somma)

print('--------------------------')

numeri = [12, 3,45,7,9]
risultato = (min(numeri), max(numeri))
print("Tupla con il minimo e massimo:", risultato)