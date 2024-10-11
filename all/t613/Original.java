package main;

/**
 * This class is for testing purposes
 * I can be used to find out the solution to see if the actually desirable algorithm solves the sudoku correctly
 * It has been written by ChatGPT-4 Data Analysis
 */
public class BacktrackingSolver {
    // The size of the Sudoku grid
    public static final int SIZE = 9;
    // The size of the smaller box inside the Sudoku
    public static final int SUBGRIDSIZE = 3;

    // Function to check whether a number can be placed at the given row, column
    private static boolean canPlaceNum(int[][] board, int row, int col, int num) {
        // Check the num in the current row
        for (int x = 0; x < SIZE; x++)
            if (board[row][x] == num)
                return false;

        // Check the num in the current column
        for (int x = 0; x < SIZE; x++)
            if (board[x][col] == num)
                return false;

        // Check the num in the current 3*3 matrix
        int startRow = row - row % SUBGRIDSIZE, startCol = col - col % SUBGRIDSIZE;
        for (int i = 0; i < SUBGRIDSIZE; i++)
            for (int j = 0; j < SUBGRIDSIZE; j++)
                if (board[i + startRow][j + startCol] == num)
                    return false;

        return true;
    }

    // Takes a partially filled-in grid and attempts to assign values to all unassigned locations in such a way to meet the requirements for Sudoku solution
    private static boolean solveSudoku(int[][] board) {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                // We skip the cells that are pre-filled
                if (board[i][j] != 0)
                    continue;

                // Try numbers from 1 to 9 in the current cell
                for (int num = 1; num <= SIZE; num++) {
                    if (canPlaceNum(board, i, j, num)) {
                        board[i][j] = num; // Place num at the current cell

                        if (solveSudoku(board)) // Recur with the updated board
                            return true;

                        board[i][j] = 0; // If placing num doesn't lead to a solution, backtrack
                    }
                }

                // Trigger backtracking
                return false;
            }
        }
        return true; // Sudoku solved
    }

    public static int[][] solve(int[][] board) {
        if (solveSudoku(board))
            return board;
        else
            throw new RuntimeException("No solution exists for the given Sudoku");
    }

    public static void main(String[] args) {
        int[][] board = new int[][]{
                {5, 3, 0, 0, 7, 0, 0, 0, 0},
                {6, 0, 0, 1, 9, 5, 0, 0, 0},
                {0, 9, 8, 0, 0, 0, 0, 6, 0},
                {8, 0, 0, 0, 6, 0, 0, 0, 3},
                {4, 0, 0, 8, 0, 3, 0, 0, 1},
                {7, 0, 0, 0, 2, 0, 0, 0, 6},
                {0, 6, 0, 0, 0, 0, 2, 8, 0},
                {0, 0, 0, 4, 1, 9, 0, 0, 5},
                {0, 0, 0, 0, 8, 0, 0, 7, 9}
        };

        int[][] solvedBoard = solve(board);

        // Printing the solved Sudoku
        for (int r = 0; r < SIZE; r++) {
            for (int d = 0; d < SIZE; d++) {
                System.out.print(solvedBoard[r][d]);
                System.out.print(" ");
            }
            System.out.print("\n");

            if ((r + 1) % SUBGRIDSIZE == 0)
                System.out.print("");
        }
    }
}