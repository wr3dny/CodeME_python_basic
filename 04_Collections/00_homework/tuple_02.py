# Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

tup_1 = ('owoce', 'warzywa ', 'mięso', 'owoce', 'ryby', 'ryby')

print('-----')
set_01 = set([word for word in tup_1 if tup_1.count(word) > 1])
print(set_01)
