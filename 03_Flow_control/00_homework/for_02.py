# 2 Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

cake = ['flour', 'eggs', 'baking soda', 'sugar', 'mleko']

print('For the cake, to a big bowl in order')
for num, ing in enumerate(cake, 1):
    print(num, ' - add ', ing)
print('\nMix ingredients and bake for 45 minutes.')
