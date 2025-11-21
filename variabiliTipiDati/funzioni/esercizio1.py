def quadrato(x):
    return x * x

print(quadrato(5))
print(quadrato(12))    

print('---------------------------')

def saluta(nome, saluta = 'Ciao'):
    print(f"{saluta} ", nome)

saluta("Luca")
saluta("Anna", "Buongiorno")

print('---------------------------')

def somma(*args):
    return sum(args)

print(somma(1, 2, 3))
print(somma(10, 20, 30, 40))

print('---------------------------')

#definisci una funzione chiamata media che:
#riceve una lista di numeri (parametro)
#calcola e restituisce la media

def media(*args):
    return sum(args) / len(args)

elements = [1,2,3,4,5,6,7]

print(f"La media dei numeri {elements} è: {media(*elements)}")