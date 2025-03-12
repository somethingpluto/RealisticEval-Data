def eight_queens():
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def solve(board, col):
        if col >= 8:
            return True
        
        for i in range(8):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                
                if solve(board, col + 1):
                    return True
                
                board[i][col] = '.'
        
        return False

    board = [['.' for _ in range(8)] for _ in range(8)]
    
    if solve(board, 0):
        for row in board:
            print(' '.join(row))
    else:
        print("No solution")

# Call the function to solve the Eight Queens problem
eight_queens()
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