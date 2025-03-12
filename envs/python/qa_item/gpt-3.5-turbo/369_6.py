from itertools import permutations

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_queens(board, col, n, solutions):
    if col == n:
        solutions.append(board[:])
        return
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_queens(board, col + 1, n, solutions)

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[j] == i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def eight_queens():
    n = 8
    board = [-1] * n
    solutions = []
    solve_queens(board, 0, n, solutions)

    if len(solutions) == 0:
        print("No solution")
    else:
        for solution in solutions:
            print_board(solution, n)
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