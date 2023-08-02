class Ai_player(Player):
      def __init__(self, letter):
              super().__init__(letter)
                
                  def get_move(self, game):
                          possible_moves = [x for x, letter in enumerate(game.board) if letter == ' ']
                              moves = 0

                                  for val in ['X', 'O']:
                                            for i in possible_moves:
                                                        boardcopy = game.board[:]
                                                                boardcopy[i] = val
                                                                        
                                                                                if game.winner(boardcopy, val):
                                                                                              moves = i
                                                                                                  return moves
                                                                                                  
                                                                                                  open_corners = []
                                                                                                      for i in possible_moves:
                                                                                                                if i in [0, 2, 6, 8]:
                                                                                                                            open_corners.append(i)
                                                                                                                                  
                                                                                                                                        if len(open_corners) > 0:
                                                                                                                                                    move = random.choice(open_corners)
                                                                                                                                                            return move
                                                                                                                                                              
                                                                                                                                                              if 4 in possible_moves:
                                                                                                                                                                          move = 4
                                                                                                                                                                                  return move
                                                                                                                                                                                    
                                                                                                                                                                                    open_edges = []
                                                                                                                                                                                          for i in possible_moves:
                                                                                                                                                                                                      if i in [1, 3, 5, 7]:
                                                                                                                                                                                                                    open_edges.append(i)
                                                                                                                                                                                                                            
                                                                                                                                                                                                                                    if len(open_edges) > 0:
                                                                                                                                                                                                                                                  move = random.choice(open_edges)
                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                return move
                                                                                                                                                                                                                                                                return random.choice(possible_moves)
