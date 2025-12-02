# Creare un sistema per gestire conti bancari diversi,
# sfruttando classi astratte, ereditarietà, poliformismo,
# property, decoratori e operator overloading.

from abc import ABC, abstractmethod

class Conto(ABC):
    def __init__(self, intestatario, saldoIniziale = 0):
        self._intestatario = intestatario
        self._saldo = saldoIniziale

    @property
    def saldo(self):
        return self.saldo
    
    @staticmethod
    def validaImporto(importo):
        return importo > 0
    
    @abstractmethod
    def deposita(self, importo):
        # self.saldo += importo
        pass

    def preleva(self, importo):

        pass

    def __str__(self):
        return f"Conto di {self._intestatario} - Saldo: {self._saldo:.2f}$"
    
class ContoCorrente(Conto):
    COMMISSIONE = 1.5

    def deposita(self, importo):
        if self.validaImporto(importo):
            self._saldo += importo
        else:
            print("Importo non valido per il deposito")

    def preleva(self, importo):
        totale = importo + ContoCorrente.COMMISSIONE
        
        if self.validaImporto(importo) and self._saldo >= totale:
            self._saldo -= totale
        else:
            print("Saldo insufficiente o importo non valido!")
    
    def __add__(self, altro):
        nuovo_saldo = self._saldo + altro._saldo
        return ContoCorrente(f"{self._intestatario} & {altro._intestatario}", nuovo_saldo)
    
cc1 = ContoCorrente("Luca", 1000)
cc2 = ContoCorrente("Giulia", 500)

cc1.deposita(200)
cc1.preleva(50)
print(cc1)

conto_fuso = cc1 + cc2
print(conto_fuso)

