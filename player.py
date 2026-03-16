#Hier werden Funtionen für die Interaktion mit dem Spieler definiert

#Spieler begrüßen und kurze Erklärung geben
def greet_players():
    print("Willkommen zu Kniffel!")
    print("Zielt ist es, durch Würfeln und kluge Entscheidungen die meisten Punkte zu erzielen.")
    print("Bis zu 8 Spieler können mitspielen.")

#Spieleranzahl abfragen und sicherstellen, dass sie zwischen 1 und 8 liegt
def get_number_of_players():
    while True:
        try:
            number = int(input("Wie viele Spieler möchten mitspielen? (1-8): "))
            if 1 <= number <= 8:
                return number
            else:
                print("Bitte eine Zahl zwischen 1 und 8 eingeben.")
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

#Spielernamen abfragen
def get_player_name(number):
    name = input(f"Name Spieler {number}: ")
    return name

#Funktion, um einen Eintrag in der Punkteliste für die Ausgabe zu formatieren
def convert_to_print(entry_number):
    if entry_number is None:
        return "___"
    elif entry_number == 0:
        return "XXX"
    elif entry_number < 10:
        return "  " + str(entry_number)
    elif entry_number < 100:
        return " " + str(entry_number)
    else:
        return str(entry_number)

#Gibt den aktuellen Punktestand eines Spielers aus (nutzt die convert_to_print Funktion)
def print_score_list(player_name, score_list):
    print(f"Aktueller Punktestand von {player_name}:")
    print(f"""    Einser:      {convert_to_print(score_list[0])}
    Zweier:      {convert_to_print(score_list[1])}
    Dreier:      {convert_to_print(score_list[2])}
    Vierer:      {convert_to_print(score_list[3])}
    Fünfer:      {convert_to_print(score_list[4])}
    Sechser:     {convert_to_print(score_list[5])}
    Bonus:       {convert_to_print(score_list[6])}
    Dreierpasch: {convert_to_print(score_list[7])}
    Viererpasch: {convert_to_print(score_list[8])}
    Full House:  {convert_to_print(score_list[9])}
    kl. Straße:  {convert_to_print(score_list[10])}
    gr. Straße:  {convert_to_print(score_list[11])}
    Kniffel:     {convert_to_print(score_list[12])}
    Chance:      {convert_to_print(score_list[13])}
    Summe:       {convert_to_print(score_list[14])}
    """)

#Testaufruf der print_score_list Funktion
#print_score_list("Max", [0, 6, None, 12, 5, 18, 0, 20, 30, None, 30, 40, None, 22, 315])


#Gibt die Endtabelle mit den Spielernamen und ihren Punkteständen aus (score_lists ist eine Liste von Listen, die die Punktestände aller Spieler enthält)
def print_final_score(player_names, score_lists):
    number_of_players = len(player_names)           #Anzahl der Spieler
    space_for_number = [0] * number_of_players      #Liste, die die Anzahl der Leerzeichen für jeden Spielernamen enthält, damit die Punkte in der Endtabelle ordentlich ausgerichtet sind
    space_for_name = [0] * number_of_players        #Liste, die die Anzahl der Leerzeichen für jeden Spielernamen enthält, damit die Namen in der Endtabelle ordentlich ausgerichtet sind

    for i in range(number_of_players):              #Wertet aus, wie viele Leerzeichen für jeden Spielernamen vor diesem und den Punkten in der Endtabelle stehen
        length_name = len(player_names[i])
        if length_name < 10:
            space_for_number[i] = 7                 #Die Anzahl derLeerzeichen inklusive bis zu drei Ziffern soll mindestens 10 betragen
            space_for_name[i] = 10 - length_name    #Leerzeichen vor dem Namen, damit die Namen in der Endtabelle ordentlich ausgerichtet sind
        else:
            space_for_number[i] = length_name - 2   #Wenn der Name 10 Zeichen lang oder länger ist, soll die Anzahl der Leerzeichen immer 3 weniger als die Anzahl der Zeichen im (Namen + ein Leerzeichen) sein
            space_for_name[i] = 1

    print("Endpunktestand:")                        #Gibt die Endtabelle mit den Spielernamen und ihren Punkteständen aus
    print("Spieler:     ", end="")
    for i in range(number_of_players):
        print(" " * space_for_name[i] + player_names[i] + "|", end="")
    print("\nEinser:      ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][0]) + "|", end="")
    print("\nZweier:      ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][1]) + "|", end="")
    print("\nDreier:      ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][2]) + "|", end="")
    print("\nVierer:      ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][3]) + "|", end="")
    print("\nFünfer:      ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][4]) + "|", end="")
    print("\nSechser:     ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][5]) + "|", end="")
    print("\nBonus:       ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][6]) + "|", end="")
    print("\nDreierpasch: ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][7]) + "|", end="")
    print("\nViererpasch: ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][8]) + "|", end="")
    print("\nFull House:  ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][9]) + "|", end="")
    print("\nkl. Straße:  ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][10]) + "|", end="")
    print("\ngr. Straße:  ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][11]) + "|", end="")
    print("\nKniffel:     ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][12]) + "|", end="")
    print("\nChance:      ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][13]) + "|", end="")
    print("\nSumme:       ", end="")
    for i in range(number_of_players):
        print(" " * space_for_number[i] + convert_to_print(score_lists[i][14]) + "|", end="")
    print()

#Testaufruf der print_final_score Funktion
#print_final_score(["Jan", "Anna", "Maximilian"], [[0, 6, 5, 12, 5, 18, 0, 20, 30, 0, 30, 40, 0, 22, 315], [4, 2, 9, 8, 10, 30, 35, 18, 24, 0, 25, 35, 0, 20, 300], [3, 4, 0, 16, 25, 30, 35, 0, 0, 25, 30, 40, 50, 26, 281]])

#Wertet den Gewinner oder die Gewinner aus und gibt die Namen der Gewinner und ihre Punktzahl aus
def winner(player_names, score_lists):
    max_score = 0
    winner_index = 0
    number_of_winners = 1

    for i in range(len(player_names)):                      #Findet die höchste Gesamtpunktzahl und den Index des Gewinners
        if score_lists[i][14] > max_score:
            max_score = score_lists[i][14]
            winner_index = i
            number_of_winners = 1
        elif score_lists[i][14] == max_score:         #Prüfung, ob es mehrere Gewinner gibt
            number_of_winners += 1

    if number_of_winners > 1:                               #Wenn es mehr als einen Gewinner gibt, werden Alle Namen und ihre Punktzahl ausgegeben
        print("Es haben ", end="")
        printed_winners_counter = 0                         #Variable zum zählen, wie viele Gewinner bereits ausgegeben wurden, damit die Namen der Gewinner mit ", " oder " und " getrennt werden können
        for i in range(len(player_names)):
            if score_lists[i][14] == max_score:
                printed_winners_counter += 1
                print(player_names[i], end="")
                if printed_winners_counter < number_of_winners - 1:
                    print(", ", end="")
                elif printed_winners_counter < number_of_winners:
                    print(" und ", end="")
        print(f" mit {max_score} Punkten gewonnen!")
    else:                                                   #Wenn es einen Gewinner gibt, wird nur der Name dieses Gewinners und seine Punktzahl ausgegeben
        print(f"Der Gewinner ist {player_names[winner_index]} mit {max_score} Punkten!")

#Testaufruf der winner Funktion
#winner(["Jan", "Anna", "Maximilian"], [[0, 6, 5, 12, 5, 18, 0, 20, 30, 0, 30, 40, 0, 22, 314], [4, 2, 9, 8, 10, 30, 35, 18, 24, 0, 25, 35, 0, 20, 314], [3, 4, 0, 16, 25, 30, 35, 0, 0, 25, 30, 40, 50, 26, 315]])