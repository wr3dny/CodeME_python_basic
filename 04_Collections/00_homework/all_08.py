# Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

norway_names = ['Ingrid', 'Sofia', 'Leah', 'Sofie', 'Emilie', 'Olivia', 'Maja', 'Ella', 'Emma', 'Nora']
belgium_names = ['Olivia', 'Emma', 'Mila', 'Louise', 'Lina', 'Alice', 'Sofia', 'Mia', 'Anna', 'Juliette']
uk_names = ['Olivia', 'Amelia', 'Isla', 'Ava', 'Mia', 'Ivy', 'Lily', 'Isabella', 'Sophia', 'Rosie']
estonia_names = ['Mia', 'Sofia', 'Emily', 'Hanna', 'Nora', 'Emma', 'Eva', 'Alisa', 'Marta', 'Lenna']
finland_names = ['Aino', 'Olivia', 'Sofia', 'Pihla', 'Aada', 'Eevi', 'Isla', 'Lilja', 'Helmi', 'Ella']
italy_names = ['Sofia', 'Giulia', 'Aurora', 'Ginevra', 'Alice', 'Beatrice', 'Emma', 'Giorgia', 'Vittoria', 'Matilde']
moldova_names = ['Sofia', 'Amelia', 'Anastasia', 'Maria', 'Daria', 'Victoria', 'Eva', 'Alexandra', 'Evelina', 'Andreea']
netherlands_names = ['Julia', 'Mila', 'Emma', 'Nora', 'Olivia', 'Sophie', 'Tess', 'Milou', 'Zoë', 'Yara']
romania_names = ['Sofia', 'Amelia', 'Anastasia', 'Maria', 'Victoria', 'Daria', 'Eva', 'Alexandra', 'Evelina', 'Andreea']
switzerland_names = ['Mia', 'Emma', 'Mila', 'Emilia', 'Lina', 'Sofia', 'Elena', 'Lea', 'Alina', 'Laura']


ten_top_names = norway_names + belgium_names + uk_names + estonia_names + finland_names + italy_names + moldova_names + \
                netherlands_names + romania_names + switzerland_names

ten_top_names_dict = {name : ten_top_names.count(name) for name in ten_top_names}
print(ten_top_names_dict)

at_least_in_3 = []

for i in norway_names:
    if i in belgium_names:
        at_least_in_3.append(i)
    elif i in uk_names:
        at_least_in_3.append(i)


print(at_least_in_3)




# top_names = []
#
# top_ten_names = list(top_ten_names)
#
# for name in top_ten_names:
#     top_names.append(top_ten_names(name))


# def names_repeat(list):
#     count = 0
#     for name in list

# print(top_ten_names)
#
# # another_form = {}
# #
# # for i in top_ten_names:
# #     another_form[i] = top_ten_names(i)
# #
# # print(another_form)
#
# repeating_names = []
# index = 0
#
# for name in top_ten_names:
#     if name in repeating_names:
#         index += 1
#     else:
#         repeating_names.append(name)
#
#
# print(len(repeating_names))



# for names in top_ten_names:
#     if names in top_ten_names[:-1]:
#         print(names, end = ' \n ')
#     else:
#         print(names)

# for names in norway_names:
#     top_ten_names.extend(names)

# print(top_ten_names)


#
# norway_names_eleven = norway_names.append('Jaja')
#
# print(norway_names)

# print(tuple(*norway_names))
#
# ?new_names_list = [tuple(*norway_names), tuple(*belgium_names), tuple(*uk_names)]
#
# bylo = set()
# uniq = []
#
# print(new_names_list)
#
# for name in new_names_list:
#     if name not in bylo:
#         uniq.append()
#         bylo.add()

# for names in top_ten_names:
#     if names in top_ten_names[:-1]:
#         print(names, end = ' | \n')
#     else:
#         print(names)
# print()
#
# print(list(enumerate(top_ten_names)))

# print(new_names_list)
# jakas_lista = []
# name_counter = {}

#
# top_another_names = set(norway_names) & set(italy_names)
# print(top_another_names)
#
# for names in switzerland_names:
#     jakas_lista.append(names)
#     if names not in jakas_lista:
#         name_counter += 1
#     else:
#         name_counter = 1
#
# print(jakas_lista)
# print(name_counter)

# print(top_ten_names)
# print(finland_names)



# for names in romania_names:
#     if names


#
# print()

# for names in moldova_names:
#     if names in moldova_names[:-1]:
#         print(names, end = ' | ')
#     else:
#         print(names)
# print()

# minimum_3_times = []
#
# for name in finland_names:
#     for index, value in enumerate(finland_names):
#         print(*value, end=" | ")
#     else:
#         print( end=" ")
#     print()
#
# norway_names = set(norway_names)
# print(norway_names)



#
# top_ten_names.split()
#
# print(top_ten_names)
# ttn = list(set(top_ten_names))
#
#
# names_counter = {}

# for name in top_ten_names:
#     if name in names_counter:
#         names_counter[word] += 1
#     else:
#         names_counter[word] = 1
#
# for k, v in words_counter.items():
#     print(f'- {k} : {v}')
#
# print(top_ten_names)
#print(names_counter)


