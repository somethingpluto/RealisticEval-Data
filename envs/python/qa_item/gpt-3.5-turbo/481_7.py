def print_board(board):
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        print("-" * (cols*4 + 1))
        for j in range(cols):
            print("| " + board[i][j], end=' ')
        print("|")
    print("-" * (cols*4 + 1))
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