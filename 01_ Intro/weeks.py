#1. minuty w tygodniu

minuts_in_hour = 60
hours_in_day = 24
days_in_week = 7
number_of_weeks = 7

minutes_in_7_weeks = minuts_in_hour * hours_in_day * days_in_week * number_of_weeks
print('Siedem tygodni to:', minutes_in_7_weeks, 'minut')

#2. czas na naukę

needed_time = 75

your_need = int(input('Podaj ile godzin możesz tygodniowo poświęcić na naukę: '))

number_of_needed_weeks = round(needed_time/your_need)
print(number_of_needed_weeks,'tygodni')

