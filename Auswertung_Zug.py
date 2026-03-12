#############################
### Auswertung eines Zugs ###
###    Alexander Hoppe    ###
###      12.03.2026       ###
#############################

### In diesem Skript wird eine Funktion definiert, die einen einzelnen Zug auswertet.
### Diese Funktion nutzt die Funktion Zug, um die entgültigen Würfelkonstelationen auszuwerten und einem Spieler zuzuordnen.

### Legende Variablen / Arreys:
### pos: Arrey, der die Positionen im Spielerarrey erklährt
### Srielerarrey: Arrey, in dem die Punkte des aktuellen Spielers gespeichert werden. (-1="noch nicht belegt")
### b1,b2,b3,b4,b5: Boolsche Werte, die angeben, ob der jeweilige Würfel gewertet werden soll oder nicht
### bpos: Boolsche Variable, die angibt, ob die gewählte Position im Spielerarrey bereits belegt ist oder nicht
### p: Variable, in der die gewählte Position im Spielerarrey gespeichert wird
### s: Variable, in der die Summe der gewerteten Würfel gespeichert wird
### w1,w2,w3,w4,w5: Werte der 5 Würfel

pos = [1er, 2er, 3er, 4er, 5er, 6er, Dreierpasch, Viererpasch, FullHouse, KleineStrasse, GrosseStrasse, Kniffel, Chance]
def ZugAuswertung(Zug(w1,w2,w3,w4,w5),spielerarrey[]):
    int s=0
    print(pos)
    print(Spielerarrey)   
    p =  int(input("Welche Position soll gewertet werden? (1-13): "))
    b1 = bool(input("Soll " + int(w1) + " gewertet werden? (1/0): "))
    b2 = bool(input("Soll " + int(w2) + " gewertet werden? (1/0): "))
    b3 = bool(input("Soll " + int(w3) + " gewertet werden? (1/0): "))
    b4 = bool(input("Soll " + int(w4) + " gewertet werden? (1/0): "))
    b5 = bool(input("Soll " + int(w5) + " gewertet werden? (1/0): "))
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
    bool bpos = False
    for bpos ==False
        if Spielerarrey[p] == -1:
            Spielerarrey[p] = s
            bpos = True
        else:
            print("Diese Position ist bereits belegt.")
    return Spielerarrey

    
    
    
