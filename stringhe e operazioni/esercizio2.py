parola = input("inserisci una parola: ").lower()
print("la parola inserita è:", parola.strip())
parola2 = parola[::-1];

if parola == parola2:
    print("la parola è palindroma")
else:
    print("la parola non è palindroma")