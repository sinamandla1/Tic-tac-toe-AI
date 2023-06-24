import math
import random


class Player:
    def __init__(self,letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomCpuPlayer(Player):
    def __int__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.availablemoves())
        return square

class HumanPlayer(Player):
    def __int__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        
        while not valid_square:
            square = input(self.letter + '\'s turn Input move (0 - 9): ')
            try:
                val = int(square)
                if val not in game.availablemoves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, try again!")
                return val
