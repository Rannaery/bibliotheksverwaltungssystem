from medium import Medium
import json

class Buch(Medium):
    def __init__(self, titel, autor, isbn, seitenzahl, id=None, ausgeliehen_an=None):
        super().__init__(titel=titel, id=id, ausgeliehen_an=ausgeliehen_an)
        self.autor = autor
        self.isbn = isbn
        self.seitenzahl = seitenzahl

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
            return [Buch(item['titel'], item['autor'], item['isbn'], item['seitenzahl'],
                         id=item.get('id'),
                         ausgeliehen_an=item.get('ausgeliehen_an'))
                    for item in data]
    except FileNotFoundError:
        return []

def bucher_speichern(bucher):
    with open('Buecher.JSON', 'w', encoding='utf-8') as f:
        json.dump([buch.to_dict() for buch in bucher], f, ensure_ascii=False, indent=4)