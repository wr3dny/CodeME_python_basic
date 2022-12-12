class Warrior:
    def __init__(self):
        self.xp = 0

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}: hp: {self.hp}, xp: {self.xp}'

    def march(self, distance):
        name = self.__class__.__name__
        print(f'{name}: I have walked {self.distance}m')
        self.xp += 0.02 * distance


