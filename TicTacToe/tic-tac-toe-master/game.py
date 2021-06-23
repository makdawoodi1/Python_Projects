'''
1. Prints the board with numbers and lets you decide which to choose
2. You select what to choose
3. Then the Letter gets switched and the Computer Selects what to choose
4. The Game Checks for three consecutive spots if it is True it prints letter wins else ties
'''
import math
import random
from player import RandomComputerPlayer, HumanPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for i in range(9)]

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        
        # return moves

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # rows
        row_ind = math.floor(square // 3)
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True

        # columns
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        # diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        # means it is a tie!
        return False

def play(game, x_player, o_player, print_game = True):
    # returns letter 
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
                print('-------------')
                game.print_board_nums()
                print('-------------')
                print('')
                print('-------------')
                game.print_board()
                print('-------------')

            if game.current_winner:
                print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
    
        # tiny pause
        time.sleep(0.8)
    
    print('It\'s a tie')

if __name__ == "__main__":
    while True:
        while True:    
            random_choice = random.choice(['1', '2'])
            choice = input('''How do you want to play the game as?? 
            1. Human VS Human
            2. RandomComputerPlayer VS RandomComputerPlayer
            3. Human VS RandomComputerPlayer: ''')
            if choice == '1':    
                x_player = HumanPlayer('X')
                o_player = HumanPlayer('O')
                break
            if choice == '2':  
                x_player = RandomComputerPlayer('X')
                o_player = RandomComputerPlayer('O')
                break
            if choice == '3':
                if random_choice == '1':
                    x_player = HumanPlayer('X')
                    o_player = RandomComputerPlayer('O')
                    break
                else:
                    x_player = RandomComputerPlayer('X')
                    o_player = HumanPlayer('O')
                    break
            
        t = TicTacToe()
        play(t, x_player, o_player, print_game = True)

        try_again = input('Do you want to play the game again?? (Y) for yes & (N) for no: ').upper()
        if try_again == 'Y':
            continue
        else: 
            print('Thank you for playing the game!')
            exit()

# from player import RandomComputerPlayer, HumanPlayer
# import time

# class TicTacToe:
#     def __init__(self):
#         self.board = self.make_board()
#         self.current_winner = None

#     @staticmethod
#     def make_board():
#         return [' ' for i in range(9)]

#     def print_board(self):
#         for row in [self.board[i * 3 : (i + 1 ) * 3] for i in range(3)]:
#             print('| ' + ' | '.join(row) + ' |')

#     @staticmethod
#     def print_board_nums():
#         # 0 | 1 | 2 etc
#         number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
#         for row in number_board:
#             print('| ' + ' | '.join(row) + ' |')

#     def available_moves(self):
#         return [i for i, spot in enumerate(self.board) if spot == ' ']
#         # moves = []
#         # for (i, spot) in enumerate(self.board):
#         #     if spot == ' ':
#         #         moves.append(i)
#         # return moves

#     def empty_squares(self):
#         return ' ' in self.board

#     def num_empty_squares(self):
#         return self.board.count(' ')

#     def make_move(self, square, letter):
#         if self.board[square] == ' ':
#             self.board[square] = letter
#             if self.winner(square, letter):
#                 self.current_winner = letter
#             return True
#         return False

#     def winner(self, square, letter):
#         # winner if there is 3 in a row. We have to check all the possibility
#         # For row
#         row_ind = square // 3
#         row = self.board[row_ind * 3 : (row_ind + 1) * 3]
#         if all(spot == letter for spot in row):
#             return True

#         # For Column
#         col_ind = square % 3
#         column = [self.board[col_ind + i * 3] for i in range(3)]
#         if all(spot == letter for spot in column):
#             return True

#         # For Diagonals
#         if square % 2 == 0:
#             diagonal1 = [self.board[i] for i in [0, 4, 8]]
#             if all(spot == letter for spot in diagonal1):
#                 return True
#             diagonal2 = [self.board[i] for i in [2, 4, 6]]
#             if all(spot == letter for spot in diagonal2):
#                 return True
            
#         # if all of these fail
#         return False

# def play(game, x_player, o_player, print_game = True):
#     # returns the winner of the game(letter) or None for a tie!
#     if print_game:
#         print('-------------')
#         game.print_board_nums()
#         print('-------------')

#     letter = 'X'
#     # iterate while the game still has empty squares

#     while game.empty_squares():
#         if letter == 'O':
#             square = o_player.get_move(game)
#         else: square = x_player.get_move(game)

#         # let's define a function to make a move
#         if game.make_move(square, letter):
#             if print_game:
#                 print(letter + f' makes a move to square {square}\n')
#                 print('-------------')
#                 game.print_board_nums()
#                 print('-------------\n')
#                 print('-------------')
#                 game.print_board()
#                 print('-------------')
#                 print('')

#             if game.current_winner:
#                 if print_game:
#                     print(letter + ' wins!')

#                 return letter

#             # after we make our move we need to alternate letters
#             letter = 'O' if letter == 'X' else 'X'

#         # tiny pause
#         time.sleep(0.8)

#     if print_game:
#         print('It\'s a tie!')

# if __name__ == "__main__":
#     x_player = HumanPlayer('X')
#     o_player = RandomComputerPlayer('O')
#     t = TicTacToe()
#     play(t, x_player, o_player, print_game = True)