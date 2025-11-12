#scrivi un programmma che
 #ha una variabile eta
#se eta stampa sei minorenne
#se eta è almeno 18 ma meno di 65 stampa sei adulto
#altriment sei anziano
eta = int(input("Quanti anni hai? "))

if eta < 18:
    print("Sei minorenne.")
elif 18 <= eta < 65:
    print("Sei adulto.")
else:
    print("Sei anziano.")