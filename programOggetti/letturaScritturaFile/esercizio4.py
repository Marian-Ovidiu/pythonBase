import csv

with open("studenti.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["nome", "età", "corso"])
    
    writer.writerow(["Luca", 20, "Informatica"])
    writer.writerow(["Anna", 22, "Matematica"])
    writer.writerow(["Paolo", 19, "Fisica"])

with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    for row in reader:
        print(row)

#versione di lettura con DictReader 
with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        nome = row["nome"]
        età = row["età"]
        corso = row["corso"]
        print(f"Nome: {nome}, Età: {età}, Corso: {corso}")

#filtro dati per corso
with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    studenti_informatica = [row for row in reader if row["corso"] == "Informatica"]
    print("Studenti iscritti a Informatica:")
    for studente in studenti_informatica:
        print(f"Nome: {studente['nome']}, Età: {studente['età']}")

#filtro dati per studenti maggiorenni
with open("studenti.csv", "r", encoding="utf-8") as f_in, \
    open("studenti_maggiorenni.csv", "w", newline="", encoding="utf-8") as f_out:
    reader = csv.DictReader(f_in)
    studenti_maggiorenni = [row for row in reader if int(row["età"]) >= 18]
    writer = csv.DictWriter(f_out, fieldnames=["nome", "età", "corso"])
    writer.writeheader()
    for studente in studenti_maggiorenni:
        writer.writerow(studente)
    print("File studenti_maggiorenni.csv creato con successo.")