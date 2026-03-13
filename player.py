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
print_score_list("Max", [0, 6, None, 12, 5, 18, 0, 20, 30, None, 30, 40, None, 22, 315])