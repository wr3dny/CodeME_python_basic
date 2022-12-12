# 4 Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#
list_input = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

list_input_length = len(list_input)
lpl = list_input_length
lpl1 = int(lpl/3)
lpl2 = int(2*lpl/3)

i = 0

for i in range(1, lpl1):
    part_1_of3 = list_input[:lpl1]
print(part_1_of3)
for i in range(lpl1, lpl2):
    part_2_of3 = list_input[lpl1:lpl2]
print(part_2_of3)
if i in range(lpl1, lpl2):
    part_3_of3 = list_input[lpl2:]
    print(part_3_of3)



