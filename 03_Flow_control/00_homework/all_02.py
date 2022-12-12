# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = input('Give me Your word: ')

# pętla

print('-----')

for i in range(len(txt)):
    if (i % 2 != 0):
        print(txt[i])

# slicing

print('-----')

sliced_txt = txt[1::2]
print(sliced_txt)
