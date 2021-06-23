import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    # word = random.choice(words)
    word = 'record'.upper()
    if '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What letter the user has guessed
    lives = 7

    # getting the user input
    while len(word_letters) > 0 and lives > 0:
        # used letters
        print('You have', lives, 'lives left and you have used these letters', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('Current word: ', ' '.join(word_list))
        print(lives_visual_dict[lives])

        user_letter = input('Guess the letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            lives -= 1

        elif user_letter in used_letters:
            print('The letter you have guessed is already used. Please try again.')
        else:
            print('Invalid character. Please try again.')

    # gets here if len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print(lives_visual_dict[0])
        print('Sorry! You lives are over, the word was', word)
    else:
        print('Yay! You have guessed the word', word, f'correctly! in {lives} guesses')

hangman()