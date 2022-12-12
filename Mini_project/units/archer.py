from warrior import Warrior


class Archer(Warrior):
    def __init__(self):
        super().__init__()
        self.quiver = 24

    def attack(self):
        print(f'Archer: I have shot an arrow')
        self.xp += 0.4
        self.quiver -= 1
        if self.quiver <= 0:
            print('Archer: Out of arrows, cant shot')