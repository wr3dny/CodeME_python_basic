# 5 Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
serached_number = 13

def cold_hot(number):
    if number == serached_number:
        return 'Trafiony zatopiony'
    elif (serached_number - 15) <= number <= (serached_number + 15):
        return 'Gorąco'
    elif (serached_number - 30) <= number <= (serached_number + 30):
        return 'Ciepławo'
    elif (serached_number - 45) <= number <= (serached_number + 45):
        return 'Wiosna w Polsce'
    elif (serached_number - 60) <= number <= (serached_number + 60):
        return 'Zimno'
    else:
        return 'Piekło zamarzło'

def main():
    while True:
        n = int(input('Podaj liczbę: '))
        result = cold_hot(n)
        number_in_def = result
        print(result)


main()
