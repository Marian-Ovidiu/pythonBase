persone = [
    {
        "nome": "Luca Rossi",
        "numero": "3331234567",
        "email": "luca.rossi@example.com"
    },
    {
        "nome": "Giulia Bianchi",
        "numero": "3209876543",
        "email": "giulia.bianchi@example.com"
    },
    {
        "nome": "Marco Verdi",
        "numero": "3451122334",
        "email": "marco.verdi@example.com"
    }
]

#aggiungere un nuovo contatto (nome numero email)

def aggiungiContatto(nome, numero, email):
    persone.append({
        "nome" : nome,
        "numero" : numero,
        "email": email
    })


#modificare un contatto esistente

def modificaContatto(nome, numero = None, nuova_mail = None):
    trovato = False
    for c in persone:
        if c["nome"].lower() == nome.lower():
            if numero:
                c['numero'] = numero
            
            if nuova_mail:
                c["email"] = nuova_mail
            
            print(f'contatto {nome} modificato')
            trovato = True
            break  # possiamo anche uscire dal loop

    if not trovato:
        print(f"Contatto {nome} non trovato")



aggiungiContatto("Mario Rossi", '1234567890', "mario.rossi@gmail.com")
modificaContatto("Mario Rossi", '8901234567', "mario_rossi@gmail.com")
print(persone)


#eliminare un contatto

def eliminaContatto(nome):
    for i in persone:
        if i['nome'].lower == nome.lower():
            persone.remove(i)
            print(f"Contatto {nome} eliminato!")
            return
    print("Contatto non trovato")

#cercare un contatto per nome
def cerca_contatto(nome):
    for i in persone:
        if i['nome'].lower() == nome.lower():
            print("Contatto trovato", i)
            return
    print("Contatto non trovato")

#visualizzare tutti i contatti in ordine alfabetico
def mostra_contatti():
    if not persone:
        print("Rubrica vuota")

    ordinati = sorted(persone, key=lambda x: x['nome'].lower())
    
    for i in ordinati:
        print(f"({i['nome']} + {i['numero']} + {i['email']})")

aggiungiContatto("Luca", "1234567890", "luca@gmail.com")
aggiungiContatto("Anna", "6789012345", "anna@gmail.com") 
mostra_contatti()

modificaContatto('Luca', nuova_mail="luca.nuova@gmail.com")
cerca_contatto('Anna')
mostra_contatti()