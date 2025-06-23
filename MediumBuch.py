from Medium import Medium

class Buch(Medium):
    def __init__(self, Titel: str, Autor: str, ISBN: int, Seitenzahl: int):
        self.Titel = Titel
        self.Autor = Autor
        self.ISBN = ISBN
        self.Seitenzahl = Seitenzahl