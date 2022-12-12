#5 Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random
CPU_number = random.randint(1, 100)

i = 0

def cold_hot(number):
    if abs(CPU_number - number):
        for i in range(0, 6):
            player_number = int(input('Your number: '))
            diff = CPU_number - player_number
        if player_number == CPU_number:
            print('Wygrywasz')
        else:
            if 0 < diff < 15:
                print('Ciepło')
            if 15 <= diff < 30:
                print('Chłodno')
            if 30 <= diff < 60:
                print('Zimno')
            if 61 <= diff <= 99:
                print('Piekło zamarzło')
    print('Koniec')

cold_hot(1)