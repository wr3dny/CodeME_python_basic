season = input('podaj porę roku:')

if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')

# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

txt = input('Podaj dowolny ciąg znaków -> ')

counter_num = 0
counter_up = 0
counter_low = 0

for l in txt:
    if l.isdigit():
        counter_num += 1
        continue

    if l.isupper():
        counter_up += 1
        continue

    if l.islower():
        counter_low += 1

print(f'Text: {txt}')
print("Cyfry", counter_num)
print("Duże litery", counter_up)
print("Małe litery", counter_low)