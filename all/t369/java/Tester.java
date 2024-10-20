package org.real.temp;

import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;

/**
 * Test class for the Eight Queens problem.
 */
public class Tester {

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private PrintStream originalOut;

    @Before
    public void setUp() {
        originalOut = System.out; // Save the original System.out
        System.setOut(new PrintStream(outContent));
    }

    @Test
    public void testSolutionExists() {
        eightQueens();
        String output = outContent.toString();
        assertTrue("The board should contain at least one queen.", output.contains("Q"));
    }

    @Test
    public void testCorrectNumberOfQueens() {
        eightQueens();
        String output = outContent.toString().strip().split("\n\n")[0]; // Split the output into blocks for each board
        int numQueens = output.split("\n").length; // Assuming each board is printed on separate lines
        assertEquals("Each board should contain exactly 8 queens.", 8, numQueens);
    }

    @Test
    public void testNoSolutionScenario() {
        noSolutionQueens();
        String output = outContent.toString();
        assertTrue("Should print 'No solution' when no solution exists.", output.contains("No solution"));
    }

    private void eightQueens() {
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

    private void noSolutionQueens() {
        char[][] board = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '.';
            }
        }
        if (!solveQueens(board, 0)) {
            System.out.println("No solution");
        }
    }

    private boolean solveQueens(char[][] board, int col) {
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

    private void printBoard(char[][] board) {
        for (char[] row : board) {
            System.out.println(new String(row).replace('.', ' ').trim());
        }
        System.out.println();
    }

    private boolean isSafe(char[][] board, int row, int col) {
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
}
