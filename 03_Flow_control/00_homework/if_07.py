# 7 Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku:
# niedowaga / waga normalna / nadwaga / otyłość.

weight = float(input('Podaj swoją wagę w kg: '))
height = float(input('Podaj swój wzrost w m: '))
bmi = weight / height ** 2

if bmi < 18.5:
    print('Twoje BMI wynosi: ', round(bmi,2), ' - niedowaga' )
elif 18.5 == bmi == 25:
    print('Twoje BMI wynosi: ', round(bmi, 2), ' - normalna waga')
elif 25 < bmi < 30:
    print('Twoje BMI wynosi: ', round(bmi, 2), ' - nadwaga')
else:
    print('Twoje BMI wynosi: ', round(bmi, 2), ' - otyłość')


