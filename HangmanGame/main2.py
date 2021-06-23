import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    if '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what letter the user has guessed

    lives = 7

    # getting the user input
    while len(word_letters) > 0 and lives > 0:
        # used letters
        print('You have ', lives, 'left and you have used these letters:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('Current word:', ' '.join(word_list))
        print(lives_visual_dict[lives])

        user_letter = input('Guess the letter: ')

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives -= 1

        elif user_letter in used_letters:
            print('Ohh! you have already used this letter. Please try again.')

        else:
            print('Invalid letter. Please try again.')

    # gets here when len(word_list) == 0 OR when lives == 0
    if lives == 0:
        print('Sorry! you have lost all the lives, the word was', word)
    else:
        print(f'Yay! You have guessed the word correctly! in {lives} guesses and the word was: {word}')

hangman()