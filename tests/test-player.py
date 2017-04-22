""" Tests the player class
"""

import unittest
from context import player
from context import board

class easyEvalTest(unittest.TestCase):
    """ Tests eval_board() method for player in easy mode
    """

    def setUp(self):
        testPlayer = player.player("X", True, "easy")
        testBoard = board.board()

    # Does not select central square if it has a diferent move
    def testCenter(self):
        testBoard.position = ["0", "O", "2", "X", "4", "5", "6", "7", "8"]
        self.assertFalse(testPlayer.eval_board(testBoard) == "4")

    # Does not select a winning move if it has a diferent move
    def testWinning(self):
        testBoard.position = ["X", "O", "O", "X", "4", "5", "6", "7", "8"]
        self.assertFalse(testPlayer.eval_board(testBoard) == "6")

    # Does not block oponents winning move if it has a diferent move
    def testBlock(self):
        testBoard.position = ["O", "X", "X", "O", "4", "5", "6", "7", "8"]
        self.assertFalse(testPlayer.eval_board(testBoard) == "6")

    # Selects the only move
    def testOnly(self):
        testBoard.position = ["X", "O", "X", "X", "4", "O", "O", "X", "O"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "4")


class mediumEvalTest(unittest.TestCase):
    """ Tests eval_board() method for player in medium difficulty
    """

    def setUp(self):
        testPlayer = player.player("X", False, "medium")
        testBoard = board.board()

    # Selects the central square if it's free
    def testCenter(self):
        testBoard.position = ["0", "O", "2", "X", "4", "5", "6", "7", "8"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "4")

    # Selects the winning square
    def testWinning(self):
        testBoard.position = ["X", "O", "O", "X", "4", "5", "6", "7", "8"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "6")

    # Allows for a winning move when oponent has central and oposite squares selected
    def testHardBlock(self):
        testBoard.position = ["0", "1", "O", "3", "O", "5", "X", "7", "8"]
        self.assertTrue((testPlayer.eval_board(testBoard) == "6") or (testPlayer.eval_board(testBoard) == "8"))

    # Blocks simple winning move
    def testEasyBlock(self):
        testBoard.position = ["O", "X", "X", "O", "4", "5", "6", "7", "8"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "6")

    # Selects the only move
    def testOnly(self):
        testBoard.position = ["X", "O", "X", "X", "4", "O", "O", "X", "O"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "4")

class hardEvalTest(unittest.TestCase):
    """ Tests eval_board() method for player in hard difficulty
    """

    def setUp(self):
        testPlayer = player.player("X", False, "hard")
        testBoard = board.board()

    # Selects the central square if it's free
    def testCenter(self):
        testBoard.position = ["0", "O", "2", "X", "4", "5", "6", "7", "8"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "4")

    # Selects the winning square
    def testWinning(self):
        testBoard.position = ["X", "O", "O", "X", "4", "5", "6", "7", "8"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "6")

    # Blocks a winning move when oponent has central and oposite squares selected
    def testHardBlock(self):
        testBoard.position = ["0", "1", "O", "3", "O", "5", "X", "7", "8"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "0")

    # Blocks simple winning move
    def testEasyBlock(self):
        testBoard.position = ["O", "X", "X", "O", "4", "5", "6", "7", "8"]
        self.assertTrue((testPlayer.eval_board(testBoard) == "6") or (testPlayer.eval_board(testBoard) == "8"))

    # Selects the only move
    def testOnly(self):
        testBoard.position = ["X", "O", "X", "X", "4", "O", "O", "X", "O"]
        self.assertTrue(testPlayer.eval_board(testBoard) == "4")
