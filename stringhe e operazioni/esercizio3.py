eta = int(input("Inserisci la tua età: "))
patente = input("Hai la patente di guida? (si/no): ").lower()

if eta >= 18 and patente == 'si':
    print("Puoi guidare.")
elif eta >= 18 and patente == 'no':
    print("Non puoi guidare senza patente.")
else:
    print("Non puoi guidare.")