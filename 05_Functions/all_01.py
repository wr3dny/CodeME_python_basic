#Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz
# zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def calc_bmi(height, weight):
    return round(weight / height ** 2, 2)


def get_bmi_status(bmi):
    if bmi < 18.5:
        return "niedowaga"
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


main()