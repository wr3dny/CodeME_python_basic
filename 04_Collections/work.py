# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
'''
while i <= 10:
    numbers = input("Dej 10 liczb: ")
    print(numbers)


# 1 .copy()
# 2 .sort()
# 3 .clear()
# 4 .count()
# 5 sum()
'''
# 3 Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

#user_list = input('Podaj liczby , sztuk 10, podzielone spacją')
#user_list = user_list.split('')

#print(user_list)

#print(' Czy pierwsza i ostatnia są takie same')
'''
if user_list[0] == user_list[-1]:
    print('Są takie same')
else:
    print('No nie pykło')
'''

# 5 Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach
# będzie znajdować się imię, nazwisko, zawód, np:

people = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]


for person in people:
    for index, value in enumerate(person):
        if index == 1:
            print(value, end=" | ")
        else:
            print(value, end=" ")
    print()


famous_persons = vfamous_persons.split('\'')

for n , s , o in famous_persons:
    print(f'Imię {n} nazwisko {s} a zawód to: {o}')

print(famous_persons[0])
print(famous_persons[1])
print(famous_persons[2])
print(famous_persons[3])

famous_persons = vfamous_persons.split('\'')

for n , s , o in famous_persons:
    print(f'Imię {n} nazwisko {s} a zawód to: {o}')
