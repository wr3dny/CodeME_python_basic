# 4 Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

natural_number = int(input('Please, give me Your number: '))

sil = 1
if natural_number <= 8:
    for num in range(1, natural_number + 1):
        sil *= num
        print(sil)

else:
    print('Number is to high')

