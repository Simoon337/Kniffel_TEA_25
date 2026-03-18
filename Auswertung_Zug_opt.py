#############################
### Auswertung eines Zugs ###
###    Alexander Hoppe    ###
###      12.03.2026       ###
#############################

#Bearbeitet am 17.03.2026 von Tobias Burgmaier

"""Optimierte Auswertung eines Zuges im Kniffel.

Dieses Modul enthält eine verbesserte Version der Funktion `Auswertung_Zug`.
Sie nutzt die optimierte Maske aus `Maske_Positionen_opt.py` und ist klarer
strukturiert, besser testbar und vermeidet redundante Logik.
"""

from Maske_Positionen_opt import Maske
import player

# pos = [
#     "(1) Einer",
#     "(2) Zweier",
#     "(3) Dreier",
#     "(4) Vierer",
#     "(5) Fünfer",
#     "(6) Sechser",
#     "    Bonus",
#     "(7) Dreierpasch",
#     "(8) Viererpasch",
#     "(9) FullHouse",
#     "(10)Kleine Straße",
#     "(11)Große Straße",
#     "(12)Kniffel",
#     "(13)Chance",
#     "    Summe",
# ]


def Auswertung_Zug(wuerfelarray, spielerarray, spielername):
    """Wertet einen Zug aus und trägt die Punkte in das Spieler-Array ein.

    Args:
        wuerfelarray: Liste mit den fünf Würfelwerten.
        spielerarray: Liste mit 15 Einträgen; `None` bedeutet "noch nicht belegt".

    Returns:
        aktualisierter `spielerarray`
    """
    w1, w2, w3, w4, w5 = wuerfelarray
    # print(w1, w2, w3, w4, w5)
    # print("Mögliche Kategorien:", pos)
    # print("Aktueller Spielstand:", spielerarray)
    player.print_score_list(spielername, spielerarray)

    # Abfrage der Kategorie, die gewertet werden soll
    wertung_erfolgt = False
    while not wertung_erfolgt:
        available_input = False
        while not available_input:
            try:
                p = int(input("Welche Position soll gewertet werden? (1-13): ")) - 1
            except ValueError:
                print("Ungültige Eingabe: Bitte eine Zahl von 1 bis 13 eingeben.")
                continue

            if  0 <= p <= 12:
                if p <= 5:
                    if spielerarray[p] is not None:
                        print("Diese Position ist bereits belegt.")
                    else:
                        available_input = True
                else:
                    if spielerarray[p + 1] is not None:
                        print("Diese Position ist bereits belegt.")
                    else:
                        available_input = True
            else:
                print("Ungültige Position: Bitte eine Zahl von 1 bis 13 wählen.")



        #Auswertung des Zugs mit der Maske
        score = Maske(p, w1, w2, w3, w4, w5)


        if score == 0:
            print("\nDie Würfel passen nicht zur gewählten Kategorie.")
            while True:
                bstreich = input("Möchtest du in dieser Kategorie 0 Punkte eintragen (ja/nein)? ").strip().lower()
                if bstreich in ("ja", "j", "yes", "y"):
                    if p <= 5:
                        spielerarray[p] = 0
                    else:
                        spielerarray[p + 1] = 0
                    wertung_erfolgt = True
                    break
                elif bstreich in ("nein", "n", "no"):
                    print("\nBitte wähle eine andere Kategorie.")
                    break
                else:
                    print("\nUngültige Eingabe: Bitte mit 'ja' oder 'nein' antworten.")
        else:
            wertung_erfolgt = True

    if p <= 5:
        spielerarray[p] = score
    else:
        spielerarray[p + 1 ] = score
    
    try:
        total_score = spielerarray[14] + score
    except TypeError:
        total_score = score

    # Auswertung des Boni
    bonus = 35 if sum(x for x in spielerarray[:6] if isinstance(x, int)) >= 63 else 0
    if bonus > 0 and spielerarray[6] is None:
        print("Du bekommst den Bonus von 35 Punkten!")
        total_score += bonus
        spielerarray[6] = bonus 
    
    # Speicher der Gesamtpunktzahl im Spielerarray
    spielerarray[14] = total_score

    return spielerarray