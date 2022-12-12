# Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

elements = input("Podaj parzystą liczbę elementów, oddzielonych spacją -> ")
elements = elements.split()
middle = int(len(elements)/2)
middle_minus = int(middle - 1)

if len(elements) %2 == 0:
    print('Czy środkowe są takie same są takie same ->', elements[middle] == elements[middle_minus])
else:
    print('Nieparzysta ilość elementów')


