# 5 Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość
# conajmniej 8 znaków.Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne
# komunikaty w zależności od rodzaju błędu.

password = input('Give me Your password: ')

if len(password) < 8:
    print('Password is to short')
if password.isalpha() == True:
    print('Need a number')
if password.isdigit() == True:
    print("You need letters")
if password.isupper() == True:
    print('Need lower letter')
if password.islower() == True:
    print('Need upper letter')
else:
    print('Password is correct')