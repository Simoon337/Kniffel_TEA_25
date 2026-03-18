# Kniffel (Yahtzee) Programm (Tobias Burgmaier, Alexander Hoppe, Simon Lämmle) 

Dieses Projekt implementiert ein komplett lauffähiges Kniffel-Spiel in Python. Es unterstützt bis zu 8 Spieler und führt Würfelwürfe, Kategorieauswertung, Bonusrundenermittlung und Gewinnerermittlung durch.

## Dateien

- `kniffel.py` - Hauptprogramm: initialisiert Spieler, Spielrunden und führt den Ablauf aus.
- `player.py` - Spielerinteraktion: Begrüßung, Eingabe von Spielerzahl und Namen, Punkteanzeige, Endergebnis und Gewinnerermittlung.
- `role_dice.py` - Würfel-Logik: bis zu drei Würfe pro Spielerzug mit Behalten von Würfeln.
- `Maske_Positionen_opt.py` - Berechnung der Punkte (Einser bis Chance, Sondersituationen).
- `Auswertung_Zug_opt.py` - Auswertung eines Zuges: Klebt Würfelwertungen an die richtige Kategorie, berechnet Bonus, aktualisiert Summe.

## Spielregeln (Kurzfassung)

- Jeder Spieler würfelt pro Runde maximal 3 Mal.
- Nach jedem Wurf kann der Spieler beliebige Würfel behalten.
- Am Zugende wählt der Spieler eine freie Kategorie (Einser..Chance).
- Punkte werden in der entsprechenden Kategorie eingetragen (bei Mismatch sind 0 Punkte möglich).
- Bonus 35 Punkte bei mind. 63 Punkten in Einser..Sechser.
- Nach 13 Runden wird der Gewinner mit der höchsten Summenpunktzahl ermittelt.
- 1-6: Alle 1er, 2er, ... zählen
- Dreierpasch: Drei gleiche Würfel, aber alles zählt
- Viererpasch: Vier gleiche Würfel, aber alles zählt
- Full House: 2 gleiche und 3 gleiche Würfel, 25P
- Kl. Straße: 4 Würfel "in Reihe", 30P
- Gr. Straße: 5 Würfel "in Reihe", 40P
- Kniffel: 5 gleiche Würfel, 50P
- Chance: alle Würfel zählen

## Installation

- Python 3.7+ ist erforderlich.
- Keine zusätzlichen Bibliotheken nötig (`random` ist Teil der Standardbibliothek).

## Ausführung

```bash
python kniffel.py
```

## Architekturübersicht

1. `kniffel.py` startet das Spiel.
2. Spieleranzahl und -namen werden abgefragt.
3. 13 Runden Schleife über alle Spieler.
4. Jeder Zug: Punkteanzeige -> Würfeln (`role_dice.roll_dice`) -> Kategorieauswahl + Scoring (`Auswertung_Zug_opt.Auswertung_Zug`).
5. Nach 13 Runden: Endpunktestand anzeigen (`player.print_final_score`) -> Gewinner (`player.winner`).

## Hinweise zur Erweiterung

- Logging oder GUI anstelle von Konsoleneingabe.
- Unit-Tests für `Maske` und `Auswertung_Zug`.
- Optionale Konfiguration von Spieleranzahl und Runden über Kommandozeilenargumente.
