# 2.Stwórz moduł, który przechowuje wzór na deltę. Skorzystaj z wbudowanego modułu math.
# W nowym pliku wykorzystaj moduł.

from delta import delta_cter

from math import sqrt

# def equation_x1(a, b, c):
#     delt = delta_cter(a, b, c)
#     x1 = (- b - sqrt(delt) / 2 * a)
#     return x1
# def equation_x2(a, b, c):
#     delt = delta_cter(a, b, c)
#     x2 = (- b + sqrt(delt) / 2 * a)
#     return x2

def main():
    na = float(input('Give a: '))
    nb = float(input('Give b: '))
    nc = float(input('Give c: '))
    dd = delta_cter(na, nb, nc)
    return dd
    # equation_x1(na, nb, nc)
    # equation_x2(na, nb, nc)
    # print(f'x1 = {x1}')
    # print(f'x2 = {x2}')
    print(dd)

# if __name__ == '__main__':
#     main()

main()

