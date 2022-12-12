from units.archer import Archer
from units.knight import Knight

knights = []
archers = []


for _ in range(4):
    knights.append(Knight())

knights.append(Knight())

for _ in range(6):
    archers.append(Archer())

for Knight in knights:
    Knight.march(2000)
    Knight.attack()



for Archer in archers:
    Archer.attack()

#knights.append(Knight(60))

army = knights + archers

for Knight in army:
    for Archer in army:
        Knight.attack()
        Archer.attack()




def main():
    pass


if __name__ == '__main__':
    main()

