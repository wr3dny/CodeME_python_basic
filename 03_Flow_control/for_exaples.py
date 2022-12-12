txt = 'abrakadabra'

for letter in txt:
    print('- ', letter)

names = ['Ada', 'Julia', 'Ruby', 'Perl']

for i in names:
    print('Hello', i)

for step in range(3):
    print(step)

for number in range(5, 20, 2):
    print('->', number)

for index, elem in enumerate(txt):
    print(index, elem)

counter = len(txt)
for index in range(0, counter, 2):
    print(index, txt[index])

pa = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)
