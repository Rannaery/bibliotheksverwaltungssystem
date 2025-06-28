from medium import Medium
import json

class DigitalesMedium(Medium):
    def __init__(self, id, titel, format, laufzeit, ausgeliehen_an=None):
        super().__init__(titel)
        self.id = id
        self.format = format
        self.laufzeit = laufzeit
        self.ausgeliehen_an = ausgeliehen_an

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "format": self.format,
            "laufzeit": self.laufzeit
        })
        return data

def digitale_medien_laden():
    try:
        with open('DigitaleMedien.JSON', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [DigitalesMedium(item['id'], item['titel'], item['format'], item['laufzeit'], item['ausgeliehen_an']) for item in data]
    except FileNotFoundError:
        return []

def digitale_medien_speichern(medien):
    with open('DigitaleMedien.JSON', 'w', encoding='utf-8') as f:
        json.dump([medium.to_dict() for medium in medien], f, ensure_ascii=False, indent=4)