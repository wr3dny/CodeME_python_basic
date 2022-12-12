# Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c)

def min_of_two(val1, val2):
    return val1 if val1 <= val2 else val2


def minimum_of(a, b, c):
    # rozwiazanie nr 1
    # if a >= b and a >= c:
    #     return a
    # elif b >= a and b >= c:
    #     return b
    # else:
    #     return c

    # rozwazanie nr 2
    return min_of_two(c, min_of_two(a, b))



def main():
    result = minimum_of(1, 16, 11)
    print(result)

main()