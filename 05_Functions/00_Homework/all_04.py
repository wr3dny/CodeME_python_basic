# 4 Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić komunikat:
# “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def in_range(n, low, upper):
    if n in range(low, upper):
        return f'Tak, liczba {n} znajduje się w zadanym zakresie'
    else:
        return f'Nie, liczba {n} jest z poza zakresu'

def main():
    n = int(input('Podaj liczbę: '))
    l = int(input('Podaj dolny zakres: '))
    u = int(input('Podaj górny zakres: '))

    result = in_range(n, l, u)
    print(result)

main()
