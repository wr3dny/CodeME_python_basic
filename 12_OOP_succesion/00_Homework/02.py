# 2  Do klasy człowiek dodaj metodę super() tak, aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.


class Animal:
    def eat(self):
        return 'need to eat'

class Mamal(Animal):
    def lifeborn(self):
        return 'yes'

class Dog(Mamal):
    def __init__(self, race):
        self.race = race
        super()



piesel = Dog('kundel')
print(piesel.eat())
print(piesel.lifeborn())
print(piesel.race)


