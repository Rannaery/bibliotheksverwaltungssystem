# import json
#
# class Nutzer ():
#
#     def ausleihen(self, MediumID):
#         pass
#
#     def zurückgeben(self):
#         pass
#
#     def nutzerHinzufuegen(self, name, nutzerID):
#         nutzer = self.getNutzer()
#         neuer_nutzer = {
#             "Name": name,
#             "NutzerID": nutzerID,
#             "ausgeliehen": []
#         },
#         nutzer.append(neuer_nutzer)
#         with open('Nutzer.JSON', 'w', encoding='utf-8') as f:
#             json.dump(nutzer, f, indent=4, ensure_ascii=False)
#
#     def nutzerLoeschen(self):
#         pass
#
#     def getNutzer(self):
#         nutzer = []
#         with open('Nutzer.JSON') as f:
#             nutzer = json.load(f)
#             print(nutzer)
#         return nutzer




import json

class Nutzer:
    def __init__(self, name, nutzer_id):
        self.name = name
        self.nutzer_id = nutzer_id

    def to_dict(self):
        return {"Name": self.name, "NutzerID": self.nutzer_id}

def nutzer_laden():
    try:
        with open('Nutzer.JSON', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Nutzer(item['name'], item['nutzerID']) for item in data]
    except FileNotFoundError:
        return []

def nutzer_speichern(nutzer_liste):
    with open('Nutzer.JSON', 'w', encoding='utf-8') as f:
        json.dump([nutzer.to_dict() for nutzer in nutzer_liste], f, ensure_ascii=False, indent=4)