// Additions at the start of the function
function printBoard(board: string[][]): void {
  if (board.length !== 3 || board.some(row => row.length !== 3)) {
    throw new Error('Board must be 3x3.');
  }

  // ... existing code ...

  // Additions at the end of the function
  const winningCombinations = [
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]],
  ];

  const checkForWinner = (board: string[][]): string | null => {
    for (const combination of winningCombinations) {
      const [a, b, c] = combination;
      if (board[a[0]][a[1]] && board[a[0]][a[1]] === board[b[0]][b[1]] && board[a[0]][a[1]] === board[c[0]][c[1]]) {
        return board[a[0]][a[1]];
      }
    }
    return null;
  };

  const winner = checkForWinner(board);
  if (winner) {
    console.log(`Winner: ${winner}`);
  }
}
describe("printBoard outputs correct format", () => {
    const board1: string[][] = [
        ['X', 'O', 'X'],
        [' ', 'X', 'O'],
        ['O', ' ', ' ']
    ];

    const board2: string[][] = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ];

    const board3: string[][] = [
        ['X', 'X', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', ' ']
    ];

    const board4: string[][] = [
        ['O', 'O', 'O'],
        ['X', 'X', 'X'],
        ['X', 'O', ' ']
    ];

    const board5: string[][] = [
        ['X', ' ', ' '],
        [' ', 'X', ' '],
        [' ', ' ', 'X']
    ];

    const board6: string[][] = [
        [' ', 'O', ' '],
        ['O', ' ', 'O'],
        [' ', 'O', ' ']
    ];

    const expectedOutputs = {
        board1: "-------------\n| X | O | X | \n-------------\n|   | X | O | \n-------------\n| O |   |   | \n-------------\n",
        board2: "-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n",
        board3: "-------------\n| X | X | X | \n-------------\n| O | O |   | \n-------------\n|   |   |   | \n-------------\n",
        board4: "-------------\n| O | O | O | \n-------------\n| X | X | X | \n-------------\n| X | O |   | \n-------------\n",
        board5: "-------------\n| X |   |   | \n-------------\n|   | X |   | \n-------------\n|   |   | X | \n-------------\n",
        board6: "-------------\n|   | O |   | \n-------------\n| O |   | O | \n-------------\n|   | O |   | \n-------------\n"
    };

    const captureConsoleOutput = (fn: () => void): string => {
        const originalLog = console.log;
        let output = '';
        console.log = (...args: any[]) => { output += args.join(' ') + '\n'; };
        
        fn();

        console.log = originalLog; // Restore original console.log
        return output;
    };

    test("Test case 1", () => {
        const output = captureConsoleOutput(() => printBoard(board1));
        expect(output).toBe(expectedOutputs.board1);
    });

    test("Test case 2", () => {
        const output = captureConsoleOutput(() => printBoard(board2));
        expect(output).toBe(expectedOutputs.board2);
    });

    test("Test case 3", () => {
        const output = captureConsoleOutput(() => printBoard(board3));
        expect(output).toBe(expectedOutputs.board3);
    });

    test("Test case 4", () => {
        const output = captureConsoleOutput(() => printBoard(board4));
        expect(output).toBe(expectedOutputs.board4);
    });

    test("Test case 5", () => {
        const output = captureConsoleOutput(() => printBoard(board5));
        expect(output).toBe(expectedOutputs.board5);
    });

    test("Test case 6", () => {
        const output = captureConsoleOutput(() => printBoard(board6));
        expect(output).toBe(expectedOutputs.board6);
    });
});
