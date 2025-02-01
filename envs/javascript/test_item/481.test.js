/**
 * Prints a 3x3 game board to the console.
 *
 * This function takes a 2D array representing a game board and prints
 * it in a formatted manner, displaying the contents of each cell.
 * The board is assumed to be a square of size 3x3, and each cell can
 * contain either a character representing a player's move ('X' or 'O')
 * or an empty space (' ').
 *
 * The output format includes a row of dashes to separate the rows of
 * the board, and each cell is enclosed within vertical bars.
 * The function does not return any value.
 *
 * @param {Array<Array<string>>} board A 2D array of characters, where each character represents
 *              the state of a cell in the game board. The board must be
 *              of size 3x3, and each character can be 'X', 'O', or ' '.
 */
function printBoard(board) {
    const separator = '-------------';
    const cellFormat = '| %s |';

    console.log(separator);
    for (let i = 0; i < board.length; i++) {
        let row = '';
        for (let j = 0; j < board[i].length; j++) {
            row += cellFormat.replace('%s', board[i][j]);
        }
        console.log(row);
        if (i < board.length - 1) {
            console.log(separator);
        }
    }
}
describe("printBoard outputs correct format", () => {
    const board1 = [
        ['X', 'O', 'X'],
        [' ', 'X', 'O'],
        ['O', ' ', ' ']
    ];

    const board2 = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ];

    const board3 = [
        ['X', 'X', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', ' ']
    ];

    const board4 = [
        ['O', 'O', 'O'],
        ['X', 'X', 'X'],
        ['X', 'O', ' ']
    ];

    const board5 = [
        ['X', ' ', ' '],
        [' ', 'X', ' '],
        [' ', ' ', 'X']
    ];

    const board6 = [
        [' ', 'O', ' '],
        ['O', ' ', 'O'],
        [' ', 'O', ' ']
    ];

    // Helper function to capture console output
    function captureOutput(fn, ...args) {
        const originalLog = console.log;
        let output = '';
        console.log = (msg) => {
            output += msg + '\n';
        };
        fn(...args);
        console.log = originalLog;
        return output;
    }

    test("Test case 1", () => {
        const expectedOutput = "-------------\n| X | O | X | \n-------------\n|   | X | O | \n-------------\n| O |   |   | \n-------------\n";
        const output = captureOutput(printBoard, board1);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 2", () => {
        const expectedOutput = "-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n";
        const output = captureOutput(printBoard, board2);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 3", () => {
        const expectedOutput = "-------------\n| X | X | X | \n-------------\n| O | O |   | \n-------------\n|   |   |   | \n-------------\n";
        const output = captureOutput(printBoard, board3);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 4", () => {
        const expectedOutput = "-------------\n| O | O | O | \n-------------\n| X | X | X | \n-------------\n| X | O |   | \n-------------\n";
        const output = captureOutput(printBoard, board4);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 5", () => {
        const expectedOutput = "-------------\n| X |   |   | \n-------------\n|   | X |   | \n-------------\n|   |   | X | \n-------------\n";
        const output = captureOutput(printBoard, board5);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 6", () => {
        const expectedOutput = "-------------\n|   | O |   | \n-------------\n| O |   | O | \n-------------\n|   | O |   | \n-------------\n";
        const output = captureOutput(printBoard, board6);
        expect(output).toBe(expectedOutput);
    });
});
