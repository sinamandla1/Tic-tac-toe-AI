import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class Ai_player(Player):
  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
      for i in game.available_moves():
        boardcopy = game.board[:]
        boardcopy[i] = self.letter
        
        if game.winner(i, self.letter):
          return i

      player_letter = 'X' if self.letter == 'O' else 'O'
      for i in game.available_moves():
        boardcopy = game.board[:]
        boardcopy[i] = player_letter
            
        if game.winner(i, player_letter):
          return i

      if 4 in game.available_moves():
        return 4

      open_corners = [move for move in game.available_moves() if move in [0, 2, 6, 8]]
      if open_corners:
        return random.choice(open_corners)
      
      open_edges = [move for move in game.available_moves() if move in [1, 3, 5, 7]]
      if open_edges:
        return random.choice(open_edges)
      
      return random.choice(game.available_moves())

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
            square = input(self.letter + "'s turn. Enter a move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid move. Try again!")

        return val
