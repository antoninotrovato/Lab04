import csv
from espositori import Espositori
from stand import Stand
from standpremium import StandPremium
from standpreseelettriche import StandPreseElettriche
from csv import reader
class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.elenco_espositori = []
        self.elenco_stand = []
        # TODO
    @property
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lettore = csv.reader(file)
                elenco_stand = []
                elenco_espositori = []
                for riga in lettore:
                  if riga[0][0] == "S":
                    codice_stand = riga[0]
                    superficie = riga[1]
                    padiglione = riga[2]
                    prezzo = riga[3]
                    if len(riga) > 4:
                        if riga[4].isdigit():
                            prese_elettriche = int(riga[4])
                            stand_prese = StandPreseElettriche(codice_stand, superficie, padiglione, prezzo, prese_elettriche)
                            elenco_stand.append(stand_prese)
                        else:
                            posizione = riga[4]
                            stand_premium = StandPremium(codice_stand, superficie, padiglione, prezzo, posizione)
                            elenco_stand.append(stand_premium)
                    else:
                        stand = Stand(codice_stand, superficie, padiglione, prezzo)
                        elenco_stand.append(stand)
                  else:
                      codice = riga[0]
                      nome = riga[1]
                      cognome = riga[2]
                      espositore = Espositori(codice, nome, cognome)
                      elenco_espositori.append(espositore)
                self.elenco_espositori = elenco_espositori
                self.elenco_stand = elenco_stand
        except FileNotFoundError:
            print("File non trovato")
            return
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
