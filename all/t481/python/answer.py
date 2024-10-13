def print_board(board):
    """Prints the tic-tac-toe board.

    Args:
        board (list of list of str): The tic-tac-toe board to print,
        with characters representing the players' moves.
    """
    board_size = 3  # Size of the board
    print("-------------")  # Print the top border
    # Loop through each row
    for i in range(board_size):
        print("| ", end="")  # Start of the row
        # Loop through each column in the row
        for j in range(board_size):
            print(board[i][j], end=" | ")  # Print each cell
        print()  # End of the row
        print("-------------")  # Print the row separator