def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


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
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_queens(board, col):
    # Base case: If all queens are placed
    if col >= len(board):
        print_board(board)
        return True

    # Consider this column and try placing this queen in all rows one by one
    solution_found = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 'Q'
            if solve_queens(board, col + 1):
                solution_found = True
            board[i][col] = '.'  # Backtrack

    return solution_found


def eight_queens():
    board = [['.' for _ in range(8)] for _ in range(8)]
    if not solve_queens(board, 0):
        print("No solution")

eight_queens()