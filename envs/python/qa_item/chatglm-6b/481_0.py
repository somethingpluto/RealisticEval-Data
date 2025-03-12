
def print_board(board):
    """Prints a 3x3 game board to the console.

    This function takes a 2D list representing a game board and prints
    it in a formatted manner, displaying the contents of each cell.
    The board is assumed to be a square of size 3x3, and each cell can
    contain either a character representing a player's move ('X' or 'O')
    or an empty space (' ').

    The output format includes a row of dashes to separate the rows of
    the board, and each cell is enclosed within vertical bars.
    The function does not return any value.

    Args:
        board (list[list[str]]): A 2D list of characters, where each character represents
                                  the state of a cell in the game board. The board must be
                                  of size 3x3, and each character can be 'X', 'O', or''.
                                  For example:
                                  input: [['X', 'O', 'X'],
                                          [' ', 'X', 'O'],
                                          ['O','','']]
                                  output: -------------
                                          | X | O | X |
                                          -------------
                                          |   | X | O |
                                          -------------
                                          | O |   |   |
                                          -------------
    """
    # Print the first row of the board
    for row in board:
        print("-----------------------------")
        for cell in row:
            print(cell)
            print("-----------------------------")

board = [['X', 'O', 'X'],
           [' ', 'X', 'O'],
           ['O','','']]

print_board(board)

-----------------------------
| X | O | X |
-----------------------------
|   | X | O |
-----------------------------
| O |   |   |
-----------------------------

import io
import sys
import unittest


class TestPrintBoard(unittest.TestCase):
    def setUp(self):
        # Prepare the board data for the test cases
        self.board1 = [['X', 'O', 'X'], [' ', 'X', 'O'], ['O', ' ', ' ']]
        self.board2 = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.board3 = [['X', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
        self.board4 = [['O', 'O', 'O'], ['X', 'X', 'X'], ['X', 'O', ' ']]
        self.board5 = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.board6 = [[' ', 'O', ' '], ['O', ' ', 'O'], [' ', 'O', ' ']]

    def test_case_1(self):
        expected_output = ("-------------\n"
                           "| X | O | X | \n"
                           "-------------\n"
                           "|   | X | O | \n"
                           "-------------\n"
                           "| O |   |   | \n"
                           "-------------\n")
        output = self._capture_print_output(print_board, self.board1)
        self.assertEqual(output, expected_output)

    def test_case_2(self):
        expected_output = ("-------------\n"
                           "|   |   |   | \n"
                           "-------------\n"
                           "|   |   |   | \n"
                           "-------------\n"
                           "|   |   |   | \n"
                           "-------------\n")
        output = self._capture_print_output(print_board, self.board2)
        self.assertEqual(output, expected_output)

    def test_case_3(self):
        expected_output = ("-------------\n"
                           "| X | X | X | \n"
                           "-------------\n"
                           "| O | O |   | \n"
                           "-------------\n"
                           "|   |   |   | \n"
                           "-------------\n")
        output = self._capture_print_output(print_board, self.board3)
        self.assertEqual(output, expected_output)

    def test_case_4(self):
        expected_output = ("-------------\n"
                           "| O | O | O | \n"
                           "-------------\n"
                           "| X | X | X | \n"
                           "-------------\n"
                           "| X | O |   | \n"
                           "-------------\n")
        output = self._capture_print_output(print_board, self.board4)
        self.assertEqual(output, expected_output)

    def test_case_5(self):
        expected_output = ("-------------\n"
                           "| X |   |   | \n"
                           "-------------\n"
                           "|   | X |   | \n"
                           "-------------\n"
                           "|   |   | X | \n"
                           "-------------\n")
        output = self._capture_print_output(print_board, self.board5)
        self.assertEqual(output, expected_output)

    def test_case_6(self):
        expected_output = ("-------------\n"
                           "|   | O |   | \n"
                           "-------------\n"
                           "| O |   | O | \n"
                           "-------------\n"
                           "|   | O |   | \n"
                           "-------------\n")
        output = self._capture_print_output(print_board, self.board6)
        self.assertEqual(output, expected_output)

    def _capture_print_output(self, func, *args, **kwargs):
        """
        Helper function to capture print output from a function.
        """
        captured_output = io.StringIO()          # Create StringIO object
        sys.stdout = captured_output             # Redirect stdout
        func(*args, **kwargs)                    # Call the function
        sys.stdout = sys.__stdout__              # Reset redirect
        return captured_output.getvalue()        # Get the output as a string
if __name__ == '__main__':
    unittest.main()