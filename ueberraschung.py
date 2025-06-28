import random

def gib_ueberraschungs_fakt():
    fakten = [
        "Wussten Sie, Herr Ruhl, dass Python nach der britischen Comedy-Gruppe Monty Python benannt ist und nicht nach der Schlange?",
        "Wussten Sie, Herr Aschauer, dass MySQL für 'My Structured Query Language' steht und das 'My' vom Namen der Tochter des Mitbegründers Michael Widenius stammt?",
        "Wussten Sie, Herr Ruhl, dass Python eine interpretierte Sprache ist, was bedeutet, dass der Code Zeile für Zeile ausgeführt wird, anstatt vor der Ausführung vollständig kompiliert zu werden?",
        "Wussten Sie, Herr Aschauer, dass, obwohl MySQL eine relationale Datenbank ist, sie auch JSON-Dokumente seit Version 5.7 unterstützt?",
        "Wussten Sie, Herr Ruhl, dass der 'Zen of Python' eine Sammlung von 19 'leitenden Prinzipien' für das Schreiben von Computerprogrammen ist, die die Philosophie von Python beeinflussen? Man kann ihn im Interpreter mit `import this` aufrufen.",
        "Wussten Sie, Herr Aschauer, dass MySQL ursprünglich von einer schwedischen Firma, MySQL AB, entwickelt und später von Sun Microsystems übernommen wurde, die wiederum von Oracle gekauft wurde?",
        "Wussten Sie, Herr Ruhl, dass Python häufig für Webentwicklung (mit Frameworks wie Django und Flask), Datenanalyse, künstliche Intelligenz und Automatisierung eingesetzt wird?",
        "Wussten Sie, Herr Aschauer, dass InnoDB die Standard-Speicher-Engine für MySQL ist, die Transaktionen (ACID-konform) und Fremdschlüssel-Beziehungen unterstützt?",
        "Wussten Sie, Herr Ruhl, dass die Global Interpreter Lock (GIL) in Python bedeutet, dass der Python-Interpreter zu einem Zeitpunkt immer nur einen Thread ausführen kann, auch auf Multi-Core-Prozessoren?",
        "Wussten Sie, Herr Aschauer, dass MySQL eine der beliebtesten Open-Source-Datenbanken der Welt ist und von vielen großen Websites und Anwendungen wie Facebook, Twitter und YouTube verwendet wird (oft in Kombination mit anderen Technologien)?"
    ]

    zufaelliger_fakt = random.choice(fakten)
    print("✨ Überraschungs-Fakt für Sie! ✨")
    print(zufaelliger_fakt)
