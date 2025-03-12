import numpy as np

def print_board(board):
    for row in board:
        row_str = ""
        for cell in row:
            if cell == 1:
                row_str += "Q "
            else:
                row_str += ". "
        print(row_str)
    print("\n")

def is_safe(board, row, col):
    for i in range(len(board)):
        if board[i][col] == 1:
            return False
        if board[row][i] == 1:
            return False
        if row + i < len(board) and col + i < len(board):
            if board[row + i][col + i] == 1:
                return False
        if row - i >= 0 and col - i >= 0:
            if board[row - i][col - i] == 1:
                return False
        if row + i < len(board) and col - i >= 0:
            if board[row + i][col - i] == 1:
                return False
        if row - i >= 0 and col + i < len(board):
            if board[row - i][col + i] == 1:
                return False
    return True

def solve(board, row):
    if row == len(board):
        print_board(board)
        return True
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0
    
    return False

def eight_queens():
    board = np.zeros((8, 8))
    if not solve(board, 0):
        print("No solution")
import unittest
from unittest.mock import patch
from io import StringIO


class TestEightQueens(unittest.TestCase):
    def setUp(self):
        self.board = [['.' for _ in range(8)] for _ in range(8)]

    def test_solution_exists(self):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            eight_queens()
            self.assertTrue("Q" in fake_out.getvalue(), "The board should contain at least one queen.")

    def test_correct_number_of_queens(self):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            eight_queens()
            output = fake_out.getvalue().strip().split('\n\n')  # Split the output into blocks for each board
            for board in output:
                # Count number of 'Q's in each board
                num_queens = board.count('Q')
                self.assertEqual(num_queens, 8, "Each board should contain exactly 8 queens.")

    def test_no_solution_scenario(self):
        # As the Eight Queens always has a solution for an 8x8 board,
        # to test the 'No solution' output we need a scenario where no solution exists.
        # We will manipulate the board to a smaller size where no solution is possible.
        # Here we consider a 3x3 board for simplicity.
        def no_solution_queens():
            board = [['.' for _ in range(3)] for _ in range(3)]
            if not solve_queens(board, 0):
                print("No solution")

        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            no_solution_queens()
            self.assertIn("No solution", fake_out.getvalue(), "Should print 'No solution' when no solution exists.")

if __name__ == '__main__':
    unittest.main()