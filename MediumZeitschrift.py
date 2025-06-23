from Medium import Medium

class Zeitschrift(Medium):
    def __init__(self, Titel: str, Ausgabe: str, Erscheinungsjahr: int):
        self.Titel = Titel
        self.Ausgabe = Ausgabe
        self.Erscheinungsjahr = Erscheinungsjahr
