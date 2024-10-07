/**
 * @brief Prints a 3x3 game board to the console.
 *
 * This function takes a 2D vector representing a game board and prints
 * it in a formatted manner, displaying the contents of each cell.
 * The board is assumed to be a square of size 3x3, and each cell can
 * contain either a character representing a player's move ('X' or 'O')
 * or an empty space (' ').
 *
 * The output format includes a row of dashes to separate the rows of
 * the board, and each cell is enclosed within vertical bars.
 * The function does not return any value.
 *
 * @param board A 2D vector of characters, where each character represents
 *              the state of a cell in the game board. The board must be
 *              of size 3x3, and each character can be 'X', 'O', or ' '.
 * For example:
 *      input: [['X', 'O', 'X'],
 *              [' ', 'X', 'O'],
 *              ['O', ' ', ' ']]
 *      output: -------------\n| X | O | X | \n-------------\n|   | X | O | \n-------------\n| O |   |   | \n-------------\n
 */
void printBoard(const vector<vector<char>>& board) {}