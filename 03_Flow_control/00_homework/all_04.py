# 4 Napisz grę - kamień (k) / papier (p) / nożyce (n).
# - Użytkownik podaje jedną z 3 figur.
# - Komputer losuje jedną z 3 figur.
# - Sprawdź kto wygrał tę rundę.
# - Zmień kod tak, by użytkownik mógł podac liczbę rund.
# - Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# - Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
import random

player_score = 0
CPU_score = 0
player_turns = 0
player_number_turns = int(input('Ile chcesz rund rozegrać: '))
options_list = ('kamień', 'nożyce', 'papier')

for player_turns in range(0, player_number_turns):
    CPU_choice = random.choice(options_list)
    player_choice = input('Podaj swój wybór kamień / nożyce / papier: ')
    player_number_turns += 1
    if ('kamień' in CPU_choice and 'kamień' in player_choice) or ('papier' in CPU_choice and 'papier' in player_choice)\
        or ('nożyce' in CPU_choice and 'nożyce' in player_choice):
        print('Remis')
    elif ('kamień' in CPU_choice and 'papier' in player_choice) or ('papier' in CPU_choice and 'nożyce' in player_choice)\
        or ('nożyce' in CPU_choice and 'kamień' in player_choice):
        print('Wygrana gracza')
        player_score += 1
    else:
        print('Wygrana komputera')
        CPU_score += 1
if CPU_score > player_score:
    print(f'Komputer wygrał {CPU_score} do {player_score}')
elif CPU_score == player_score:
    print('Remis')
else:
    print(f'Gracz wygrał {player_score} do {CPU_score}')



