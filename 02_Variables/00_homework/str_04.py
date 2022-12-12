# 4 Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

book = input('Podaj tytuł książki: ')
author = input('Podaj autora książki (nazwisko): ')
number_pages = input ('Podaj ilość stron: ')

book2 = book.replace(' ','')

# - Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową

print(f'Ciąg {book} zawiera same litery', book2.isalpha())
print(f'Ciąg {author} zawiera same litery', author.isalpha())
print(f'Ciąg {number_pages} zawiera same cyfry', number_pages.isdigit())

# - Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

print(book.capitalize())
print(author.capitalize())

# - Połącz dane w jeden ciąg book za pomocą spacji
print(book + ' ' + author + ' ' + number_pages)

# - Policz liczbę wszystkich znaków w napisie book
book3 = 'book'
print(len(book3))