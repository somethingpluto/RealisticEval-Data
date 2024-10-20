package org.real.temp;

public class Answer {

    public static void main(String[] args) {
        eightQueens();
    }

    private static void printBoard(char[][] board) {
        for (char[] row : board) {
            System.out.println(new String(row).replace('.', ' ').trim());
        }
        System.out.println();
    }

    private static boolean isSafe(char[][] board, int row, int col) {
        // Check this row on the left side
        for (int i = 0; i < col; i++) {
            if (board[row][i] == 'Q') {
                return false;
            }
        }

        // Check upper diagonal on the left side
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        // Check lower diagonal on the left side
        for (int i = row, j = col; i < board.length && j >= 0; i++, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    private static boolean solveQueens(char[][] board, int col) {
        // Base case: If all queens are placed
        if (col >= board.length) {
            printBoard(board);
            return true;
        }

        // Consider this column and try placing this queen in all rows one by one
        boolean solutionFound = false;
        for (int i = 0; i < board.length; i++) {
            if (isSafe(board, i, col)) {
                board[i][col] = 'Q';
                if (solveQueens(board, col + 1)) {
                    solutionFound = true;
                }
                board[i][col] = '.';  // Backtrack
            }
        }

        return solutionFound;
    }

    private static void eightQueens() {
        char[][] board = new char[8][8];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                board[i][j] = '.';
            }
        }
        if (!solveQueens(board, 0)) {
            System.out.println("No solution");
        }
    }
}