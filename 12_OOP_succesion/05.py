# Stwórz abstrakcyjną klasę Pojazdy. Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki. Dodaj opisy
# zgodne z tym jak te pojazdy są klasyfikowane.  Jaki rodzaj dokumentu jest potrzebny, by kierować
# poszczegolnym pojazdem.

from abc import ABC, abstractmethod


class Fura(ABC):
    @abstractmethod
    def mobiles(self): # abstract method
        pass

class Bus(Fura):
    def mobiles(self):
        return 'Valid ticket'

class Bike(Fura):
    def mobiles(self):
        return 'Bike card'

class Car(Fura):
    def mobiles(self):
        return 'Driving license for cars'

class Truck(Fura):
    def mobiles(self):
        return 'Driving license for heavy trucks'


b = Bus()
bi = Bike()
c = Car()
t = Truck()
print(t.mobiles())
print(b.mobiles())
print(bi.mobiles())
print(c.mobiles())
