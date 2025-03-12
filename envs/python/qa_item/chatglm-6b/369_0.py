
def eight_queens():
    """
    solve the Eight Queens problem, if a solution is found, it will print out the configuration of the chessboard. If all queens cannot be placed, print "No solution"
    print example as below:
   .. Q.....
   .... Q...
   . Q......
   ....... Q
   .... Q...
   ...... Q.
    Q.......
    """
    # Initialize the board to all 0's
    board = [0] * 8

    # Iterate over all possible positions of the queens
    for i in range(8):
        # Check if all queens can be placed in the current position
        if board[i]!= 0:
            # If not, return "No solution"
            return "No solution"
        # Add the queen to the board
        board[i] = 1

    # Print the configuration of the chessboard
    return "".join(str(x) for x in board)

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