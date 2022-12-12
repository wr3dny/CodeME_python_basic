# 1 Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#
#         atrybuty: imię, kolor sierści, rasę
#
#         metody: szczekaj, machaj ogonem
#
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class Dog:
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def machacz(self):
        return f'Dog named {self.name} is waging his tail'



def main():
    Dog.piorun = Dog('Piorun', 'black', 'mixed')
    Dog.bessie = Dog('Bessie', 'brown/white', 'big one')
    Dog.piorun.machacz()

if __name__ == '__main__':
    main()



print(Dog.piorun.color)
print(Dog.machacz(Dog.piorun))
