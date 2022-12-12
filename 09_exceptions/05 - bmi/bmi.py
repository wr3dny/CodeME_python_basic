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
        return "otyłość"

def advice(bmi_result):

    if bmi_result == 'niedowaga':
        filename = 'skinny'
    elif bmi_result == 'norma':
        filename = 'ok'
    elif bmi_result == 'nadwaga':
        filename = 'little_to_fat'
    elif bmi_result == 'otyłość':
        filename = 'fatty'
    with open(f'{filename}.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()
        return content



def main():
    w = float(input("Podaj wagę [kg]"))
    h = float(input("Podaj wzrost [m]"))
    result = calc_bmi(h, w)
    advice(result)
    print('Twoje BMI:', get_bmi_status(result), advice(result))
    print()


# def calc_bmi(height, weight):
#     return round(weight / height ** 2, 2)
#
#
# def get_bmi_status(bmi):
#     if bmi < 18.5:
#         return "underweight"
#     elif bmi < 25:
#         return "standard"
#     elif bmi < 30:
#         return "overweight"
#     else:
#         return "obesity"

if __name__ == '__main__':
    main()