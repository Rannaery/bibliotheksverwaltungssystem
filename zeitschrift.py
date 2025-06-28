from medium import Medium
import json

class Zeitschrift(Medium):
    def __init__(self, id, titel, ausgabe, erscheinungsjahr, ausgeliehen_an=None):
        super().__init__(titel)
        self.id = id
        self.ausgabe = ausgabe
        self.erscheinungsjahr = erscheinungsjahr
        self.ausgeliehen_an = ausgeliehen_an

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "ausgabe": self.ausgabe,
            "erscheinungsjahr": self.erscheinungsjahr
        })
        return data

def zeitschriften_laden():
    try:
        with open('Zeitschriften.JSON', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Zeitschrift(item['id'], item['titel'], item['ausgabe'], item['erscheinungsjahr'], item['ausgeliehen_an']) for item in data]
    except FileNotFoundError:
        return []

def zeitschriften_speichern(zeitschriften):
    with open('Zeitschriften.JSON', 'w', encoding='utf-8') as f:
        json.dump([zeitschrift.to_dict() for zeitschrift in zeitschriften], f, ensure_ascii=False, indent=4)