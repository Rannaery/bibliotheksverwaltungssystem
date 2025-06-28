from bibliothek import Bibliothek
from buch import Buch
from zeitschrift import Zeitschrift
from digitalemedien import DigitalesMedium
from nutzer import Nutzer
from ueberraschung import gib_ueberraschungs_fakt


def main_menu():
    bibliothek = Bibliothek()
    print("Willkommen Herr Aschauer und Rühl bei unserem Projekt!")
    while True:
        print("\n--- Bibliotheksverwaltung ---")
        print("1. Medium hinzufügen")
        print("2. Nutzer hinzufügen")
        print("3. Medium ausleihen")
        print("4. Medium zurückgeben")
        print("5. Medien anzeigen")
        print("6. Nutzer anzeigen")
        print("7. Medien suchen")
        print("8. Beenden")
        print("9. Überraschung")

        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            print("\n--- Medium hinzufügen ---")
            typ = input("Typ (Buch/Zeitschrift/DigitalesMedium): ")
            titel = input("Titel: ")
            if typ.lower() == 'buch':
                autor = input("Autor: ")
                isbn = input("ISBN: ")
                seitenzahl = int(input("Seitenzahl: "))
                medium = Buch(titel, autor, isbn, seitenzahl)
            elif typ.lower() == 'zeitschrift':
                ausgabe = input("Ausgabe: ")
                erscheinungsjahr = int(input("Erscheinungsjahr: "))
                medium = Zeitschrift(titel, ausgabe, erscheinungsjahr)
            elif typ.lower() == 'digitalesmedium':
                format = input("Format: ")
                laufzeit = input("Laufzeit: ")
                medium = DigitalesMedium(titel, format, laufzeit)
            else:
                print("Ungültiger Medientyp.")
                input("Drücken Sie Enter zum Fortfahren...")
                continue
            bibliothek.medium_hinzufuegen(medium)
            print(f"Medium '{medium.titel}' (ID: {medium.id}) hinzugefügt.")
            input("Drücken Sie Enter zum Fortfahren...")

        elif wahl == '2':
            print("\n--- Nutzer hinzufügen ---")
            name = input("Name: ")
            nutzer_id = input("Nutzer-ID: ")
            nutzer = Nutzer(name, nutzer_id)
            bibliothek.nutzer_hinzufuegen(nutzer)
            print("Nutzer hinzugefügt.")
            input("Drücken Sie Enter zum Fortfahren...")

        elif wahl == '3':
            print("\n--- Medium ausleihen ---")
            bibliothek.medien_anzeigen()
            medium_id = input("ID des Mediums, das ausgeliehen werden soll: ")
            bibliothek.nutzer_anzeigen()
            nutzer_id = input("Nutzer-ID des Ausleihenden: ")
            bibliothek.medium_ausleihen(medium_id, nutzer_id)
            input("Drücken Sie Enter zum Fortfahren...")

        elif wahl == '4':
            print("\n--- Medium zurückgeben ---")
            bibliothek.medien_anzeigen()
            medium_id = input("ID des Mediums, das zurückgegeben werden soll: ")
            bibliothek.medium_zurueckgeben(medium_id)
            input("Drücken Sie Enter zum Fortfahren...")

        elif wahl == '5':
            print("\n--- Medien anzeigen ---")
            filter_option = input("Nach Typ filtern (Buch/Zeitschrift/DigitalesMedium/Alle)? (Enter für Alle): ")
            bibliothek.medien_anzeigen(filter_option if filter_option else None)
            input("Drücken Sie Enter zum Fortfahren...")

        elif wahl == '6':
            print("\n--- Nutzer anzeigen ---")
            bibliothek.nutzer_anzeigen()
            input("Drücken Sie Enter zum Fortfahren...")

        elif wahl == '7':
            print("\n--- Medien suchen ---")
            suchbegriff = input("Suchbegriff (Titel oder Autor für Bücher): ")
            bibliothek.suchen(suchbegriff)
            input("Drücken Sie Enter zum Fortfahren...")

        elif wahl == '8':
            print("Programm beendet.")
            print("Erstellt von Emre, Joris und Philipp")
            break
        elif wahl == '9':
            while True:
                gib_ueberraschungs_fakt()
                weiter_wahl = input("\nMöchten Sie einen weiteren Fakt erhalten (j/n)? ").lower()
                if weiter_wahl != 'j':
                    break
            input("Drücken Sie Enter, um zum Hauptmenü zurückzukehren...")


        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")
            input("Drücken Sie Enter zum Fortfahren...")

if __name__ == "__main__":
    main_menu()