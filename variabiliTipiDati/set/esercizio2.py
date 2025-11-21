#immaginamia due corsi universitari: COrso A e Corso B
# vogliamo sapere:
# 1. chi frequenta entrambi i corsi
# 2. chi frequenta solo il corso A
# 3. chi frequenta solo il corso B
# 4. chi frequenta almeno uno dei due corsi
# 5. quanti studenti unici ci sono in totale

corso_a = {"Alice", "Bob", "Carla", "Davide"}
corso_b = {"Carla", "Elena", "Francesco", "Giovanni"}

# 1. chi frequenta entrambi i corsi
frequenta_entrambi = corso_a & corso_b
print("Studenti che frequentano entrambi i corsi:", frequenta_entrambi)

# 2. chi frequenta solo il corso A
solo_corso_a = corso_a - corso_b
print("Studenti che frequentano solo il corso A:", solo_corso_a)

# 3. chi frequenta solo il corso B
solo_corso_b = corso_b - corso_a
print("Studenti che frequentano solo il corso B:", solo_corso_b)

# 4. chi frequenta almeno uno dei due corsi
almeno_uno = corso_a.union(corso_b)
print("Studenti che frequentano almeno uno dei due corsi:", almeno_uno)

