'''
1. Ask the user how he wants to play the game
    1. Human Player against Smart Computer (Take random choice (X or O) and pass it to Human Player otherwise to SmartComputer Player)
    2. Human Player against Human Player (Take random choice (X or O) and pass it to Human Player otherwise to Human Player)
    3. Random Computer Player against Random Computer Player (Take random choice (X or O) and pass it to RandomComputer Player otherwise to RandomComputer Player)
    4. Smart Computer Player Against Smart Computer Player (Take random choice (X or O) and pass it to SmartComputer Player otherwise to SmartComputer Player)
    5. Human Player Against Random Computer Player (Take random choice (X or O) and pass it to Human Player otherwise to Random Computer Player)
2. 
'''

import math
import random
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range( j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]


def play(game, x_player, o_player, print_game = True):

    if print_game:
        print('-------------')
        game.print_board_nums()
        print('-------------')

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                print('\nChoose from selected positions!\n')
                print('-------------')
                game.print_board_nums()
                print('-------------')
                print('')
                print('-------------')
                game.print_board()
                print('-------------')
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    while True:
        while True:
            user_choice = input('''\nHow do you want to play the game as?
            1. Human Player against Smart Computer
            2. Human Player against Human Player
            3. Random Computer Player against Random Computer Player
            4. Smart Computer Player Against Smart Computer Player
            5. Human Player Against Random Computer Player?? ''')
            random_choice = random.choice(['X', 'O'])
            if user_choice == '1':
                if random_choice == 'X':
                    x_player = HumanPlayer(random_choice)
                    o_player = SmartComputerPlayer('O')
                x_player = HumanPlayer(random_choice)
                o_player = SmartComputerPlayer('X')
                break
            elif user_choice == '2':
                if random_choice == 'X':
                    x_player = HumanPlayer(random_choice)
                    o_player = HumanPlayer('O')
                x_player = HumanPlayer(random_choice)
                o_player = HumanPlayer('X')
                break
            elif user_choice == '3':
                if random_choice == 'X':
                    x_player = RandomComputerPlayer(random_choice)
                    o_player = RandomComputerPlayer('O')
                x_player = RandomComputerPlayer(random_choice)
                o_player = RandomComputerPlayer('X')
                break
            elif user_choice == '4':
                if random_choice == 'X':
                    x_player = SmartComputerPlayer(random_choice)
                    o_player = SmartComputerPlayer('O')
                x_player = SmartComputerPlayer(random_choice)
                o_player = SmartComputerPlayer('X')
                break
            elif user_choice == '5':
                if random_choice == 'X':
                    x_player = HumanPlayer(random_choice)
                    o_player = RandomComputerPlayer('O')
                x_player = HumanPlayer(random_choice)
                o_player = RandomComputerPlayer('X')
                break
            else: print('\nInvalid Character. Try again!')

        t = TicTacToe()
        play(t, x_player, o_player, print_game = True)
        try_again = input('Do you want to play again?? (Y) for yes and (N) for no: ').upper()
        if try_again == 'Y':
            continue
        else: break