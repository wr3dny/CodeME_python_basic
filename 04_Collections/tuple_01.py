# 1 Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę
# na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie
# np. “Mój pies, rasy border collie wabi się Dyzio”.

imaginary_pet = ('Pająk', 'Czarna Wdowa', 'Belzebub')
(pet, pet_more, name ) = imaginary_pet

print(f'Mój wyimaginowany {pet}, dokładniej {pet_more} wabi się {name}')