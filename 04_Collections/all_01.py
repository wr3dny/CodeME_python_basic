# 1 Utwórz listę lists_to_dict zawierającą listy 2 elementowe. Przekształć ją w słownik dict_from_list.
list_to_dict = [['leg', 'beine'], ['head', 'kopf'], ['eye', 'auge']]

dict_from_list = dict(list_to_dict)

print(type(dict_from_list))
print(dict_from_list)