"""Optimierte Maske für Kniffel-Positionen.

Dieses Modul enthält eine bereinigte und wartbare Implementierung der
Positionsmaske (Maske) für Kniffel.

Die Funktion `Maske(p, w1, w2, w3, w4, w5)` liefert eine Liste mit
5 booleschen Werten (für die Würfel) und einen Punktwert (Score).

Die Semantik entspricht der alten Implementierung in Maske_Positionen.py.
"""

from collections import Counter
from typing import List, Tuple


def Maske(p: int, w1: int, w2: int, w3: int, w4: int, w5: int) -> List[object]:
    """Berechne Maske + Punkte für die Kniffel-Kategorie p.

    Args:
        p: Kategorieindex (0=bestehend aus 13 Positionen: Einer..Chance).
        w1..w5: Werte der fünf Würfel (1-6).

    Returns:
        [b1, b2, b3, b4, b5, score]
        - b1..b5: Booleans, welche Würfel gewertet werden.
        - score: Punktzahl (für manche Kategorien fix, sonst 0 und die Summe
          wird extern über die Maske berechnet).
    """

    dice = [w1, w2, w3, w4, w5]
    mask = [False, False, False, False, False]
    score = 0

    if 1 <= p <= 6:  # Einer..Sechser
        target = p + 1
        mask = [d == target for d in dice]
        return mask + [score]

    counts = Counter(dice)

    if p == 7:  # Dreierpasch
        if any(v >= 3 for v in counts.values()):
            mask = [True] * 5
        return mask + [score]

    if p == 8:  # Viererpasch
        if any(v >= 4 for v in counts.values()):
            mask = [True] * 5
        return mask + [score]

    if p == 9  :  # FullHouse
        if sorted(counts.values()) == [2, 3]:
            score = 25
        return mask + [score]

    if p == 10:  # Kleine Straße
        if _has_straight(dice, 4):
            score = 30
        return mask + [score]

    if p == 11:  # Große Straße
        if _has_straight(dice, 5):
            score = 40
        return mask + [score]

    if p == 12:  # Kniffel
        if any(v == 5 for v in counts.values()):
            score = 50
        return mask + [score]

    if p == 13:  # Chance
        mask = [True] * 5
        return mask + [score]

    return mask + [score]


def _has_straight(dice: List[int], length: int) -> bool:
    """Prüft, ob im Würfelwurf eine Straße der Länge 'length' enthalten ist."""
    unique = sorted(set(dice))
    for start in range(1, 7 - length + 1):
        if all(val in unique for val in range(start, start + length)):
            return True
    return False
