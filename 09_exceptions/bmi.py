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

def enter_value_h():
    try:
        h = float(input("Podaj wzrost [m]"))
    except TypeError:
        print('Podaj wartość liczbową ( w cyferkach )')
    except ValueError:
        print('Błąd !')
    except UnboundLocalError:
        print('Podaj bez jednostek')
    return h

def enter_value_w():
    try:
        w = float(input("Podaj wzrost [m]"))
    except TypeError:
        print('Podaj wartość liczbową ( w cyferkach )')
    except ValueError:
        print('Błąd !')
    except UnboundLocalError:
        print('Podaj bez jednostek')
    return w




def main():
    w = enter_value_w()
    h = enter_value_h()

    # try:
    #     h = float(input("Podaj wzrost [m]"))
    # except TypeError:
    #     print('Podaj wartość liczbową ( w cyferkach )')
    # except ValueError:
    #     print('Błąd !')
    # except UnboundLocalError:
    #     print('Podaj bez jednostek')
    #
    # try:
    #     w = float(input("Podaj wagę [kg]"))
    # except TypeError:
    #     print('Podaj wartość liczbową ( w cyferkach )')
    # except ValueError:
    #     print('Błąd !')
    # except UnboundLocalError:
    #     print('Podaj bez jednostek')
    result = calc_bmi(h, w)
    print('Twoje BMI:', get_bmi_status(result))


if __name__ == '__main__':
    main()