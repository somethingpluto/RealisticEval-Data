package org.real.temp;

public class Answer {

    private static final int SIZE = 9;

    // Main method to solve the Sudoku puzzle
    public static boolean solveSudoku(int[][] board) {
        for (int row = 0; row < SIZE; row++) {
            for (int col = 0; col < SIZE; col++) {
                // If the cell is empty (0), we try to fill it
                if (board[row][col] == 0) {
                    for (int num = 1; num <= SIZE; num++) {
                        // Check if it's safe to place the number
                        if (canPlaceNum(board, row, col, num)) {
                            board[row][col] = num; // Place the number

                            // Recursively try to solve the rest of the board
                            if (solveSudoku(board)) {
                                return true; // If successful, return true
                            }

                            // If placing num doesn't lead to a solution, backtrack
                            board[row][col] = 0;
                        }
                    }
                    return false; // Trigger backtracking
                }
            }
        }
        return true; // Puzzle solved
    }

    // Method to check if we can place a number in a specific cell
    private static boolean canPlaceNum(int[][] board, int row, int col, int num) {
        // Check the row and column for duplicates
        for (int i = 0; i < SIZE; i++) {
            if (board[row][i] == num || board[i][col] == num) {
                return false;
            }
        }

        // Check the 3x3 sub-square
        int startRow = row - row % 3;
        int startCol = col - col % 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i + startRow][j + startCol] == num) {
                    return false;
                }
            }
        }

        return true; // No duplicates found, it's safe to place the number
    }

    // Utility method to print the Sudoku board
    public static void printBoard(int[][] board) {
        for (int r = 0; r < SIZE; r++) {
            for (int d = 0; d < SIZE; d++) {
                System.out.print(board[r][d] + " ");
            }
            System.out.print("\n");
        }
    }

    // Example usage
    public static void main(String[] args) {
        int[][] board = {
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

        if (solveSudoku(board)) {
            System.out.println("Sudoku solved:");
            printBoard(board);
        } else {
            System.out.println("No solution exists.");
        }
    }
}