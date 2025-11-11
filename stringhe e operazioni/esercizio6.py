#chiedere all'utente quanti euro ha
#chiedere all'utente il prezzo di un oggetto
#usa // per calcolare quante volte l'oggetto può essere comprato
#usa % per calcolare quanti euro avanzano

euro_posseduti = float(input("Quanti euro hai? "))
prezzo_oggetto = float(input("Qual è il prezzo dell'oggetto? "))
oggetti_acquistabili = euro_posseduti // prezzo_oggetto
euro_avanzanti = euro_posseduti % prezzo_oggetto

print("Puoi comprare", int(oggetti_acquistabili), "oggetti.")
print("Ti avanzeranno", euro_avanzanti, "euro.")