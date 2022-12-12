#3 Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 -
# bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

heroes = int(input('Rate heroes: '))
story = int(input('Rate story'))
lenght = int(input('Rate lenght: '))

rate = (heroes + story + lenght) / 3

if rate >= 7:
    print('Worth of Your time')
elif rate >= 5:
    print('Could be better')
else:
    print('Unworthy piece of paper')

