# verfiicare se un numero è multiplo di 3
numero = int(input("Inserisci un numero intero: "))
if numero % 3 == 0:
    print(numero, "è un multiplo di 3.")
else:
    print(numero, "non è un multiplo di 3.")


# verificare se il voto iserito è sufficiente o meno
voto = float(input("Inserisci il tuo voto (0-10): "))
if voto >= 6:
    print("Il voto è sufficiente.") 
else:
    print("Il voto non è sufficiente.")

# verificare se una letttera è una vocale o una consonante

lettera = input("Inserisci una lettera: ").lower()
if lettera in 'aeiou':
    print(lettera, "è una vocale.")
else:
    print(lettera, "è una consonante.")

# verificare se un numero è positivo negativo o zero
numero = float(input("Inserisci un numero: "))
if numero > 0:
    print(numero, "è un numero positivo.")  
elif numero < 0:
    print(numero, "è un numero negativo.")
else:
    print("Il numero è zero.")

#in questo esercizio verifichiamo quale tra tre numeri è il più grande
a, b, c = 7, 3, 9
if a >= b and a >= c:
    print(a, "è il numero più grande.")
elif b >= a and b >= c:
    print(b, "è il numero più grande.")
else:
    print(c, "è il numero più grande.")

#calcolare il prezzo del biglietto in base all'età
# se età è minore di 12 anni, il biglietto costa 5 euro
# se eta minore di 65 anni, il biglietto costa 10 euro
#altrimento il prezzo è 12 euro
età = int(input("Inserisci la tua età: "))
if età < 12:
    prezzo_biglietto = 5
elif età < 65:
    prezzo_biglietto = 10
else:
    prezzo_biglietto = 12
print("Il prezzo del biglietto è:", prezzo_biglietto, "euro.")

#dati 3 valori, classificare il tipo di triangolo   
x, y, z = 5, 5, 3
if x == y == z:
    print("Il triangolo è equilatero.")
elif x == y or y == z or x == z:
    print("Il triangolo è isoscele.")
else:
    print("Il triangolo è scaleno.")