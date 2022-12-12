for val in "string":
  if val == "i":
      break
  print(val)

print("Koniec")

for letter in "string":
  if letter == "i":
      continue
  print(letter, end= '**')


print("Koniec")

print('-----')

while True:
    x = int(input('Podaj liczbę od 1 - 10'))

    if 1 <= x <= 10:
        break
    else:
        print('To nie jest liczba z zakresu')

print('Hello')