# 1
pi = 3.14
def calculate_circle_field(r):
    return pi * r**2

radius = float(input('Podaj promień: '))

field = calculate_circle_field(radius)
print(field)
