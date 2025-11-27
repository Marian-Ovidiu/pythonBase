# Crea una classe astratta Veicolo con metodo astraatto muovi()
# Poi crea due classi concrete:
# Auto => muovi() stampa "l'auto si muove su strada"
# Aereo => muovi() stampa "l'aereo vola nel cielo"
# infine scrivi una funzione che accetti un Generico Veicolo e chiami muovi.

from abc import ABC, abstractmethod

class Veicolo(ABC):
    @abstractmethod
    def muovi(self):
        pass

class Auto(Veicolo):
    def muovi(self):
        print("l'auto si muove su strada")

class Aereo(Veicolo):
    def muovi(self):
        print("l'aereo vola nel cielo")

def fai_muovere(veicolo: Veicolo):
    veicolo.muovi()

auto = Auto()
auto.muovi()

aereo = Aereo()
aereo.muovi();

fai_muovere(auto)
fai_muovere(aereo)

