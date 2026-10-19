from stand import Stand
class StandPremium(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.prezzo = round(float(prezzo)*1.3,2)
        self.posizione = posizione
    def __str__(self):
        return f"{self.codice_stand}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo} - Posizione: {self.posizione} - {self.disponibilita}"