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

from queens import QueensState, Position, DuplicateQueenError, MissingQueenError
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
        self.assertTrue(self.state.has_queen(test_position_exists))
        self.assertFalse(self.state.has_queen(test_position_empty))

    def test_any_queens_unsafe(self):
        # Safe
        self.state._board[0][0] = 1
        self.state._board[1][2] = 1
        self.state._board[2][4] = 1
        self.assertFalse(self.state.any_queens_unsafe())

        # Row
        self.state._board[0][1] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Column
        self.state._board[0][1] = 0
        self.state._board[1][0] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Diagonal
        self.state = QueensState(8, 8)
        self.state._board[0][0] = 1
        self.state._board[7][7] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Anti-Diagonal
        self.state = QueensState(8, 8)
        self.state._board[0][6] = 1
        self.state._board[6][0] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Another Anti-Diagonal
        self.state = QueensState(8, 8)
        self.state._board[0][7] = 1
        self.state._board[1][6] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # No queens
        self.state = QueensState(8, 8)
        self.assertFalse(self.state.any_queens_unsafe())

        # Single queen
        self.state = QueensState(8, 8)
        self.state._board[3][4] = 1
        self.assertFalse(self.state.any_queens_unsafe())

        # Multiple queens, no conflicts
        self.state = QueensState(8, 8)
        self.state._board[0][0] = 1
        self.state._board[1][2] = 1
        self.state._board[2][4] = 1
        self.assertFalse(self.state.any_queens_unsafe())

        # Conflict in same row
        self.state = QueensState(8, 8)
        self.state._board[4][1] = 1
        self.state._board[4][7] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Conflict in same column
        self.state = QueensState(8, 8)
        self.state._board[1][5] = 1
        self.state._board[7][5] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Conflict on a diagonal
        self.state = QueensState(8, 8)
        self.state._board[0][0] = 1
        self.state._board[7][7] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Conflict on the other diagonal
        self.state = QueensState(8, 8)
        self.state._board[0][7] = 1
        self.state._board[7][0] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Conflict among many queens
        self.state = QueensState(8, 8)
        self.state._board[0][0] = 1
        self.state._board[1][2] = 1
        self.state._board[2][4] = 1
        self.state._board[3][6] = 1
        self.state._board[7][2] = 1
        self.assertTrue(self.state.any_queens_unsafe())

        # Known safe configuration
        self.state = QueensState(8, 8)
        safe_positions = [
            Position(0, 0), Position(1, 4), Position(2, 7), Position(3, 5),
            Position(4, 2), Position(5, 6), Position(6, 1), Position(7, 3)
        ]
        self.state = self.state.with_queens_added(safe_positions)
        self.assertFalse(self.state.any_queens_unsafe())

        # Close positions without conflict
        self.state = QueensState(8, 8)
        self.state._board[0][0] = 1
        self.state._board[2][1] = 1
        self.assertFalse(self.state.any_queens_unsafe())

        # Another non-conflicting case
        self.state = QueensState(8, 8)
        self.state._board[0][7] = 1
        self.state._board[2][4] = 1
        self.assertFalse(self.state.any_queens_unsafe())

        # More obvious non-conflicting
        self.state = QueensState(8, 8)
        self.state._board[0][7] = 1
        self.state._board[3][1] = 1
        self.assertFalse(self.state.any_queens_unsafe())

    def test_with_queens_added(self):
        # Assignment
        positions = [Position(row=0, column=1), Position(row=1, column=1)]
        new = self.state.with_queens_added(positions)
        self.assertTrue(new.has_queen(positions[0]))
        self.assertTrue(new.has_queen(positions[1]))

        # Duplicate Error
        self.state = new
        with self.assertRaises(DuplicateQueenError):
            self.state.with_queens_added(positions)

    def test_with_queens_removed(self):
        positions = [Position(row=0, column=1), Position(row=1, column=1)]

        # Missing Queen Error
        with self.assertRaises(MissingQueenError):
            self.state.with_queens_removed(positions)

        self.state = self.state.with_queens_added(positions)
        # Removing valid
        self.state = self.state.with_queens_removed(positions)
        self.assertFalse(self.state.has_queen(positions[0]))
        self.assertFalse(self.state.has_queen(positions[1]))

    def test_queen_count_updates_after_add_and_remove(self):
        positions = [Position(0, 1), Position(1, 3), Position(2, 5)]
        s2 = self.state.with_queens_added(positions)
        self.assertEqual(s2.queen_count(), 3)
        # original unchanged
        self.assertEqual(self.state.queen_count(), 0)
        s3 = s2.with_queens_removed([positions[0]])
        self.assertEqual(s3.queen_count(), 2)
        self.assertEqual(s2.queen_count(), 3)
        self.assertEqual(self.state.queen_count(), 0)

    def test_with_queens_added_is_immutable_has_queen(self):
        p = Position(0, 0)
        s2 = self.state.with_queens_added([p])
        self.assertFalse(self.state.has_queen(p))
        self.assertTrue(s2.has_queen(p))

if __name__ == '__main__':
    unittest.main()
