# Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc. Poproś użytkownika o podanie
# kategorii przed rozpoczęciemy gry. Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
# Rozgrywka powinna być maksymalnie intuicyjna.
import random


def category():
    user_choice = input('Chose category (fruits/sports): ')
    return user_choice


def random_word(filename):
    with open(f'{filename}.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()
        word = random.choice(content)
        return word


# def hangman(letter):
#     if letter in word_to_gues:
def gallows_pole():

    print(' -------\n'
          ' |     |\n'
          ' |     0\n'
          ' |    /|\ \n'
          ' |    / \ \n'
          ' |      \n'
          '/|\ \n')


def hangman():
    print()


def main():
    print('Welcome to Hangman')
    cat_chosen = category()
    word_to_gues = random_word(cat_chosen)
    print(word_to_gues)
    gallows_pole()
    pass
    # secret_word = category()
    # random_word(secret_word)


if __name__ == '__main__':
    main()
