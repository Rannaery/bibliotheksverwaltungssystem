# Bibliotheksverwaltungssystem




## 1. Projektbeschreibung
Das Bibliotheksverwaltungssystem ist eine Python-Anwendung zur kompakten Verwaltung von Medien und Nutzern. Die Anwendung ermöglicht das Hinzufügen, Ausleihen und Zurückgeben von Medien (z.B.: Bücher, Zeitschriften, digitale Medien) sowie die Verwaltung von Nutzern.
Die Anwendung nutzt Kapselung, wie auch objektorientierte Programmierung (OOP) mit Vererbung und speichert Daten persistent in JSON-Dateien. Ein Konsolenmenü bietet eine benutzerfreundliche Bedienung. In diesem sind unter anderem Suchfunktion sowie Filteroptionen zur Erleichterung der Navigation & Ansicht mitgeboten. Zusätzlich gibt es eine Überraschungsfunktion, die zufällige Fakten anzeigt.

## 2. Überblick über die Klassen
Die Anwendung ist modular aufgebaut und verwendet folgende Hauptklassen:
• Medium (Basisklasse)
–	Attribute: titel, id (UUID), ausgeliehen_an (Nutzer-ID oder None).
–	Methoden: to_dict() (für JSON-Serialisierung).
–	Zweck: Abstrakte Basisklasse für alle Medientypen.

• Buch (erbt von Medium)
–	Zusätzliche Attribute: autor, isbn, seitenzahl.
–	Zweck: Repräsentiert Bücher mit spezifischen Eigenschaften.

• Zeitschrift (erbt von Medium)
–	Zusätzliche Attribute: ausgabe, erscheinungsjahr.
–	Zweck: Verwaltet Zeitschriften.

• DigitaleMedien (erbt von Medium)
–	Zusätzliche Attribute: format, laufzeit.
–	Zweck: Verwaltet digitale Medien wie Filme oder Podcasts.

• Nutzer
–	Attribute: name, nutzer_id.
–	Zweck: Repräsentiert Bibliotheksnutzer.

• Bibliothek
–	Attribute: medien (Liste aller Medien), nutzer (Liste aller Nutzer).
–	Methoden: medium_hinzufuegen(), nutzer_hinzufuegen(), medium_ausleihen(), medium_zurueckgeben(), medien_anzeigen(), nutzer_anzeigen(), suchen().
–	Zweck: Zentrale Verwaltung von Medien und Nutzern.

## 3. Bedienungsanleitung
1. Programm starten:
– Hierzu  main.py in einer Python-Umgebung ausführen (Python 3.6+ erforderlich).
– TIPP: Sicherstellen, dass die JSON-Dateien (Buecher.JSON, Zeitschriften.JSON, DigitaleMedien.JSON, Nutzer.JSON) im gleichen Verzeichnis liegen.
2. Hauptmenü:
Nach dem Start erscheint das Konsolenmenü mit folgenden Optionen:
1.	Medium hinzufügen: Fügt ein neues Medium in die Bibliothek hinzu.
       2. Nutzer hinzufügen: Legt einen neuen Nutzer ein.
       3. Medium ausleihen: Registriert die Leihe und markiert diese.
       4. Medium zurückgeben: Registriert die Rückgabe & stellt das Medium verfügbar.
       5. Medien anzeigen: Zeigt alle verfügbaren Medien an (mit Filteroption)
       6. Nutzer anzeigen: Listet alle registrierten Nutzer auf.
       7. Medien suchen: Sucht nach Titel oder Autor (für Bücher).
       8. Beenden
       9. Überraschung: Für eine randomisierte Ausgabe von Fakten
3. Beispiel: Buch ausleihen
1. Wähle Option 5, um verfügbare Medien anzuzeigen.
2. Notiere die ID des gewünschten Mediums (z. B. 001 für ein Buch).
3. Wähle Option 6, um Nutzer anzuzeigen, 
4. Notiere die ID des gewünschten Nutzer (z. B. 001).
5. Wähle Option 3, gebe die Medium-ID (001) und Nutzer-ID (001) ein.
6. Das System bestätigt die Ausleihe und bucht diese.

## 4. Hinweise zur Dateispeicherung
• Speicherort: Daten werden in folgenden JSON-Dateien im Projektverzeichnis gespeichert:
-	Buecher.JSON (Bücher)
-	Zeitschriften.JSON (Zeitschriften)
-	DigitaleMedien.JSON (Digitale Medien)
-	Nutzer.JSON (Nutzer)
• Jede Datei enthält bereits eine Liste von Objekten mit den Attributen der jeweiligen 
   Klasse zum testen.s
• Automatisches Laden/Speichern: Beim Programmstart werden vorhandene Daten    
   geladen. Änderungen (z. B. neue Medien, Ausleihen) werden automatisch gespeichert.

   Hinweis: Bei händischer Anpassung der JSON muss das Programm neu gestartet werden um 
            die Änderungen zu übernehmen.
	     Es muss sichergestellt werden, dass die JSON Dateien schreibbar sind. Fehlende JSON-Dateien werden beim Programmstart automatisch neu erstellt.
