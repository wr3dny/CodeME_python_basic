from warrior import Warrior


class Knight(Warrior):
    def __init__(self):
        super().__init__()


    def attack(self):
        print(f'Knight: I have swing my sword')
        self.xp += 0.3

    def march(self, distance):
        print(f'Knight: I have walked {distance}m ')
        self.xp += 0.3
