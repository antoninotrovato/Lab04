from stand import Stand
class StandPremium(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.prezzo = float(prezzo)*1.3
        self.posizione = posizione