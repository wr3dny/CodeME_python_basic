#1
print('\nPoproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez \n '
      'użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat \n'
      '“Twoja liczba jest podzielna przez 3”.')

x = int(input('Podaj lioczbę:'))
if x % 3 == 0:
    print('podzielna')
else:
    print('niepodzielna')

