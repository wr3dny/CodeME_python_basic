# Stwórz własną implementację kolejki lifo. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak:
#  - wyswietlenie kolejki,
#  - sprawdzenie czy jest pusta,
#  - dodanie elementu do kolejki (put),
#  - wyjęcie elementu z kolejki (get).
# Utwórz kilka obiektów klasy Queue z różnymi parametrami.


class Queue: # lifo first in - first out
    def __init__(self, lifo=[]):
        self.lifo = lifo

    def show(self):
        print('Queue -->', self.lifo)

    def is_empty(self):
        return len(self.lifo) == 0

    def put(self, item):
        self.lifo.append(item)

    def get(self):
        return self.lifo.pop(-1)

def main():
    q = Queue([3, 2, 7, 9, 'txt'])
    q.show()
    print(q.is_empty())
    q.put('rita')
    q.put('asmodeusz')
    q.show()
    x = q.get()
    print('wyjęto -->', x)
    q.show()

if __name__ == '__main__':
    main()