#############################
### Auswertung eines Zugs ###
###    Alexander Hoppe    ###
###      12.03.2026       ###
#############################

### In diesem Skript wird eine Funktion definiert, die einen einzelnen Zug auswertet.
### Diese Funktion nutzt die Funktion Zug, um die entgültigen Würfelkonstelationen auszuwerten und einem Spieler zuzuordnen.

### Legende Variablen / Arreys (Auswertung_Zug):
### pos: Arrey, der die Positionen im Spielerarrey erklährt
### Srielerarrey: Arrey, in dem die Punkte des aktuellen Spielers gespeichert werden. (None="noch nicht belegt")
### b1,b2,b3,b4,b5: Boolsche Werte, die angeben, ob der jeweilige Würfel gewertet werden soll oder nicht
### bpos: Boolsche Variable, die angibt, ob die gewählte Position im Spielerarrey bereits belegt ist oder nicht
### p: Variable, in der die gewählte Position im Spielerarrey gespeichert wird
### s: Variable, in der die Summe der gewerteten Würfel gespeichert wird
### w1,w2,w3,w4,w5: Werte der 5 Würfel


from Kniffel_TEA_25.Maske_Positionen import Maske

pos = ["Einer", "Zweier", "Dreier", "Vierer", "Fünfer", "Sexer", "Dreierpasch", "Viererpasch", "FullHouse", "KleineStrasse", "GrosseStrasse", "Kniffel", "Chance"]
def Auswertung_Zug(w1: int, w2: int, w3: int, w4: int, w5: int, eingabearray: list):                                                                         
    spielerarray = eingabearray 
    print(pos)                                                              #Ausgabe der möglichen Positionen im Spiel
    print(spielerarray)                                                     #Ausgabe des Spielerarreys, damit der Spieler sieht, welche Positionen bereits belegt sind
    p =  int(input("Welche Position soll gewertet werden? (1-13): ")-1)       #Abfrage der Position, die gewertet werden soll
    b1 = bool(Maske [0])       #Abfrage Wertung der einzelnen Würfel
    b2 = bool(Maske [1])       #Abfrage Wertung der einzelnen Würfel
    b3 = bool(Maske [2])       #Abfrage Wertung der einzelnen Würfel
    b4 = bool(Maske [3])       #Abfrage Wertung der einzelnen Würfel
    b5 = bool(Maske [4])       #Abfrage Wertung der einzelnen Würfel
    s = Maske [5]                                                                #Initialisierung der Summe der gewerteten Würfel und anschließende Berechnung
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
    bpos = False                                                       #Prüfung, ob der Spieler die gewählte Position schon belegt hat mit anschließender Belegung
    for bpos in False:
        if spielerarray[p] is None:
            spielerarray[p] = s
            bpos = True
        elif s==0 and b1==False and b2==False and b3==False and b4==False and b5==False:   #Prüfung, ob etwas überschrieben wird
            print("ungültige Eingabe, da die Bedingungen für die gewählte Kategorie mit den gewürfelten Würfeln nicht übereinstimmt")
            bstreich = bool(input("Möchten sie ind dieser Kategorie 0Punkte (streichen)?")) #Abfrage Kategorie streichen
            if bstreich == True:
                spielerarray[p] = 0
                bpos = True
            else:
                print("Bitte wählen sie eine andere Kategorie.")
                return spielerarray
        else:
            print("Diese Position ist bereits belegt.")
    return spielerarray                                                     #Rückgabe des aktualisierten Spielerarreys, damit die Punkte in der Hauptschleife weiterverwendet werden können

    
    
    
