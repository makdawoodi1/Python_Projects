import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turn. Input values (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except:
                print('Invalid character. Please try again.')

        return val

# import math
# import random

# class Player:
#     def __init__(self, letter):
#         self.letter = letter

#     def get_move(self, game):
#         pass

# class RandomComputerPlayer(Player):
#     def __init__(self, letter):
#         super().__init__(letter)

#     def get_move(self, game):
#         # get a random valid spot for our RandomComputerPlayer
#         square = random.choice(game.available_moves())
#         return square

# class HumanPlayer(Player):
#     def __init__(self, letter):
#         super().__init__(letter)

#     def get_move(self, game):
#         valid_square = False
#         val = None

#         if not valid_square:
#             square = input(self.letter + '\'s turn. Input moves (0-8): ')
#             try:
#                 val = int(square)
#                 if val not in game.available_moves():
#                     raise ValueError
#                 valid_square = True
#             except:
#                 print('Invalid character. Please try again.')

#         return val