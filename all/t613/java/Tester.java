package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    private final Answer answer = new Answer();

    @Test
    public void testValidSudoku() {
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

        assertTrue(answer.solveSudoku(board));
        assertTrue(isSolved(board));
    }

    @Test
    public void testSudokuWithNoSolution() {
        int[][] board = {
            {5, 1, 1, 0, 7, 0, 0, 0, 0},
            {6, 0, 0, 1, 9, 5, 0, 0, 0},
            {0, 9, 8, 0, 0, 0, 0, 6, 0},
            {8, 0, 0, 0, 6, 0, 0, 0, 3},
            {4, 0, 0, 8, 0, 3, 0, 0, 1},
            {7, 0, 0, 0, 2, 0, 0, 0, 6},
            {0, 6, 0, 0, 0, 0, 2, 8, 0},
            {0, 0, 0, 4, 1, 9, 0, 0, 5},
            {0, 0, 0, 0, 8, 0, 0, 7, 9}
        };

        assertFalse(answer.solveSudoku(board));
    }

    @Test
    public void testAlreadySolvedSudoku() {
        int[][] board = {
            {5, 3, 4, 6, 7, 8, 9, 1, 2},
            {6, 7, 2, 1, 9, 5, 3, 4, 8},
            {1, 9, 8, 3, 4, 2, 5, 6, 7},
            {8, 5, 9, 7, 6, 1, 4, 2, 3},
            {4, 2, 6, 8, 5, 3, 7, 9, 1},
            {7, 1, 3, 9, 2, 4, 8, 5, 6},
            {9, 6, 1, 5, 3, 7, 2, 8, 4},
            {2, 8, 7, 4, 1, 9, 6, 3, 5},
            {3, 4, 5, 2, 8, 6, 1, 7, 9}
        };

        assertTrue(answer.solveSudoku(board));
        assertTrue(isSolved(board));
    }

    @Test
    public void testPartiallyFilledSudoku() {
        int[][] board = {
            {0, 0, 0, 0, 7, 0, 0, 0, 0},
            {0, 0, 0, 1, 0, 0, 0, 5, 0},
            {0, 0, 0, 0, 0, 5, 0, 4, 0},
            {0, 6, 1, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 3, 0, 0, 0},
            {0, 0, 0, 0, 0, 6, 2, 0, 0},
            {0, 5, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 0, 0}
        };

        assertTrue(answer.solveSudoku(board));
        assertTrue(isSolved(board));
    }

    @Test
    public void testEmptySudoku() {
        int[][] board = new int[9][9]; // All cells are initially 0 (empty)

        assertTrue(answer.solveSudoku(board));
        assertTrue(isSolved(board));
    }

    private boolean isSolved(int[][] board) {
        // Check if the board is valid and solved
        for (int row = 0; row < 9; row++) {
            boolean[] rowCheck = new boolean[9];
            boolean[] colCheck = new boolean[9];
            boolean[] boxCheck = new boolean[9];

            for (int col = 0; col < 9; col++) {
                // Check row
                if (board[row][col] != 0) {
                    if (rowCheck[board[row][col] - 1]) return false;
                    rowCheck[board[row][col] - 1] = true;
                }
                // Check column
                if (board[col][row] != 0) {
                    if (colCheck[board[col][row] - 1]) return false;
                    colCheck[board[col][row] - 1] = true;
                }
                // Check 3x3 box
                int boxRow = 3 * (row / 3);
                int boxCol = 3 * (col / 3);
                if (board[boxRow + col / 3][boxCol + col % 3] != 0) {
                    if (boxCheck[board[boxRow + col / 3][boxCol + col % 3] - 1]) return false;
                    boxCheck[board[boxRow + col / 3][boxCol + col % 3] - 1] = true;
                }
            }
        }
        return true; // Board is valid and solved
    }
}
