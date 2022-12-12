# 3  Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją
'''
tab = [
    ['-', '-', '-'],
  ['-', '-', '-'],
  ['-', '-', '-']
]

for row in tab:
    for i in row:
        print(i, end=' ')
    print()
'''

n = int(input('Podaj liczbę:'))
tab = [['_'] * n ] * n
for row in tab:
    for i in row:
        print(i, end=' ')
    print()