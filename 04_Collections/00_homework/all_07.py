# 7 Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
krotka_example = tuple(set(example_list))
print(krotka_example)
max_krotka = max(krotka_example)
min_krotka = min(krotka_example)
print(f'Wartość maxymalna: {max_krotka}, wartość minimalna: {min_krotka}')
