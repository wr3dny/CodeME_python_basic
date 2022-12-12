# 6 Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat
# “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

number_by_me = 13
asked_number = int(input("Give me Your number ( from 1 to 100): "))

if asked_number == number_by_me:
    print('Bull\'s Eye !')
else:
    print('You missed')
