class Espositori():
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
    def __eq__(self, other):
        if isinstance(other, Espositori):
            return self.codice == other.codice
        if isinstance(other, str):
            return self.codice == other
        return False
    def __str__(self):
        return f"Codice {self.codice} - Nome {self.nome} - Cognome {self.cognome}"