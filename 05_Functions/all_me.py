def my_book(book, score):
   print(book + ' ' + score)

book = input('Podaj nazwę ksiązki: ')
score = input('podaj ocenę ksiązki: ')

my_book(book, score)

print('-----')

def book_number():
    print('Book index', index)

index = int(input('Podaj nnumer książki: '))
book_number(index)

print('-----')

book_number_base = (1, 2, 3, 4, 5)

def error(number):
    if number not in book_number_base:
        print('Out side of range')
number = int(input('Number (1-5): '))

error(number)