def rectangle(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("i expect numbers")
        return a * b


def triangle(a, h):
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        print("i expect numbers")
        return 0.5 * a * h


def trapezoid(a, b, h):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(h, (int, float)):
        print("i expect numbers")
        return (((a + b) * h) / 2)


def main():
    side_A = 6
    side_B = 5
    higth_H = 4

    area_r = rectangle(side_A, side_B)
    area_t = triangle(side_A, side_B)
    area_tz = trapeze(side_A, side_B, higth_H)

    print(area_r == 30)
    print(area_t == 15)
    print(area_tz)


if __name__ == '__main__':
    main()
