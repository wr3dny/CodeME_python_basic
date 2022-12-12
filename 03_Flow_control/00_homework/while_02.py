# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

user_number = int(input('Find a secret number in range 0 - 20: '))
secret_number = 7

if user_number in range(0, 20):
    while user_number != secret_number:
        print('Wrong number. Please try again.')
        user_number = int(input('Find a secret number in range 0 - 20: '))
        if user_number == secret_number:
            print('You hit the right one')
else:
    print('Number out of range !')
