import random

def play():
    user = input("(r) for rock, (p) for paper, and (s) for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer: return '\nIt\'s a tie!\n'

    if is_win(user, computer): return f'\nYou Won! The Player chose {user} and The Computer chose {computer}.\n'

    return f'\nYou Lost! The Player chose {user} and The Computer chose {computer}\n'

def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'): return True

print(play())

while True:
    choice = input('\nDo you want to play the game again? (Y) for yes and (N) for no?? ').lower()

    if choice == 'y': print(play())
    else: exit()