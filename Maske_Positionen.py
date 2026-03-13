######################################
### Maske der einzelnen Positionen ###
###         Alexander Hoppe        ###
###           12.03.2026           ###
######################################

#In diesem Skript werden die unterschiedlichen Positionsmasken im Spiel für die Auswertung definiert.

def Maske(p,w1,w2,w3,w4,w5):
    import operator
    b1 = False
    b2 = False 
    b3 = False
    b4 = False
    b5 = False
    s = 0
    if p < 6:                                 #Prüfung der Würfel für Position 1-6 mit anschließender Belegung der Maske
        if w1==p+1:
            b1 = True
        if w2==p+1:
            b2 = True
        if w3==p+1:
            b3 = True
        if w4==p+1:
            b4 = True
        if w5==p+1:
            b5 = True

    if p == 7:                               # Prüfung der Würfel für Position Dreierpasch mit anschließender Belegung der Maske
        if w1==w2 and w2==w3:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w1==w3 and w3==w4:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w1==w4 and w4==w5:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w2==w3 and w3==w4:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w2==w3 and w3==w5:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w2==w4 and w4==w5:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w3==w4 and w4==w5:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
    if p == 8:                                  # Prüfung der Würfel für Position Viererpasch mit anschließender Belegung der Maske
        if w1==w2 and w3==w4 and w1==w3:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w1==w2 and w3==w5 and w1==w3:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w1==w2 and w4==w5 and w1==w4:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w1==w3 and w4==w5 and w1==w4:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
        if w2==w3 and w4==w5 and w2==w4:
            b1 = True
            b2 = True
            b3 = True
            b4 = True
            b5 = True
    if p == 9:                                  # Prüfung der Würfel für Position FullHouse mit anschließender Ausgabe der Punkte
        if w1==w2 and w2==w3 and w4==w5 and w1!=w4:
            s = 25
        if w1==w2 and w2==w4 and w3==w5 and w1!=w3:
           s = 25
        if w1==w2 and w2==w5 and w3==w4 and w1!=w3:
            s = 25
        if w1==w3 and w3==w4 and w2==w5 and w1!=w2:
            s = 25
        if w1==w3 and w3==w5 and w2==w4 and w1!=w2:
            s = 25
        if w1==w4 and w4==w5 and w2==w3 and w1!=w2:
            s = 25
    if p == 10:                                                                      # Prüfung der Würfel für Position Kleine Straße mit anschließender Ausgabe der Punkte
        if w1==1 or w2==1 or w3==1 or w4==1 or w5==1:
            if w1==2 or w2==2 or w3==2 or w4==2 or w5==2:
                if w1==3 or w2==3 or w3==3 or w4==3 or w5==3:
                    if w1==4 or w2==4 or w3==4 or w4==4 or w5==4:
                        s = 30
        if w1==2 or w2==2 or w3==2 or w4==2 or w5==2:
            if w1==3 or w2==3 or w3==3 or w4==3 or w5==3:
                if w1==4 or w2==4 or w3==4 or w4==4 or w5==4:
                    if w1==5 or w2==5 or w3==5 or w4==5 or w5==5:
                        s = 30
        if w1==3 or w2==3 or w3==3 or w4==3 or w5==3:
            if w1==4 or w2==4 or w3==4 or w4==4 or w5==4:
                if w1==5 or w2==5 or w3==5 or w4==5 or w5==5:
                    if w1==6 or w2==6 or w3==6 or w4==6 or w5==6:
                        s = 30
    if p == 11:                                                                      # Prüfung der Würfel für Position Große Straße mit anschließender Ausgabe der Punkte   
        if w1==1 or w2==1 or w3==1 or w4==1 or w5==1:
            if w1==2 or w2==2 or w3==2 or w4==2 or w5==2:
                if w1==3 or w2==3 or w3==3 or w4==3 or w5==3:
                    if w1==4 or w2==4 or w3==4 or w4==4 or w5==4:
                        if w1==5 or w2==5 or w3==5 or w4==5 or w5==5:
                            s = 40
        if w1==2 or w2==2 or w3==2 or w4==2 or w5==2:
            if w1==3 or w2==3 or w3==3 or w4==3 or w5==3:
                if w1==4 or w2==4 or w3==4 or w4==4 or w5==4:
                    if w1==5 or w2==5 or w3==5 or w4==5 or w5==5:
                        if w1 == 6 or w2 == 6 or w3 == 6 or w4 == 6 or w5 == 6:
                            s = 40
    if p == 12:                                                                      # Prüfung der Würfel für Position Kniffel mit anschließender Ausgabe der Punkte
        if w1==w2 and w2==w3 and w3==w4 and w4==w5:
            s = 50
    if p == 13:                                                                      # Prüfung der Würfel für Position Chance mit anschließender Ausgabe der Punkte
        b1 = True
        b2 = True
        b3 = True
        b4 = True
        b5 = True
    return [b1,b2,b3,b4,b5,s]