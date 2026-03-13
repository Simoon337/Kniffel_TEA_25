#############################
### Auswertung eines Zugs ###
###    Alexander Hoppe    ###
###      12.03.2026       ###
#############################

"""Optimierte Auswertung eines Zuges im Kniffel.

Dieses Modul enthält eine verbesserte Version der Funktion `Auswertung_Zug`.
Sie nutzt die optimierte Maske aus `Maske_Positionen_opt.py` und ist klarer
strukturiert, besser testbar und vermeidet redundante Logik.
"""

from typing import List

from Kniffel_TEA_25.Maske_Positionen_opt import Maske

pos = [
    "Einer",
    "Zweier",
    "Dreier",
    "Vierer",
    "Fünfer",
    "Sexer",
    "Dreierpasch",
    "Viererpasch",
    "FullHouse",
    "KleineStrasse",
    "GrosseStrasse",
    "Kniffel",
    "Chance",
]


def Auswertung_Zug(w1: int, w2: int, w3: int, w4: int, w5: int, spielerarray: List[int]) -> List[int]:
    """Wertet einen Zug aus und trägt die Punkte in das Spieler-Array ein.

    Args:
        w1..w5: Die fünf Würfelwerte.
        spielerarray: Liste mit 13 Einträgen; -1 bedeutet "noch nicht belegt".

    Returns:
        Das aktualisierte `spielerarray`.
    """

    print("Mögliche Kategorien:", pos)
    print("Aktueller Spielstand:", spielerarray)

    try:
        p = int(input("Welche Position soll gewertet werden? (1-13): ")) - 1
    except ValueError:
        print("Ungültige Eingabe: Bitte eine Zahl von 1 bis 13 eingeben.")
        return spielerarray

    if not 0 <= p < len(pos):
        print("Ungültige Position: Bitte eine Zahl von 1 bis 13 wählen.")
        return spielerarray

    if spielerarray[p] != -1:
        print("Diese Position ist bereits belegt.")
        return spielerarray

    mask_and_score = Maske(p, w1, w2, w3, w4, w5)
    mask, score = mask_and_score[:5], mask_and_score[5]

    dice = [w1, w2, w3, w4, w5]
    total = score + sum(d for d, m in zip(dice, mask) if m)

    if total == 0 and not any(mask):
        print("Ungültige Eingabe: Die Würfel passen nicht zur gewählten Kategorie.")
        bstreich = input("Möchten Sie in dieser Kategorie 0 Punkte eintragen (ja/nein)? ").strip().lower()
        if bstreich in ("ja", "j", "yes", "y"):
            spielerarray[p] = 0
        else:
            print("Bitte wählen Sie eine andere Kategorie.")
        return spielerarray

    spielerarray[p] = total
    return spielerarray
