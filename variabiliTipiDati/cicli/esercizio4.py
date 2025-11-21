r = range(10)

for i in r:
    print(f"{i+1}")

print("------------------------------------------")

r = range(20)
for i in r:
    if i % 2 == 0 and i != 0:
        print(f"{i}")

print("------------------------------------------")

r = range(2, 21, 2)
for i in r:
    print(f"{i}")

print("------------------------------------------")

parola = "Python"
for lettera in parola:
    print(f"{lettera}")

print("------------------------------------------")

r= range(1, 101)
somma = 0
for i in r:
    somma += i

print(f"La somma dei numeri da 1 a 100 è: {somma}")

print("------------------------------------------")

r = range(3, 31, 3)
for i in r:
    print(f"{i}")

print("------------------------------------------")

n = 5
fattoriale = 1
for i in range(1, n + 1):
    fattoriale *= i
print(f"Il fattoriale di {n} è: {fattoriale}")

print("------------------------------------------")

parola = "programmazione"
vocali = "aeiou"
count = 0
for lettera in parola:
    if lettera in vocali:
        count += 1

print(f"La parola '{parola}' contiene {count} vocali.")

print("------------------------------------------")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end="  ")
    print()

print("------------------------------------------")

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(i)

print("------------------------------------------")

for i in range(1, 11):
    if i == 8:
        break
    else:
        print(i)
