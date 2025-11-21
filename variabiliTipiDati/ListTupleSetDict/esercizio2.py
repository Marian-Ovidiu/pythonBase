tuples = [(1,3), (2, 1), (5, 0)]
ordinata = sorted(tuples, key=lambda x: x[1])
print(ordinata)

print("--------------------")

t = (1,2,3,4,5,6)
pari = tuple(x for x in t if x % 2 == 0)
print(pari) 

print("--------------------")

t = (1,2,3,4,5,6)
invertita1 = t[::-1];
invertita2 = tuple(reversed(t))
print(invertita1)
print(invertita2)

print("--------------------")

s = "Programmazione"
t = tuple(s)
print(t)
t = set(t)
print(t)    

print("--------------------")

a = [1,2,3]
b = ["a", "b", "c"]
zipped = list(zip(a,b))
print(zipped)

print("--------------------")

A = {1,2,3}
B = {3,4,5}
C = {5,6}

diff = A ^ B ^ C
print(diff)

print("--------------------")

frase = "ciao come stai, ciao tutto bene"
uniche = set(frase.split())
print(uniche)

print("--------------------")

liste = [[1,2,3], [3,4,5], [6,7]]
unione = set().union(*map(set, liste))
print(unione)

liste = [[1,2,3], [3,4,5], [6,7]]
#OPPURE 
unione = set()
for sotto_lista in liste:
    for numero in sotto_lista:
        unione.add(numero)
print(unione)
