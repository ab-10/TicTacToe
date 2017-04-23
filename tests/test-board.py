""" Test the board class
"""

import unittest
from context import board
from context import player

class boardTest(unittest.testBoard):
    def setUp(self):
        testBoard = board.board()
        testPlayer = player.player("O", False)

    def testMove(self):
        testBoard.move(testPlayer, 4)
        self.assertTrue(testBoard.position == ["0", "1", "2", "3", "O", "5", "6", "7", "8"])
        testBoard.move(testPlayer, 0)
        self.assertTrue(testBoard.position == ["O", "1", "2", "3", "O", "5", "6", "7", "8"])
