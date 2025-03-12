def eight_queens():
    """
    solve the Eight Queens problem, if a solution is found, it will print out the configuration of the chessboard. If all queens cannot be placed, print "No solution"
    print example as below:
    . . Q . . . . .
    . . . . Q . . .
    . Q . . . . . .
    . . . . . . . Q
    . . . . . Q . .
    . . . Q . . . .
    . . . . . . Q .
    Q . . . . . . .
    Returns:

    """
    def is_safe(board, row, col):
        # check this row on left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # check lower diagonal on left side
        for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve_n_queens_util(board, col):
        # base case: If all queens are placed
        # then return true
        if col >= len(board):
            return True

        # Consider this column and try placing
        # this queen in all rows one by one
        for i in range(len(board)):
            if is_safe(board, i, col):
                # place this queen in board[i][col]
                board[i][col] = 'Q'

                # recur to place rest of the queens
                if solve_n_queens_util(board, col + 1) == True:
                    return True

                # If placing queen in board[i][col
                # doesn't lead to a solution, then
                # remove queen from board[i][col]
                board[i][col] = '.'

        # If the queen cannot be placed in any row in
        # this column col then return false
        return False

    def solve_n_queens(n):
        board = [['.' for _ in range(n)] for _ in range(n)]

        if solve_n_queens_util(board, 0) == False:
            print("No solution")
            return False

        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
        return True

    solve_n_queens(8)

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