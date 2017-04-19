class Game:
  def __init__(self):
    self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    self.player1 = "\033[91mX\033[0m" # 1st player's marker
    self.player2 = "\033[92mO\033[0m" # 2nd player's marker
    self.endMsg = ""

  def start_game(self):
    # start by printing the board
    print " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
        (self.board[0], self.board[1], self.board[2],
             self.board[3], self.board[4], self.board[5],
             self.board[6], self.board[7], self.board[8])
    # loop through until the game was won or tied
    while not self.game_is_over(self.board) and not self.tie(self.board):
        print "Enter a number representing the square you want to select:"
        self.get_human_spot()
        if not self.game_is_over(self.board) and not self.tie(self.board):
            self.eval_board()

        print " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
            (self.board[0], self.board[1], self.board[2],
                self.board[3], self.board[4], self.board[5],
                self.board[6], self.board[7], self.board[8])
    print self.endMsg

  def get_human_spot(self):
    spot = None
    while spot is None:
        spot = int(raw_input())
        if (spot <= 8) and (spot >= 0):
            if (self.board[spot] != self.player1) and (self.board[spot] != self.player2):
                self.board[spot] = self.player2
            else:
                print "Square has been selected before, select a valid square"
                spot = None
        else:
            print "The square is not within the grid, select a square within the grid"
            spot = None

  def eval_board(self):
    spot = None
    while spot is None:
      if self.board[4] == "4":
        spot = 4
        self.board[spot] = self.player1
      else:
        spot = self.get_best_move(self.board, self.player1)
        if self.board[spot] != self.player1 and self.board[spot] != self.player2:
          self.board[spot] = self.player1
        else:
          spot = None

  def get_best_move(self, board, next_player, depth = 0, best_score = {}):
    available_spaces = [s for s in board if (s != self.player1) and (s != self.player2)]
    best_move = None

    for avail in available_spaces:
      board[int(avail)] = self.player1
      if self.game_is_over(board):
        best_move = int(avail)
        board[int(avail)] = avail
        return best_move
      else:
        board[int(avail)] = self.player2
        if self.game_is_over(board):
          best_move = int(avail)
          board[int(avail)] = avail
          return best_move
        else:
          board[int(avail)] = avail

    if best_move:
      return best_move
    else:
      return int(available_spaces[0])

  def three_in_a_row(self, *args):
    if args[0] == args[1] == args[2] == self.player1:
        self.endMsg = "X wins"
        return True
    if args[0] == args[1] == args[2] == self.player2:
        self.endMsg  = "O wins"
        return True
    return False

  def game_is_over(self, b):
    return self.three_in_a_row(b[0], b[1], b[2]) or \
        self.three_in_a_row(b[3], b[4], b[5]) or \
        self.three_in_a_row(b[6], b[7], b[8]) or \
        self.three_in_a_row(b[0], b[3], b[6]) or \
        self.three_in_a_row(b[1], b[4], b[7]) or \
        self.three_in_a_row(b[2], b[5], b[8]) or \
        self.three_in_a_row(b[0], b[4], b[8]) or \
        self.three_in_a_row(b[2], b[4], b[6])

  def tie(self, b):
    if len([s for s in b if s == self.player1 or s == self.player2]) == 9:
        self.endMsg  = "It's a tie"
        return True
    else:
        return False

if __name__ == '__main__':
  game = Game()
  game.start_game()
