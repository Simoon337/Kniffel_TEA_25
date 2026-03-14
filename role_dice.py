


import random #Random wird importiert, um die Augenzahlen der Würfel zufällig zu generieren.

# Hier wird die Funktion zur Überprüfung der gehaltenen Würfel auf Gültigkeit definiert.
def is_keep_valid(keep_dice_list, current_roll):

    #keep_dice_list: Liste der Augenzahlen, die der Spieler behalten möchte.
    #current_roll: Liste der aktuellen Würfelergebnisse.
    #Rückgabe: True, wenn jede Augenzahl nicht öfter gewählt wurde als vorhanden.
    
    for value in set(keep_dice_list):
        if keep_dice_list.count(value) > current_roll.count(value):
            return False
    return True

# Hier wird die Würfelfunktion definiert, die den Ablauf des Würfelns enthält.
def roll_dice():
    #Führt bis zu drei Würfe eines Kniffel-Zuges aus und lässt den Spieler Würfel behalten.
    #Hierfür lässt sie den Spieler wählen, ob und welche Würfel er behalten möchte.
    
    dice_faces = [1, 2, 3, 4, 5, 6] # Mögliche Augenzahlen auf den Würfeln
    turns = 1                       # Zählt die Anzahl der Würfe (maximal 3)
    keep_dice_list = []             # Liste der Augenzahlen der Würfel, die der Spieler behalten möchte
    answer_valid = False            # Variable zur Überprüfung der Gültigkeit der Antwort des Spielers
    choice_valid = False            # Variable zur Überprüfung der Gültigkeit der Auswahl der zu behaltenden Würfel
    accepted_answer = False         # Variable zur Überprüfung der Gültigkeit der Antwort, wenn der Spieler alle Würfel behalten möchte
    dices = [0, 0, 0, 0, 0]         # Liste, die die aktuellen Augenzahlen der 5 Würfel speichert
    

    while turns <= 3:
        if len(keep_dice_list) == 0:                    #Generieren der Augenzahlen für die 5 Würfel, wenn keine Würfel behalten werden
            dices[0] = random.choice(dice_faces)
            dices[1] = random.choice(dice_faces)
            dices[2] = random.choice(dice_faces)
            dices[3] = random.choice(dice_faces)
            dices[4] = random.choice(dice_faces)
        elif len(keep_dice_list) == 1:                  #Generieren der Augenzahlen für die 5 Würfel, wenn 1 Würfel behalten wird. Der behaltene Würfel wird automatisch in den nächsten Wurf übernommen
            dices[0] = keep_dice_list[0]
            dices[1] = random.choice(dice_faces)
            dices[2] = random.choice(dice_faces)
            dices[3] = random.choice(dice_faces)
            dices[4] = random.choice(dice_faces)
        elif len(keep_dice_list) == 2:                  #Generieren der Augenzahlen für die 5 Würfel, wenn 2 Würfel behalten werden. Die behaltenen Würfel werden automatisch in den nächsten Wurf übernommen    
            dices[0] = keep_dice_list[0]
            dices[1] = keep_dice_list[1]
            dices[2] = random.choice(dice_faces)
            dices[3] = random.choice(dice_faces)
            dices[4] = random.choice(dice_faces)
        elif len(keep_dice_list) == 3:                  #Generieren der Augenzahlen für die 5 Würfel, wenn 3 Würfel behalten werden. Die behaltenen Würfel werden automatisch in den nächsten Wurf übernommen
            dices[0] = keep_dice_list[0]
            dices[1] = keep_dice_list[1]
            dices[2] = keep_dice_list[2]
            dices[3] = random.choice(dice_faces)
            dices[4] = random.choice(dice_faces)
        elif len(keep_dice_list) == 4:                  #Generieren der Augenzahlen für die 5 Würfel, wenn 4 Würfel behalten werden. Die behaltenen Würfel werden automatisch in den nächsten Wurf übernommen
            dices[0] = keep_dice_list[0]
            dices[1] = keep_dice_list[1]
            dices[2] = keep_dice_list[2]
            dices[3] = keep_dice_list[3]
            dices[4] = random.choice(dice_faces)
        print(f"Du hast folgende Augenzahlen gewürfelt: {dices[0]}, {dices[1]}, {dices[2]}, {dices[3]}, {dices[4]}")
        if turns < 3: # Überprüfen, ob der Spieler noch Würfe übrig hat, bevor er gefragt wird, ob er erneut würfeln möchte
            print(f"Du hast noch {3 - turns} Würfe übrig.") #Ausgabe der verbleibenden Würfe.
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
                keep_dice_list = [] #Leeren der Keep-Dice-Liste, um die neuen Würfel zu generieren, wenn der Spieler erneut würfeln möchte
                while choice_valid == False:
                    keep_dice = input("Welche Würfel möchtest du behalten? (Gib die Augenzahlen der Würfel ein,\ndie du behalten möchtest, getrennt durch Kommas): ")
                    keep_dice_entries = [x.strip() for x in keep_dice.split(",") if x.strip() != ""] #Formation der Eingabe in eine Liste ohne Lehrzeichen und Kommas
                    if len(keep_dice_entries) > 5: #Fehlermeldung, wenn über 5 Würfel behalten werden sollen
                        print("Ungültige Eingabe. Du kannst maximal 5 Würfel behalten.")
                        continue
                    elif len(keep_dice_entries) ==5: #Abfrage, ob der Spieler alle 5 Würfel behalten möchte, wenn er 5 Augenzahlen eingegeben hat. Die Augenzahlen werden nicht überprüft, da der Spieler alle Würfel behalten möchte
                        print(f"Wenn du 5 Würfel behalten möchtest\nwird dein Zug mit deinen aktuellen Würfeln {dices} beendet.")
                        accepted_answer = False
                        while accepted_answer == False: #Abfrage, ob der Spieler alle 5 Würfel behalten und seinen Zug beenden möchte oder nicht, bis eine gültige Antwort gegeben wird
                            accept_keep_all = input("Möchtest du alle 5 Würfel behalten? (ja/nein): ").lower()
                            if accept_keep_all in ["ja", "nein"]:
                                accepted_answer = True
                            else:
                                print("Ungültige Eingabe. Bitte gib 'ja' oder 'nein' ein.")
                        if accept_keep_all == "ja": #Wenn der Spieler alle 5 Würfel behalten und seinen Zug beenden möchte, geschieht dies hier
                            turns = 4  # Beendet die Schleife, da der Spieler alle Würfel behalten möchte.
                            choice_valid = True
                        else: #Möchte der Spieler nicht alle 5 Würfel behalten, wird er erneut gefragt, welche Würfel er behalten will
                            continue
                    try: #Hier wird die Eingabe der zu behaltenden Würfel in eine Liste von Ganzzahlen umgewandelt.
                        keep_dice_list = [int(x) for x in keep_dice_entries]
                    except ValueError: #Fehlermeldung, falls keine gültigen Zahlen eingegeben wurden.
                        print("Ungültige Eingabe. Bitte gib nur Zahlen von 1 bis 6 getrennt durch Kommas ein.")
                        continue
                    if not all(1 <= x <= 6 for x in keep_dice_list): #Fehlermeldung, falls zahlen außerhalb von 1-6 eingegeben wurden
                        print("Ungültige Eingabe. Bitte gib nur Zahlen von 1 bis 6 ein.")
                        continue
                    if not is_keep_valid(keep_dice_list, dices):# Prüfen, ob die gewählten Augenzahlen in dices in der gewählten Häufigkeit vorkommen. Fehlermeldung, falls dies nicht der Fall ist.
                        print("Ungültige Eingabe.\nDu hast mehr Würfel einer Zahl behalten als im aktuellen Wurf vorhanden.")
                        continue 
                    choice_valid = True #Wenn alle Kriterien an die Eingabe eingehalten wurden, wird die Schleife verlassen
                if len(keep_dice_list) == 0 and turns < 4: #Erklärung des Ablaufs, zum besseren Verständnis des Spielers                   
                    print("Es wird erneut gewürfelt.\nEs wurden keine Würfel gehalten, daher wurden alle Würfel erneut gewürfelt.")
                elif len(keep_dice_list) > 0 and turns < 4: #Erklärung des Ablaufs, zum besseren Verständnis des Spielers
                    print(f"Du hast folgende Würfel behalten: {keep_dice_list}") #Ausgabe der vom Spieler gehaltenen Würfel
                    print ("Es wird erneut gewürfelt.\nDie behaltenen Würfel werden automatisch in den nächsten Wurf übernommen.")
                    print ("\n")
                else: #Hinweis, dass der Zug beendet wird
                    print("Du hast den Wurf mit folgenden Würfeln beendet:")
            else: # Hinweis, dass der Spieler den Zug mit den aktuellen Würfeln beendet
                print("Du hast dich entschieden, nicht mehr zu würfeln. Deine aktuellen Würfel werden beibehalten.")
                turns = 4  # Beendet die Schleife, da der Spieler nicht mehr würfeln möchte.
        else: # Hinweis, dass der Spieler keine Würfe mehr übrig hat und der Zug mit den aktuellen Würfeln beendet wird
            print("Du hast keine Würfe mehr übrig. Deine aktuellen Würfel werden beibehalten.")
        turns += 1 #Erhöht die Anzahl der Würfe um 1, um den Ablauf der Schleife zu steuern

    print(dices[0], dices[1], dices[2], dices[3], dices[4]) #Anzeigen der finalen Würfelwerte nach dem letzten Wurf
    return [dices[0], dices[1], dices[2], dices[3], dices[4]] #Rückgabe der finalen Würfelwerte als Liste


            