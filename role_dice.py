


import random #Random wird importiert, um die Augenzahlen der Würfel zufällig zu generieren

# Hier wird die Funktion zur Überprüfung der gehaltenen Würfel auf Gültigkeit definiert
def is_keep_valid(keep_dice_list, current_roll):
    
    for value in set(keep_dice_list):
        if keep_dice_list.count(value) > current_roll.count(value):
            return False
    return True

# Hier wird die Würfelfunktion definiert, die den Ablauf des Würfelns enthält
def roll_dice():
    #Führt bis zu drei Würfe eines Kniffel-Zuges aus
    #Lässt den Spieler wählen, ob und welche Würfel er behalten möchte
    
    dice_faces = [1, 2, 3, 4, 5, 6] 
    turns = 1                       
    keep_dice_list = []             
    answer_valid = False            # Variable zur Überprüfung der Gültigkeit der Antwort des Spielers
    choice_valid = False            # Variable zur Überprüfung der Gültigkeit der Auswahl der zu behaltenden Würfel
    accepted_answer = False         # Variable zur Überprüfung der Gültigkeit der Antwort, wenn der Spieler alle Würfel behalten möchte
    dices = [0, 0, 0, 0, 0]
    
    while turns <= 3:
        
        i = 1
        while i <= len(dices): #Hier wird der Wurf generiert, entweder durch random oder gehaltene Würfel
            if i > len(keep_dice_list):
                dices[i-1] = random.choice(dice_faces)
            else:
                dices[i-1] = keep_dice_list[i-1]
            i += 1

        print(f"Du hast folgende Augenzahlen gewürfelt: {dices[0]}, {dices[1]}, {dices[2]}, {dices[3]}, {dices[4]}")
        
        if turns < 3: # Überprüfen, ob der Spieler noch Würfe übrig hat, bevor er gefragt wird, ob er erneut würfeln möchte
            print(f"Du hast noch {3 - turns} Würfe übrig.")
            answer_valid = False
            continue_rolling = ""
            while answer_valid == False:  #Wiederholte Abfrage, ob der Spieler erneut würfeln möchte, bis eine gültige Antwort gegeben wird
                continue_rolling = input("Möchtest du noch einmal würfeln? (ja/nein): ").lower()
                if continue_rolling in ["ja", "nein"]:
                    answer_valid = True
                else:                   
                    print("Ungültige Eingabe. Bitte gib 'ja' oder 'nein' ein.")  
            if continue_rolling == "ja":
                choice_valid = False
                keep_dice_list = []
                while choice_valid == False:
                    keep_dice = input("Welche Würfel möchtest du behalten? (Gib die Augenzahlen der Würfel ein,\ndie du behalten möchtest, getrennt durch Kommas.\nPro Eingabe wird ein Würfel gehalten): ")
                    keep_dice_entries = [x.strip() for x in keep_dice.split(",") if x.strip() != ""] #Formation der Eingabe in eine Liste ohne Lehrzeichen und Kommas
                    if len(keep_dice_entries) > 5:
                        print("Ungültige Eingabe. Du kannst maximal 5 Würfel behalten.")
                        continue
                    elif len(keep_dice_entries) ==5: #Abfrage, ob der Spieler alle 5 Würfel behalten möchte
                        print(f"Wenn du 5 Würfel behalten möchtest\nwird dein Zug mit deinen aktuellen Würfeln {dices} beendet.")
                        accepted_answer = False
                        while accepted_answer == False: 
                            accept_keep_all = input("Möchtest du alle 5 Würfel behalten? (ja/nein): ").lower()
                            if accept_keep_all in ["ja", "nein"]:
                                accepted_answer = True
                            else:
                                print("Ungültige Eingabe. Bitte gib 'ja' oder 'nein' ein.")
                        if accept_keep_all == "ja": 
                            turns = 4  # Beendet die Schleife, da der Spieler alle Würfel behalten möchte
                            choice_valid = True
                        else: 
                            continue
                    try: #Umwandlung der Spielereingabe in Ganzzahlen, Fehlermeldung, falls dies nicht möglich ist
                        keep_dice_list = [int(x) for x in keep_dice_entries]
                    except ValueError:
                        print("Ungültige Eingabe. Bitte gib nur Zahlen von 1 bis 6 getrennt durch Kommas ein.")
                        continue
                    if not all(1 <= x <= 6 for x in keep_dice_list):
                        print("Ungültige Eingabe. Bitte gib nur Zahlen von 1 bis 6 ein.")
                        continue
                    if not is_keep_valid(keep_dice_list, dices):#Aufrufen der Überprüfungsfunktion
                        print("Ungültige Eingabe.\nDu hast mehr Würfel einer Zahl behalten als im aktuellen Wurf vorhanden.")
                        continue 
                    choice_valid = True 
                if len(keep_dice_list) == 0 and turns < 4:                  
                    print("Es wird erneut gewürfelt.\nEs wurden keine Würfel gehalten, daher wurden alle Würfel erneut gewürfelt.")
                elif len(keep_dice_list) > 0 and turns < 4:
                    print(f"Du hast folgende Würfel behalten: {keep_dice_list}")
                    print ("Es wird erneut gewürfelt.\nDie behaltenen Würfel werden automatisch in den nächsten Wurf übernommen.")
                    print ("\n")
                else: 
                    print("Du hast den Wurf mit folgenden Würfeln beendet:")
            else: 
                print("Du hast dich entschieden, nicht mehr zu würfeln. Deine aktuellen Würfel werden beibehalten.")
                turns = 4  # Beendet die Schleife, da der Spieler nicht mehr würfeln möchte.
        else:
            print("Du hast keine Würfe mehr übrig. Deine aktuellen Würfel werden beibehalten.")
        turns += 1 #Erhöht die Anzahl der Würfe um 1, um den Ablauf der Schleife zu steuern

    print(dices[0], dices[1], dices[2], dices[3], dices[4]) 
    return [dices[0], dices[1], dices[2], dices[3], dices[4]] #Rückgabe der finalen Würfelwerte als Liste     