from stand import Stand
class StandPreseElettriche(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, numero_prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.numero_prese = numero_prese
        self.prezzo = round(prezzo * (1 + 0.07 * numero_prese),2)
    def __str__(self):
        return f"{self.codice_stand}: Prese extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f} - Prese aggiuntive {self.numero_prese} - {self.disponibilita}"