#2 z możliwością wyboru danych - zadanie domowe

average_fuel_usage = float(input('Give Your vehical average fuel usage: '))
predicted_distance = float(input('Whats Your predicted distance: '))
fuel_price = float(input('How much for fuel: '))

user_cost_of_traveling = predicted_distance / 100 * average_fuel_usage * fuel_price

print('This trip will cost You', round(user_cost_of_traveling, 2), 'coins')
