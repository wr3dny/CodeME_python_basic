# 7 Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#
# Co wiemy o tych numerach tych kart?
#
#     All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#
#     MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#
#     American Express card numbers start with 34 or 37 and have 15 digits.

def is_card(number):
    return number.isdigit() and 13 <= len(number) <= 16

def is_visa(number):
    if len(number) in [13, 16] and number[0] == '4':
        return True
    else:
        return False

def is_mastercard(number):
    if len(number) == 16 and (51 <= int(number[0:2]) <= 55 or int(number[0:4]) in range(2221, 2720 + 1)):
        return True
    else:
        return False

def is_american_express(number):
    return len(number) == 15 and number.startwith(('34', '37'))

def main():
    while True:
        number = input('Podaj numer karty do sprawdzenia').replace(' ', '')
        if is_card(number):
            break
        else:
            print('To nie jest prawidłowy nr karty')
    # print('Visa', is_card(number))
    # print('Mastercard', is_mastercard(number))
    # print('American Express', is_american_express(number))
    if is_visa(number):
        print('To jest Visa')
    elif is_mastercard(number):
        print('To jest Mastercard')
    elif is_american_express(number):
        print('To jest Americna Express')
    else:
        print('Nieznany typ karty')

main()
