class board:
    def __init__(self):
        self.position = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    def move(self, player, spot):
        """ Records move of a player to board
        """

        self.position[int(spot)] = player.marker
