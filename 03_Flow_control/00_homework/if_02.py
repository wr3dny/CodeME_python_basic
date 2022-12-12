# 2 Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik,
# w przeciwnym wypadku wyświetl “Koniec”.

a = int(input('Give Your first number: '))
b = int(input('Give Your second number: '))

if a + b > 100:
    print(a +b)
else:
    print('End')