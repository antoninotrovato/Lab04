class Stand():
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.codice_stand = codice_stand
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo
        self.espositore = None
        self.disponibilita = "Disponibile"
    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.codice_stand == other.codice_stand
        if isinstance(other, str):
            return self.codice_stand == other
        return False
    def non_disponibile(self):
        self.disponibilita = "Non disponibile"
    def __lt__(self, other):
        return self.prezzo < other.prezzo
    def __str__(self):
        return f"{self.codice_stand}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo} - {self.disponibilita}"