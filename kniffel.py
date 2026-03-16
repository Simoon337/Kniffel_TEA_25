# Kniffelprogramm
# authors: Alexander Hoppe, Simon Lämmle, Tobias Burgmaier
# date: 16.03.2026
''' Dies ist ein Kniffel-Programm, bei dem bis zu 8 Spieler miteinander spielen können.
    Das Würfeln, sowie die Punktespeicherung und -berechnung werden automatisch durchgeführt.
    Zum Schluss wird der Gewinner mit der höchsten Punktzahl bekannt gegeben.
    Die Regeln können in der README-Datei nachgelesen werden.'''

# Importieren der Funktionen aus den anderen Dateien
import player
import role_dice
import Auswertung_Zug_opt as auswertung

# Initialisierung der Punktelisten für 8 Einzelspieler
player_1_score_list = [None] * 15
player_2_score_list = [None] * 15
player_3_score_list = [None] * 15
player_4_score_list = [None] * 15
player_5_score_list = [None] * 15
player_6_score_list = [None] * 15
player_7_score_list = [None] * 15
player_8_score_list = [None] * 15
''' Reihenfolge der Punkte in einer Liste:
    0: Einser
    1: Zweier
    2: Dreier
    3: Vierer
    4: Fünfer
    5: Sechser
    6: Bonus
    7: Dreierpasch
    8: Viererpasch
    9: Full House
    10: kleine Straße
    11: große Straße
    12: Kniffel
    13: Chance
    14: Summe (wird am Ende berechnet)'''

# Initialisierung der benötigten Variablen
player_names = []
number_of_players = 0
score_lists = [player_1_score_list, player_2_score_list, player_3_score_list, player_4_score_list, player_5_score_list, player_6_score_list, player_7_score_list, player_8_score_list]

# Programmablauf
player.greet_players()
number_of_players = player.get_number_of_players()

for i in range(number_of_players):
    player_names.append(player.get_player_name(i + 1))

for rounds in range(13):
    for current_player in range(number_of_players):
        player.print_score_list(player_names[current_player], score_lists[current_player])
        print(f"{player_names[current_player]} ist am Zug.")
        score_lists[current_player] = auswertung.Auswertung_Zug(role_dice.roll_dice(), score_lists[current_player])

player.print_final_score(player_names, score_lists)
player.winner(player_names, score_lists)