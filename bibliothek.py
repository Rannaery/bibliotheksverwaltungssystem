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

    def medium_ausleihen(self, medium_id, nutzer_id):
        nutzer_obj = None
        for n in self.nutzer:
            if n.nutzer_id == nutzer_id:
                nutzer_obj = n
                break
        if not nutzer_obj:
            print(f"Fehler: Nutzer mit ID '{nutzer_id}' nicht gefunden.")
            return False

        for medium in self.medien:
            if medium.id == medium_id:
                if medium.ausgeliehen_an is None:
                    medium.ausgeliehen_an = nutzer_id
                    self._medien_speichern()
                    print(
                        f"'{medium.titel}' (ID: {medium_id}) erfolgreich an Nutzer '{nutzer_obj.name}' (ID: {nutzer_id}) ausgeliehen.")
                    return True
                else:
                    print(
                        f"Fehler: '{medium.titel}' (ID: {medium_id}) ist bereits an Nutzer '{medium.ausgeliehen_an}' ausgeliehen.")
                    return False

        print(f"Fehler: Medium mit ID '{medium_id}' nicht gefunden.")
        return False

    def medium_zurueckgeben(self, medium_id):
        for medium in self.medien:
            if medium.id == medium_id:
                if medium.ausgeliehen_an is not None:
                    print(
                        f"'{medium.titel}' (ID: {medium_id}) wird von Nutzer '{medium.ausgeliehen_an}' zurückgegeben.")
                    medium.ausgeliehen_an = None
                    self._medien_speichern()
                    print(f"'{medium.titel}' (ID: {medium_id}) erfolgreich zurückgegeben.")
                    return True
                else:
                    print(f"Fehler: '{medium.titel}' (ID: {medium_id}) ist nicht ausgeliehen.")
                    return False

        print(f"Fehler: Medium mit ID '{medium_id}' nicht gefunden.")
        return False

    def medien_anzeigen(self, filter_typ=None):
        gefilterte_medien = []
        if filter_typ:
            if filter_typ.lower() == "buch":
                gefilterte_medien = [m for m in self.medien if isinstance(m, Buch)]
            elif filter_typ.lower() == "zeitschrift":
                gefilterte_medien = [m for m in self.medien if isinstance(m, Zeitschrift)]
            elif filter_typ.lower() == "digitalesmedium":
                gefilterte_medien = [m for m in self.medien if isinstance(m, DigitalesMedium)]
            else:
                print("Ungültiger Filter-Typ.")
                return
        else:
            gefilterte_medien = self.medien

        if not gefilterte_medien:
            print("Keine Medien vorhanden oder keine Treffer für den Filter.")
            return

        print("\n--- Aktueller Medienbestand ---")
        for medium in gefilterte_medien:
            status = f" (Ausgeliehen an ID: {medium.ausgeliehen_an})" if medium.ausgeliehen_an else " (Verfügbar)"
            if isinstance(medium, Buch):
                print(
                    f"Buch (ID: {medium.id}): {medium.titel} von {medium.autor}, ISBN: {medium.isbn}, Seiten: {medium.seitenzahl}{status}")
            elif isinstance(medium, Zeitschrift):
                print(
                    f"Zeitschrift (ID: {medium.id}): {medium.titel}, Ausgabe: {medium.ausgabe}, Erscheinungsjahr: {medium.erscheinungsjahr}{status}")
            elif isinstance(medium, DigitalesMedium):
                print(
                    f"Digitales Medium (ID: {medium.id}): {medium.titel}, Format: {medium.format}, Laufzeit: {medium.laufzeit}{status}")

    def nutzer_anzeigen(self):
        if not self.nutzer:
            print("Keine Nutzer vorhanden.")
            return
        print("\n--- Registrierte Nutzer ---")
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
            print(f"Keine Medien für den Suchbegriff '{suchbegriff}' gefunden.")
            return

        print(f"\n--- Suchergebnisse für '{suchbegriff}' ---")
        for medium in treffer:
            status = f" (Ausgeliehen an ID: {medium.ausgeliehen_an})" if medium.ausgeliehen_an else " (Verfügbar)"
            if isinstance(medium, Buch):
                print(
                    f"Buch (ID: {medium.id}): {medium.titel} von {medium.autor}, ISBN: {medium.isbn}, Seiten: {medium.seitenzahl}{status}")
            elif isinstance(medium, Zeitschrift):
                print(
                    f"Zeitschrift (ID: {medium.id}): {medium.titel}, Ausgabe: {medium.ausgabe}, Erscheinungsjahr: {medium.erscheinungsjahr}{status}")
            elif isinstance(medium, DigitalesMedium):
                print(
                    f"Digitales Medium (ID: {medium.id}): {medium.titel}, Format: {medium.format}, Laufzeit: {medium.laufzeit}{status}")