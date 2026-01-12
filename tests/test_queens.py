# test_queens.py
#
# ICS 33 Winter 2026
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_queen_count_is_zero_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

from queens import QueensState
import unittest



class TestQueensState(unittest.TestCase):
    def setUp(self):
        self.state = QueensState(8,8)
    def test_queen_count_is_zero_initially(self):
        self.assertEqual(self.state.queen_count(), 0)

    def test_queen_board_initialization(self):
        board = self.state.get_board()
        self.assertIsNotNone(board)
        self.assertEqual(len(board), 8)
        self.assertEqual(len(board[0]), 8)

    def test_queens_positions(self):
        pass

if __name__ == '__main__':
    unittest.main()
