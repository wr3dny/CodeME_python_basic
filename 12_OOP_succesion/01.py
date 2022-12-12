class Animal:
    def eat(self):
        return 'need to eat'

class Mamal(Animal):
    def lifeborn(self):
        return 'yes'

class Dog(Mamal):
    def __init__(self, race):
        self.race = race



piesel = Dog('kundel')
print(piesel.eat())
print(piesel.lifeborn())
print(piesel.race)

