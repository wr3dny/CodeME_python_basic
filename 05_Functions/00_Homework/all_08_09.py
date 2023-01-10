# 8. Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#    Program zacznie ze stworzonym słownikiem o trzech kluczach:
#    marka (str)
#    model (str)
#    rocznik (int)
#    Wypisze ten słownik na ekran (bez żadnego formatowania)
#    Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
#    “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#     Jeśli nie spełnia powyższego warunku, wypisze komunikat:
#    “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#     Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć,
#     czy progam również zmienia swoje zachowanie.
# 9▹ Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
#  W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#     Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
#     dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#     ponownie wyświetl zmieniony słownik
#     Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego
#     oryginalności. Dopisz odpowiednie komunikaty.

def user_car(brand, model, year, parts):
    car_dict = {
        'brand': brand,
        'model': model,
        'year': year,
        'parts': original_parts(parts)
    }
    return car_dict


def car_age(year, brand):
    import datetime
    now = datetime.datetime.now().year
    age = now - year
    return age


def original_parts(parts):
    if parts == 'Yes':
        return True
    else:
        return False


def main():
    b = input('What\'s Your car brand: ')
    b = (b.lower()).capitalize()
    m = input('What\'s Your car model: ')
    m = (m.lower()).capitalize()
    y = int(input('What\'s Your car year: '))
    p = input('Running on 75% of original parts (yes/no): ')
    p = (p.lower()).capitalize()
    result = user_car(b, m, y, p)
    age = car_age(y, b)
    result3 = original_parts(p)
    if age >= 25 and p == 'Yes':
        print(f'Gratulacje! Twój samochód {b} może być zarejestrowany jako zabytek')
    elif age < 25:
        print(f'Twój samochód {b}jest jeszcze zbyt młody.')
    elif p == 'No':
        print(f'Twój samochód {b}ma poniżej 75% oryginalnych części.')
    elif p == 'No' and age < 25:
        print(f'Twój samochód {b}nie spełnia obu warunków zabytkowego pojazdu')

    print()
    for k, v in result.items():
        print(k, ' :', v)

main()

