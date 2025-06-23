from Medium import Medium

class DigitaleMedien(Medium):
    def __init__(self, Titel: str, Format: str, Laufzeit: str):
        self.Titel = Titel
        self.Format = Format
        self.Laufzeit = Laufzeit