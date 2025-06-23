import json

class Nutzer ():

    def ausleihen(self, MediumID):
        pass

    def zurückgeben(self):
        pass

    def nutzerHinzufuegen(self, name, nutzerID):
        nutzer = self.getNutzer()
        neuer_nutzer = {
            "Name": name,
            "NutzerID": nutzerID,
            "ausgeliehen": []
        },
        nutzer.append(neuer_nutzer)
        with open('Nutzer.JSON', 'w', encoding='utf-8') as f:
            json.dump(nutzer, f, indent=4, ensure_ascii=False)

    def nutzerLoeschen(self):
        pass

    def getNutzer(self):
        nutzer = []
        with open('Nutzer.JSON') as f:
            nutzer = json.load(f)
            print(nutzer)
        return nutzer