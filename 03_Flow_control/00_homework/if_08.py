# 8 Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę.
# Wyświetl liczby od największej do najmniejszej.

a = int(input('Give number #1: '))
b = int(input('Give number #2: '))
c = int(input('Give number #3: '))

if a > b and a > c:
    print('The biggest is \'a\'')
if b > a and b > c:
    print('The biggest is \'b\'')
if c > b and c > a:
    print('The biggest is \'c\'')
elif a == b or b == c or c == a:
    print('There is more then one biggest number')

print(sorted([a, b, c], reverse=True))

