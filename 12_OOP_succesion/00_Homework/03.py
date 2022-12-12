# 3 Zadanie inspirowane popkulturą: https://www.youtube.com/watch?v=Ct6BUPvE2sM
#
# Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple. Logiki to nie ma, więc dodaj wg uznania.

class Pen:
    def ppen(self):
        return 'Pen'


class Pinapple:
    def ppianpple(selfs):
        return 'Pinapple'

class PenPinapple:
    def __init__(self, onepart, secondpart):
        print(str(onepart) + str(secondpart))


answer = PenPinapple(Pinapple, Pen)

print(answer)


