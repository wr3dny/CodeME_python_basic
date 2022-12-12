#1
print('\n#1 Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i\n'
      '  zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.\n')
word = 'dlugieslowo'

print(word)

mid_index = word[int(len(word)//2)]
mid_idnex_after = word[int(len(word)//2 + 1)]
mid_idnex_befor = word[int(len(word)//2 - 1)]

word_3letter = mid_idnex_befor + mid_index + mid_idnex_after

print('Słowo z 3 środkowych liter: ', word_3letter)

#3
print('\n3# Do zmiennej quote przypisz zdanie: \n"Honesty is the first chapter in the book of wisdom.”')

quote = "Honesty is the first chapter in the book of wisdom."

print('\nPolicz wszystkie znaki w napisie')
print('Liczba znaków wynosi:', len(quote))

print('\nNie modyfikując zmiennej wyświetl słowo wisdom')
print(quote[-8:-1])

print('\nWyświetl tylko pierwszą połowę tekstu')
print(quote[:int(len(quote)//2)+1])

print('\nWyświetl tylko kropkę')
print(quote[-1:])

print('\nWyświetl od połowy tylko co trzecią literę cytatu')
print(quote[int(len(quote)//2)::3])

print('\nWyświetl ‘Hnsyi h is hpe ntebo fwso.')
print(quote[::2])

print('\nWyświetl cały cytat odwrotnie')
print(quote[::-1])

print('\nZamień wisdom na słowo friendship')
print(quote.replace('wisdom', 'friendship'))