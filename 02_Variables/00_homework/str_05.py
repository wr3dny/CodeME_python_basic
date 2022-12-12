# 5 Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy
#      wprowadzone wyrażenie jest palindromem

palindrom = input('Podaj palindrom: ')
mordnilap = palindrom[::-1]

if palindrom == mordnilap:
    print(f'Słowo {palindrom} jest palindromem')
else:
    print(f'Słowo {palindrom} nie jest palindromem')