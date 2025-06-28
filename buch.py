from medium import Medium
import json

class Buch(Medium):
    def __init__(self, id, titel, autor, isbn, seitenzahl, ausgeliehen_an=None):
        super().__init__(titel)
        self.id = id
        self.autor = autor
        self.isbn = isbn
        self.seitenzahl = seitenzahl
        self.ausgeliehen_an = ausgeliehen_an

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "autor": self.autor,
            "isbn": self.isbn,
            "seitenzahl": self.seitenzahl
        })
        return data

def bucher_laden():
    try:
        with open('Buecher.JSON', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Buch(item['id'], item['titel'], item['autor'], item['isbn'], item['seitenzahl'], item['ausgeliehen_an']) for item in data]
    except FileNotFoundError:
        return []

def bucher_speichern(bucher):
    with open('Buecher.JSON', 'w', encoding='utf-8') as f:
        json.dump([buch.to_dict() for buch in bucher], f, ensure_ascii=False, indent=4)