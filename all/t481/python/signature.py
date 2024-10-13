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
                                  of size 3x3, and each character can be 'X', 'O', or ' '.
                                  For example:
                                  input: [['X', 'O', 'X'],
                                          [' ', 'X', 'O'],
                                          ['O', ' ', ' ']]
                                  output: -------------
                                          | X | O | X |
                                          -------------
                                          |   | X | O |
                                          -------------
                                          | O |   |   |
                                          -------------
    """