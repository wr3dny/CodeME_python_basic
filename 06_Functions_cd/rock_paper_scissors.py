# 4 Napisz grę - kamień (k) / papier (p) / nożyce (n).
# - Użytkownik podaje jedną z 3 figur.
# - Komputer losuje jedną z 3 figur.
# - Sprawdź kto wygrał tę rundę.
# - Zmień kod tak, by użytkownik mógł podac liczbę rund.
# - Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# - Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
import random

# wygrany: (przegrany)
WINNERS = {
    'k': ('n', 'j'),
    'n': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}

CORRECT_VALUES = ('k', 'p', 'n', 'j', 's')


def get_comp_choice():
    return random.choice(CORRECT_VALUES)


def get_user_choice():
    while True:
        user_choice = input('Podaj wartość k - kamień, p - papier , n - nożyce, s - Spock, j - jaszczurka: ')
        if user_choice in CORRECT_VALUES:
            break

    return user_choice


def show_result(comp, user):
    if user == comp:
        print('Remis')
    elif comp in WINNERS[user]:
        print('Wygrywa użytkownika')
    else:
        print('Wygrywa komputer')


def main():
    while True:
        print('**** GRA K-P-N ****')

        comp = get_comp_choice()
        user = get_user_choice()
        print(f'komputer {comp}, user {user}')
        show_result(comp, user)

        play_again = input("Czy zagrać ponownie? [T / N] -> ")
        if play_again.upper() == 'N':
            break

    print('Dzięki za grę!')

main()

# def rock_paper_scissors(rounds):
#     player_score = 0
#     CPU_score = 0
#     player_turns = 0
#     while True:
#         player_number_turns = int(input('Ile chcesz rund rozegrać: '))
#         for player_turns in range(0, player_number_turns):
#             CPU_choice = random.choices(options_list)
#             player_choice = input('Podaj swój wybór kamień / nożyce / papier: ')
#             player_number_turns += 1
#             if CPU_choice == player_choice:
#                 print('Remis')
#             elif ('kamień' in CPU_choice and 'papier' in player_choice) or (
#                 'papier' in CPU_choice and 'nożyce' in player_choice) \
#                 or ('nożyce' in CPU_choice and 'kamień' in player_choice):
#                 print('Wygrana gracza')
#                 player_score += 1
#             else:
#                 print('Wygrana komputera')
#                 CPU_score += 1
#         if CPU_score > player_score:
#             print(f'Komputer wygrał {CPU_score} do {player_score}')
#         elif CPU_score == player_score:
#             print('Remis')
#         else:
#             print(f'Gracz wygrał {player_score} do {CPU_score}')




