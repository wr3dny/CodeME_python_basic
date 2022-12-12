class bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calc_bmi(self):
        return round(self.weight/ self.height ** 2, 2)


#
# def get_bmi_status(bmi):
#     if bmi < 18.5:
#         return "skinny"
#     elif bmi < 25:
#         return "norma"
#     elif bmi < 30:
#         return "nadwaga"
#     else:
#         return "otylosc"


def main():

    pacjent = bmi(85, 1.85)


    print('Twoje BMI:', pacjent.calc_bmi())

if __name__ == '__main__':
    main()