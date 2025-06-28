from medium import Medium
import json

class DigitalesMedium(Medium):
    def __init__(self, titel, format, laufzeit, id=None, ausgeliehen_an=None):
        super().__init__(titel=titel, id=id, ausgeliehen_an=ausgeliehen_an)
        self.format = format
        self.laufzeit = laufzeit

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "format": self.format,
            "laufzeit": self.laufzeit
        })
        return data

def digitale_medien_laden():
    try:
        with open('DigitaleMedien.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [DigitalesMedium(item['titel'], item['format'], item['laufzeit'],
                                    id=item.get('id'),
                                    ausgeliehen_an=item.get('ausgeliehen_an'))
                    for item in data]
    except FileNotFoundError:
        return []

def digitale_medien_speichern(medien):
    with open('DigitaleMedien.json', 'w', encoding='utf-8') as f:
        json.dump([medium.to_dict() for medium in medien], f, ensure_ascii=False, indent=4)