from buch import Buch, bucher_laden, bucher_speichern
from zeitschrift import Zeitschrift, zeitschriften_laden, zeitschriften_speichern
from digitalemedien import DigitalesMedium, digitale_medien_laden, digitale_medien_speichern
from nutzer import Nutzer, nutzer_laden, nutzer_speichern
import json

class Bibliothek:
    def __init__(self):
        self.medien = self._alle_medien_laden()
        self.nutzer = nutzer_laden()

    def _alle_medien_laden(self):
        alle_medien = []
        alle_medien.extend(bucher_laden())
        alle_medien.extend(zeitschriften_laden())
        alle_medien.extend(digitale_medien_laden())
        return alle_medien

    def _medien_speichern(self):
        bucher = [m for m in self.medien if isinstance(m, Buch)]
        zeitschriften = [m for m in self.medien if isinstance(m, Zeitschrift)]
        digitale_medien = [m for m in self.medien if isinstance(m, DigitalesMedium)]
        bucher_speichern(bucher)
        zeitschriften_speichern(zeitschriften)
        digitale_medien_speichern(digitale_medien)

    def medium_hinzufuegen(self, medium):
        self.medien.append(medium)
        self._medien_speichern()

    def nutzer_hinzufuegen(self, nutzer):
        self.nutzer.append(nutzer)
        nutzer_speichern(self.nutzer)

    def medium_ausleihen(self, id, nutzer_id):
        for medium in self.medien:
            print(medium.id)
            print(id)
            print(medium.id == id)

            print(medium.ausgeliehen_an)

            if medium.id == id and medium.ausgeliehen_an is None:
                for nutzer_obj in self.nutzer:
                    if nutzer_obj.nutzer_id == nutzer_id:
                        medium.ausgeliehen_an = nutzer_id
                        self._medien_speichern()
                        return True
            else:
                break;

        if medium.id != id:
            print("Medium Titel nicht gefunden")
        if medium.ausgeliehen_an is not None:
            print("Medium wurde bereits von jemandem ausgeliehen")
        return False

    def medium_zurueckgeben(self, titel):
        for medium in self.medien:
            if medium.titel == titel and medium.ausgeliehen_an is not None:
                medium.ausgeliehen_an = None
                self._medien_speichern()
                return True
        return False

    def medien_anzeigen(self, filter_typ=None):
        gefilterte_medien = []
        if filter_typ:
            if filter_typ == "Buch":
                gefilterte_medien = [m for m in self.medien if isinstance(m, Buch)]
            elif filter_typ == "Zeitschrift":
                gefilterte_medien = [m for m in self.medien if isinstance(m, Zeitschrift)]
            elif filter_typ == "DigitalesMedium":
                gefilterte_medien = [m for m in self.medien if isinstance(m, DigitalesMedium)]
            else:
                print("Ungültiger Filter-Typ.")
                return
        else:
            gefilterte_medien = self.medien

        if not gefilterte_medien:
            print("Keine Medien vorhanden oder keine Treffer für den Filter.")
            return

        for medium in gefilterte_medien:
            status = f" (Ausgeliehen an ID: {medium.ausgeliehen_an})" if medium.ausgeliehen_an else " (Verfügbar)"
            if isinstance(medium, Buch):
                print(f"ID: {medium.id} Buch: {medium.titel} von {medium.autor}, ISBN: {medium.isbn}, Seiten: {medium.seitenzahl}{status}")
            elif isinstance(medium, Zeitschrift):
                print(f"ID: {medium.id} Zeitschrift: {medium.titel}, Ausgabe: {medium.ausgabe}, Erscheinungsjahr: {medium.erscheinungsjahr}{status}")
            elif isinstance(medium, DigitalesMedium):
                print(f"ID: {medium.id} Digitales Medium: {medium.titel}, Format: {medium.format}, Laufzeit: {medium.laufzeit}{status}")

    def nutzer_anzeigen(self):
        if not self.nutzer:
            print("Keine Nutzer vorhanden.")
            return
        for nutzer in self.nutzer:
            print(f"Nutzer: {nutzer.name}, ID: {nutzer.nutzer_id}")

    def suchen(self, suchbegriff):
        treffer = []
        for medium in self.medien:
            if suchbegriff.lower() in medium.titel.lower():
                treffer.append(medium)
            elif isinstance(medium, Buch) and suchbegriff.lower() in medium.autor.lower():
                treffer.append(medium)
        if not treffer:
            print("Keine Treffer gefunden.")
            return
        for medium in treffer:
            status = f" (Ausgeliehen an ID: {medium.ausgeliehen_an})" if medium.ausgeliehen_an else " (Verfügbar)"
            if isinstance(medium, Buch):
                print(f"Buch: {medium.titel} von {medium.autor}, ISBN: {medium.isbn}, Seiten: {medium.seitenzahl}{status}")
            elif isinstance(medium, Zeitschrift):
                print(f"Zeitschrift: {medium.titel}, Ausgabe: {medium.ausgabe}, Erscheinungsjahr: {medium.erscheinungsjahr}{status}")
            elif isinstance(medium, DigitalesMedium):
                print(f"Digitales Medium: {medium.titel}, Format: {medium.format}, Laufzeit: {medium.laufzeit}{status}")