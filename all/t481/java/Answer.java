package org.real.temp;

/**
 * @brief Prints a 3x3 game board to the console.
 *
 * This method takes a 2D array representing a game board and prints
 * it in a formatted manner, displaying the contents of each cell.
 * The board is assumed to be a square of size 3x3, and each cell can
 * contain either a character representing a player's move ('X' or 'O')
 * or an empty space (' ').
 *
 * The output format includes a row of dashes to separate the rows of
 * the board, and each cell is enclosed within vertical bars.
 * This method does not return any value.
 *
 * @param board A 2D array of characters, where each character represents
 *              the state of a cell in the game board. The board must be
 *              of size 3x3, and each character can be 'X', 'O', or ' '.
 * For example:
 *      input: [['X', 'O', 'X'],
 *              [' ', 'X', 'O'],
 *              ['O', ' ', ' ']]
 *      output: -------------\n| X | O | X | \n-------------\n|   | X | O | \n-------------\n| O |   |   | \n-------------\n
 */
public class Answer {
    public static void printBoard(char[][] board) {
        final int boardSize = 3; // Size of the board
        System.out.println("-------------");

        // Loop through each row
        for (int i = 0; i < boardSize; i++) {
            System.out.print("| "); // Start of the row

            // Loop through each column in the row
            for (int j = 0; j < boardSize; j++) {
                System.out.print(board[i][j] + " | "); // Print each cell
            }

            System.out.println(); // End of the row
            System.out.println("-------------"); // Print the row separator
        }
    }
}