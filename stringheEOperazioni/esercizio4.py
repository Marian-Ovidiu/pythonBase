ritardo = input("Sei inn ritardo con la resituzione [si/no]: ").lower().strip()
abbonamento = input("Sei abbonato [si/no]: ").lower().strip()

if ritardo == "si" and abbonamento == "si":
    print("Devi pagare 2 euro di multa e puoi entrare.")
elif ritardo == "no" and abbonamento == "si":
    print("Non devi pagare nulla. Puoi entrare")
elif abbonamento == "no" and ritardo == "si":
    print("Devi pagare 5 euro per l'ingresso e il ritardo.")
else:
    print("Devi pagare 3 euro per l'ingresso.")