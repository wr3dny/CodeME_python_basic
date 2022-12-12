weight = float(input('Podaj swoją wagę w kg: '))
height = float(input('Podaj swój wzrost w m: '))
bmi = weight / height ** 2

print('Twoje BMI wynosi: ', round(bmi,2))