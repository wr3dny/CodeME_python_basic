# 2 Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
empty_list_numbers = []
i = 0
print('Wymagam podania 10 liczb.')
while i in range(0, 10):
    user_number = int(input("Podaj liczbę: "))
    empty_list_numbers.append(user_number)
    i += 1
    print(f'Podałeś już {i} z 10 liczb')

odd_list = []
for j in empty_list_numbers:
    if j %2 != 0:
        odd_list.append(j)
print(f'Z podanych liczb, nieparzyste to {odd_list}')
