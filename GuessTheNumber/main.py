import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    number_of_guesses = 0

    while guess != random_number:
        number_of_guesses += 1
        guess = int(input(f'\nPlease enter a number to guess between 1 and {x}: '))

        if guess < random_number:
            if random_number - guess >= 50:
                print('Sorry! You are too low.. Please try again :)')
            elif random_number - guess >= 30 and guess - random_number < 50:
                print('Sorry! You are low.. Please try again :)')
            elif random_number - guess >= 1 and guess - random_number < 30:
                print('Sorry! You are low but close enough.. Please try again :)')
        
        elif guess > random_number:
            if guess - random_number >= 50:
                print('Sorry! You are too high.. Please try again :)')
            elif guess - random_number >= 30 and guess - random_number < 50:
                print('Sorry! You are high.. Please try again :)')
            elif guess - random_number >= 1 and guess - random_number < 30:
                print('Sorry! You are high but close enough.. Please try again :)')

    print(f'\nYay! Congrats. You have guessed the number {(random_number)} in {number_of_guesses} guesses\n')

    while True:
        try_again = input('\nDo you want to play again! (Y) for yes, (N) for no?? ').lower()

        if try_again == 'y':
            while True:
                choice = int(input('\nWhich game do you want to play? \
1 for (You guess the number) \
2 for (Computer guess the number)?? '))
                if choice == 1: guess(100)
                else: computer_guess(100)
        else: exit()

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    number_of_guesses = 0

    while feedback != 'C':
        number_of_guesses += 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'\nIs {guess} too high (H), too low (L), or correct (C)?? ').upper()

        if feedback == 'H':
            high = guess - 1

        elif feedback == 'L':
            low = guess + 1
        
    print(f'\nYay! The Computer Guessed your number, {guess}, correctly! in {number_of_guesses} guesses\n')

    while True:
        try_again = input('\nDo you want to play again! (Y) for yes, (N) for no?? ').lower()

        if try_again == 'y':
            while True:
                choice = int(input('\nWhich game do you want to play? \
1 for (You guess the number) \
2 for (Computer guess the number)?? '))
                if choice == 1: guess(100)
                else: computer_guess(100)
        else: exit()

while True:
    choice = int(input('\nWhich game do you want to play? \
1 for (You guess the number) \
2 for (Computer guess the number)?? '))        

    if choice == 1: guess(100)
    else: computer_guess(100)