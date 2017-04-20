""" Tests the player class
"""
import unittest
from context import game

class easyEvalTest(unittest.TestCase):
    """ Tests eval_board() method for player in easy mode
    """

    # Does not select central square if it's free
    def testCenter(self):
        # to be implemented

    # Does not select a winning move it has a diferent move
    def testWinning(self):
        # to be implemented

    # Does not block oponents winning move if has a diferent move
    def testBlock(self):
        # to be implemented

    # Selects the only move
    def testOnly(self):
        # to be implemented

class mediumEvalTest(unittest.TestCase):
    """ Tests eval_board() method for player in medium difficulty
    """
    # Selects the central square if it's free
    def testCenter(self):
        # to be implemented

    # Selects the winning square
    def testWinning(self):
        # to be implemented

    # Allows for a winning move when oponent has central and oposite squares selected
    def testBlock(self):
        # to be implemented

    # Selects the only square
    def testOnly(self):
        # to be implemented

class hardEvalTest(unittest.TestCase):
    """ Tests eval_board() method for player in hard difficulty
    """
    # Selects the central square if it's free
    def testCenter(self):
        # to be implemented

    # Selects the winning square
    def testWinning(self):
        # to be implemented

    # Blocks the oponent when central and oposite squares are selected
    def testBlock(self):
        # to be implemented

    # Selects the only square
    def testOnly(self):
        # to be implemented
