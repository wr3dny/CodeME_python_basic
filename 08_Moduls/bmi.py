def calc_bmi(height, weight):
    return round(weight / height ** 2, 2)


def get_bmi_status(bmi):
    if bmi < 18.5:
        return "skinny"
    elif bmi < 25:
        return "norma"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otylosc"


def main():
    w = float(input("Podaj wagę [kg]"))
    h = float(input("Podaj wzrost [m]"))

    result = calc_bmi(h, w)
    print('Twoje BMI:', get_bmi_status(result))

if __name__ == '__main__':
    main()