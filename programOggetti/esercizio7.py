# Crea una classe ContoBancario con:
# Attributo privato __saldo
# Metodo deposita(importo)
# Metodo preleva(importo)
# Simula alcune operazioni di deposito e prelievo

class ContoBancario():
    def __init__(self):
        self.__saldo = 0

    def deposita(self, somma):
        self.__saldo += somma
        self.mostra_saldo()

    def preleva(self, somma):
        if somma > self.__saldo:
            return print(f"Fondi insufficienti")
        else:
            self.__saldo -= somma
            self.mostra_saldo()

    def mostra_saldo(self):
        print(f"Il nuovo saldo è {self.__saldo}")

c = ContoBancario()
c.deposita(500)
c.preleva(600)
c.preleva(150)
c.deposita(300)
