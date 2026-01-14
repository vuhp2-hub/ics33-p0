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

from queens import QueensState, Position
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
        # Changing board directly is not intended
        # But for ease of testing
        self.state._board[0][0] = 1
        queensPositions = self.state.queens()
        self.assertIsNotNone(queensPositions[0])
        self.assertEqual(queensPositions[0].row, 0)
        self.assertEqual(queensPositions[0].column, 0)

    def test_has_queen(self):
        self.state._board[0][0] = 1
        test_position_exists = Position(row=0, column=0)
        test_position_empty = Position(row=0, column=1)
        self.assertEqual(self.state.has_queen(test_position_exists), True)
        self.assertEqual(self.state.has_queen(test_position_empty), False)

    def test_any_queens_unsafe(self):
        # Safe
        self.state._board[0][0] = 1
        self.state._board[1][2] = 1
        self.state._board[2][4] = 1
        self.assertEqual(self.state.any_queens_unsafe(), False)

        # Row
        self.state._board[0][1] = 1
        self.assertEqual(self.state.any_queens_unsafe(), True)

        # Column
        self.state._board[0][1] = 0
        self.state._board[1][0] = 1
        self.assertEqual(self.state.any_queens_unsafe(), True)

        # Diagonal
        self.state = QueensState(8, 8)
        self.state._board[0][0] = 1
        self.state._board[7][7] = 1
        self.assertEqual(self.state.any_queens_unsafe(), True)

        # Anti-Diagonal
        self.state = QueensState(8, 8)
        self.state._board[0][6] = 1
        self.state._board[6][0] = 1
        self.assertEqual(self.state.any_queens_unsafe(), True)


if __name__ == '__main__':

    unittest.main()
