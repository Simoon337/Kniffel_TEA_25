#############################
### Auswertung eines Zugs ###
###    Alexander Hoppe    ###
###      12.03.2026       ###
#############################

### In diesem Skript wird eine Funktion definiert, die einen einzelnen Zug auswertet.
### Diese Funktion nutzt die Funktion Zug, um die entgültigen Würfelkonstelationen auszuwerten und einem Spieler zuzuordnen.

### Legende Variablen / Arreys (Auswertung_Zug):
### pos: Arrey, der die Positionen im Spielerarrey erklährt
### Srielerarrey: Arrey, in dem die Punkte des aktuellen Spielers gespeichert werden. (-1="noch nicht belegt")
### b1,b2,b3,b4,b5: Boolsche Werte, die angeben, ob der jeweilige Würfel gewertet werden soll oder nicht
### bpos: Boolsche Variable, die angibt, ob die gewählte Position im Spielerarrey bereits belegt ist oder nicht
### p: Variable, in der die gewählte Position im Spielerarrey gespeichert wird
### s: Variable, in der die Summe der gewerteten Würfel gespeichert wird
### w1,w2,w3,w4,w5: Werte der 5 Würfel


from Kniffel_TEA_25.Maske_Positionen import Maske

pos = [1er, 2er, 3er, 4er, 5er, 6er, Dreierpasch, Viererpasch, FullHouse, KleineStrasse, GrosseStrasse, Kniffel, Chance]
def Auswertung_Zug(Zug(w1,w2,w3,w4,w5),spielerarrey[]):                     #Einlesen des Spielerarreys und derWürfelwerte                                                                
    print(pos)                                                              #Ausgabe der möglichen Positionen im Spiel
    print(spielerarrey[])                                                     #Ausgabe des Spielerarreys, damit der Spieler sieht, welche Positionen bereits belegt sind
    p =  int(input("Welche Position soll gewertet werden? (1-13): ")-1)       #Abfrage der Position, die gewertet werden soll
    b1 = bool(Maske [0])       #Abfrage Wertung der einzelnen Würfel
    b2 = bool(Maske [1])       #Abfrage Wertung der einzelnen Würfel
    b3 = bool(Maske [2])       #Abfrage Wertung der einzelnen Würfel
    b4 = bool(Maske [3])       #Abfrage Wertung der einzelnen Würfel
    b5 = bool(Maske [4])       #Abfrage Wertung der einzelnen Würfel
    int s = Maske [5]                                                                #Initialisierung der Summe der gewerteten Würfel und anschließende Berechnung
    if b1 == True:
        s = s + w1
    if b2 == True:
        s = s + w2
    if b3 == True:
        s = s + w3
    if b4 == True:
        s = s + w4
    if b5 == True:
        s = s + w5
    bool bpos = False                                                       #Prüfung, ob der Spieler die gewählte Position schon belegt hat mit anschließender Belegung
    for bpos ==False
        if spielerarrey[p] == -1:
            spielerarrey[p] = s
            bpos = True
        else:
            print("Diese Position ist bereits belegt.")
    return spielerarrey                                                     #Rückgabe des aktualisierten Spielerarreys, damit die Punkte in der Hauptschleife weiterverwendet werden können

    
    
    
