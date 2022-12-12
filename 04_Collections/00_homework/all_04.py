# 4 Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia
# wiersz × kolumna.

multiplication_table = []

for i in range(1, 11):
    inner_list = []
    for j in range(1, 11):
        inner_list.append(i * j)
    multiplication_table.append(inner_list)

print(*multiplication_table, sep = "\n")




