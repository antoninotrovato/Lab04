from stand import Stand
class StandPreseElettriche(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, numero_prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.numero_prese = numero_prese
        self.prezzo = prezzo * (1 + 0.07 * numero_prese)