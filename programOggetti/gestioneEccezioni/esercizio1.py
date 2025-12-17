# Crea una classe Divisione con un metodoto dividi(a, b) che gestisca la divisione per zero.
# Crea una classe Persona che sollevi un ValueError se l'età inserita è negativa
# Crea una classe Banca Con metodo preleva(). Se il saldo non basta, solleva l'eccezione personalizzata
 
class Divisione:
    def __init__(self):
        pass

    def dividi(self, a, b):
        try:
            return a / b;
        except ZeroDivisionError:
            return "Errore: Divisione per zero non permessa."
        

class Persona:
    def __init__(self):
        pass;
    
    def __str__(self):
        return f"Età: {self.eta}"

    def set_eta(self, eta):
        if eta < 0:
            raise ValueError("L'età non può essere negativa.")
        self.eta = eta;


class Banca:
    saldo = 1000
    def __init__(self):
        pass

    def __str__(self):
        return f"Saldo attuale: {self.saldo} euro"
    
    def preleva(self, importo):
        if importo > self.saldo:
            raise SaldoInsufficienteError("Saldo insufficiente per il prelievo richiesto.")
        self.saldo -= importo
        return self.saldo

class SaldoInsufficienteError(Exception):
    pass

numero1 = int(input("Inserisci il primo numero:"))
numero2 = int(input("Inserisci il secondo numero:"))
divisione = Divisione()
print(divisione.dividi(numero1, numero2))

persona = Persona()
try:
    eta_input = int(input("Inserisci l'età della persona:"))
    persona.set_eta(eta_input)
except ValueError as e:
    print(f"Errore: {e}")

conto = Banca()
print(conto)
try:
    conto.preleva(int(input("Inserisci l'importo da prelevare:")))
except SaldoInsufficienteError as e:
    print(f"Errore: {e}")
print(conto)

