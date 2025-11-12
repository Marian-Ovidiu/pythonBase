#Prova  a scrivere un programma che
#chiede all'utente di inserire un numero positivo
#continua a chiedere finché l'utente non inserisce un numero positivo > 0
#quando ha il numero positivo, stampa "Hai inserito il numero positivo: " seguito dal numero
#e termina

numero = -1  # Inizializza con un valore negativo per entrare nel ciclo
while numero <= 0:
    numero = float(input("Inserisci un numero positivo: ")) 
    if numero > 0:
        print("Hai inserito il numero positivo:", numero)
    else:
        continue



 #extra: dato un numero in input controllare se è azzeccato o meno rispetto a un numero segreto da 1 a 10
numero_segreto = 10   
numero_utente = int(input("Indovina il numero segreto (da 1 a 10): "))
while numero_utente != numero_segreto:
    print("Numero sbagliato, riprova.")
    numero_utente = int(input("Indovina il numero segreto (da 1 a 10): "))
    if numero_utente == numero_segreto:
        print("Complimenti! Hai indovinato il numero segreto:", numero_segreto)
        break