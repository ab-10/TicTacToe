class player:
    def __init__(marker, isComputer, difficulty=None):
        self.marker = marker
        self.isComputer = isComputer
        self.difficulty = difficulty

    """ Evaluetes move and returns the square that should be selected based
    on the difficulty of player.
    If the player is not computer raises attribute error
    """
    def eval_board(board):
        if isComputer:
            if difficulty == "easy":
                # to be implemented

            elif difficulty == "medium":
                # to be implemented

            elif difficulty == "hard":
                # to be implemented

        else:
            raise AttributeError("eval_board is not defined for non computer player")
