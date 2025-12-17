# ============================================================
# ESERCIZIO: Sistema di Gestione Libreria Digitale
# ============================================================
# Obiettivo:
# Creare un sistema per gestire una libreria digitale sfruttando:
# - classi astratte
# - ereditarietà
# - polimorfismo
# - property
# - staticmethod o classmethod
# - operator overloading (+, ==, len(), str())
#
# ============================================================
# 1) Classe astratta Media
# ============================================================
# Crea una classe astratta "Media" con:
# - attributi protetti:
#       _titolo (str)
#       _autore (str)
#       _durata_minuti (float/int)
# - property in sola lettura per titolo, autore, durata
# - metodo statico valida_durata(durata) -> True se durata > 0
# - metodo astratto descrizione()
# - __str__ che usa descrizione()
# - __eq__ che confronta due Media in base a titolo e autore
#
# ============================================================
# 2) Sottoclassi concrete
# ============================================================
# Crea almeno due classi che ereditano da Media:
#
#   Classe Ebook:
#       - attributo aggiuntivo: _numero_pagine (int)
#       - property numero_pagine
#       - descrizione():
#           "Ebook: 'titolo' di autore - durata X min - pagine Y"
#
#   Classe Audiolibro:
#       - attributo aggiuntivo: _narratore (str)
#       - property narratore
#       - descrizione():
#           "Audiolibro: 'titolo' di autore, narrato da X - durata Y min"
#
# (Opzionale: aggiungi anche PodcastEpisode o altre varianti)
#
# ============================================================
# 3) Classe LibreriaDigitale
# ============================================================
# La classe deve:
# - contenere una lista interna di oggetti Media
# - permettere:
#       aggiungi_media(media)
#       rimuovi_media(media)
#       totale_durata() -> somma delle durate
#
# - operatori overload:
#       __len__  -> numero di contenuti
#       __str__  -> lista formattata + durata totale
#       __add__  -> unisce due librerie in una nuova LibreriaDigitale
#
# ============================================================
# 4) Overloading extra (facoltativo)
# ============================================================
# Implementa __eq__ per confrontare due librerie
# (scegli se confrontare durata totale o numero di elementi).
#
# ============================================================
# 5) Programma di test
# ============================================================
# Scrivi uno script che:
# - crea vari Ebook e Audiolibro
# - crea due librerie diverse
# - aggiunge contenuti differenti
# - stampa contenuto e durata totale di ciascuna libreria
# - mostra len(libreria)
# - combina due librerie con +
# - confronta Media con ==
# - (se implementato) confronta LibreriaDigitale con ==
#
# ============================================================
# Fine consegna
# ============================================================

from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, titolo: str, autore: str, durata_minuti: float):
        self._titolo = titolo
        self._autore = autore
        if not self.valida_durata(durata_minuti):
            raise ValueError("La durata deve essere maggiore di 0")
        self._durata_minuti = durata_minuti

    @property
    def titolo(self):
        return self._titolo
    
    @property
    def autore(self):
        return self._autore

    @property
    def durata_minuti(self):
        return self._durata_minuti
    
    @staticmethod
    def valida_durata(durata):
        return durata > 0
    
    @abstractmethod
    def descrizione(self):
        pass

    def __str__(self):
        return self.descrizione()
    
    def __eq__(self, other):
        if not isinstance(other, Media):
            return NotImplemented
        return self.titolo == other.titolo and self.autore == other.autore

class Ebook(Media):
    def __init__(self, titolo: str, autore: str, durata_minuti: float, numero_pagine: int):
        super().__init__(titolo, autore, durata_minuti)
        self._numero_pagine = numero_pagine

    @property
    def numero_pagine(self):
        return self._numero_pagine
    
    def descrizione(self):
        return f"Ebook: '{self.titolo}' di {self.autore} - durata {self.durata_minuti} min - pagine {self.numero_pagine}"
    
class Audiolibro(Media):
    def __init__(self, titolo: str, autore: str, durata_minuti: float, narratore: str):
        super().__init__(titolo, autore, durata_minuti)
        self._narratore = narratore

    @property
    def narratore(self):
        return self._narratore
    
    def descrizione(self):
        return f"Audiolibro: '{self.titolo}' di {self.autore}, narrato da {self.narratore} - durata {self.durata_minuti} min"
    
class LibreriaDigitale:
    def __init__(self):
        self.media_list = []

    def aggiungi_media(self, media: Media):
        self.media_list.append(media)

    def rimuovi_media(self, media: Media):
        if media in self.media_list:
            self.media_list.remove(media)

    def totale_durata(self):
        return sum(media.durata_minuti for media in self.media_list)

    def __len__(self):
        return len(self.media_list)

    def __str__(self):
        if not self.media_list:
            return "Libreria Digitale vuota"
        lines = [str(media) for media in self.media_list]
        lines.append(f"Durata Totale: {self.totale_durata()} min")
        return "\n".join(lines)

    def __add__(self, other):
        new_library = LibreriaDigitale()
        new_library.media_list = self.media_list + other.media_list
        return new_library
    
# Esempio di utilizzo
ebook1 = Ebook("1984", "George Orwell", 300, 328)
audiolibro1 = Audiolibro("Il Nome della Rosa", "Umberto Eco", 480, "Francesco Pannofino")

library1 = LibreriaDigitale()
library2 = LibreriaDigitale()

library1.aggiungi_media(ebook1)
library2.aggiungi_media(audiolibro1)
print("Libreria 1:")
print(library1)
print("\nLibreria 2:")
print(library2)

combined_library = library1 + library2
print("\nLibreria Combinata:")
print(combined_library)
print(f"\nNumero di contenuti nella libreria combinata: {len(combined_library)}")

library1.rimuovi_media(ebook1)
print("\nLibreria 1 dopo la rimozione:")
print(library1)

print(f"\nNumero di contenuti nella libreria 2: {len(library2)}")
print(f"Durata totale della libreria 2: {library2.totale_durata()} min")
