package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class Tester {

    @Test
    public void testPrintBoard() {
        char[][] board1 = {
            {'X', 'O', 'X'},
            {' ', 'X', 'O'},
            {'O', ' ', ' '}
        };

        char[][] board2 = {
            {' ', ' ', ' '},
            {' ', ' ', ' '},
            {' ', ' ', ' '}
        };

        char[][] board3 = {
            {'X', 'X', 'X'},
            {'O', 'O', ' '},
            {' ', ' ', ' '}
        };

        char[][] board4 = {
            {'O', 'O', 'O'},
            {'X', 'X', 'X'},
            {'X', 'O', ' '}
        };

        char[][] board5 = {
            {'X', ' ', ' '},
            {' ', 'X', ' '},
            {' ', ' ', 'X'}
        };

        char[][] board6 = {
            {' ', 'O', ' '},
            {'O', ' ', 'O'},
            {' ', 'O', ' '}
        };

        // Test case 1
        assertPrintBoardOutput(board1, "-------------\n| X | O | X | \n-------------\n|   | X | O | \n-------------\n| O |   |   | \n-------------\n");
        
        // Test case 2
        assertPrintBoardOutput(board2, "-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n");

        // Test case 3
        assertPrintBoardOutput(board3, "-------------\n| X | X | X | \n-------------\n| O | O |   | \n-------------\n|   |   |   | \n-------------\n");
        
        // Test case 4
        assertPrintBoardOutput(board4, "-------------\n| O | O | O | \n-------------\n| X | X | X | \n-------------\n| X | O |   | \n-------------\n");
        
        // Test case 5
        assertPrintBoardOutput(board5, "-------------\n| X |   |   | \n-------------\n|   | X |   | \n-------------\n|   |   | X | \n-------------\n");
        
        // Test case 6
        assertPrintBoardOutput(board6, "-------------\n|   | O |   | \n-------------\n| O |   | O | \n-------------\n|   | O |   | \n-------------\n");
    }

}