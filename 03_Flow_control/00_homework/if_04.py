# 4 Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy
# zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

variable = input('Write something: ')


if len(variable) > 5 and 'a' in variable:
    print(variable.replace('a', 'i'))
else:
    print('Nothing to do here')
