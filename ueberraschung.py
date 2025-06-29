import random

def gib_ueberraschungs_fakt():
fakten = [
    "Wussten Sie, Herr Ruhl, dass Python nach der britischen Comedy-Gruppe Monty Python benannt ist\nund nicht nach der Schlange?",
    "Wussten Sie, Herr Aschauer, dass MySQL für 'My Structured Query Language' steht\nund das 'My' vom Namen der Tochter des Mitbegründers Michael Widenius stammt?",
    "Wussten Sie, Herr Ruhl, dass Python eine interpretierte Sprache ist,\nwas bedeutet, dass der Code Zeile für Zeile ausgeführt wird,\nanstatt vor der Ausführung vollständig kompiliert zu werden?",
    "Wussten Sie, Herr Aschauer, dass, obwohl MySQL eine relationale Datenbank ist,\nsie auch JSON-Dokumente seit Version 5.7 unterstützt?",
    "Wussten Sie, Herr Ruhl, dass der 'Zen of Python' eine Sammlung von 19 'leitenden Prinzipien'\nfür das Schreiben von Computerprogrammen ist,\ndie die Philosophie von Python beeinflussen?\nMan kann ihn im Interpreter mit `import this` aufrufen.",
    "Wussten Sie, Herr Aschauer, dass MySQL ursprünglich von einer schwedischen Firma, MySQL AB, entwickelt\nund später von Sun Microsystems übernommen wurde,\ndie wiederum von Oracle gekauft wurde?",
    "Wussten Sie, Herr Ruhl, dass Python häufig für Webentwicklung\n(mit Frameworks wie Django und Flask),\nDatenanalyse, künstliche Intelligenz und Automatisierung eingesetzt wird?",
    "Wussten Sie, Herr Aschauer, dass InnoDB die Standard-Speicher-Engine für MySQL ist,\ndie Transaktionen (ACID-konform) und Fremdschlüssel-Beziehungen unterstützt?",
    "Wussten Sie, Herr Ruhl, dass die Global Interpreter Lock (GIL) in Python bedeutet,\ndass der Python-Interpreter zu einem Zeitpunkt immer nur einen Thread ausführen kann,\nauch auf Multi-Core-Prozessoren?",
    "Wussten Sie, Herr Aschauer, dass MySQL eine der beliebtesten Open-Source-Datenbanken der Welt ist\nund von vielen großen Websites und Anwendungen wie Facebook, Twitter und YouTube verwendet wird\n(oft in Kombination mit anderen Technologien)?"
]

    zufaelliger_fakt = random.choice(fakten)
    print("✨ Überraschungs-Fakt für Sie! ✨")
    print(zufaelliger_fakt)
