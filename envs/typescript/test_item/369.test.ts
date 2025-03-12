// Importing readline-sync for synchronous user input
import * as readlineSync from 'readline-sync';

/**
 * Solves the Eight Queens problem. If a solution is found, it will print out the configuration of the chessboard.
 * If all queens cannot be placed, it prints "No solution".
 * 
 * Example output:
 * 
 * . . Q . . . . .
 * . . . . Q . . .
 * . Q . . . . . .
 * . . . . . . . Q
 * . . . . . Q . .
 * . . . Q . . . .
 * . . . . . . Q .
 * Q . . . . . . .
 */
function eightQueens(): void {
  // ... (rest of the eightQueens function code)

  // After finding a solution, ask the user if they want to see another solution
  const showAnotherSolution = readlineSync.keyInYN('Do you want to see another solution? (y/n)');
  if (showAnotherSolution === 'y') {
    // Reset the board and call the function again to find another solution
    board = Array(8).fill(0).map(() => Array(8).fill('.'));
    eightQueens();
  }
}

eightQueens();
describe('TestEightQueens', () => {
  beforeEach(() => {
      // Setup can be done here if needed
  });

  it('should contain at least one queen', () => {
      const originalConsoleLog = console.log;
      let fakeOut = '';

      // Mock console.log to capture output
      console.log = jest.fn((output) => {
          fakeOut += output;
      });

      eightQueens();

      // Restore original console.log
      console.log = originalConsoleLog;

      expect(fakeOut.includes('Q')).toBe(true, 'The board should contain at least one queen.');
  });

  it('should contain exactly 8 queens', () => {
      const originalConsoleLog = console.log;
      let fakeOut = '';

      // Mock console.log to capture output
      console.log = jest.fn((output) => {
          fakeOut += output;
      });

      eightQueens();

      // Restore original console.log
      console.log = originalConsoleLog;

      const boards = fakeOut.trim().split('\n\n'); // Split the output into blocks for each board
      for (const board of boards) {
          const numQueens = (board.match(/Q/g) || []).length;
          expect(numQueens).toBe(8, 'Each board should contain exactly 8 queens.');
      }
  });

  it('should print "No solution" when no solution exists', () => {
      const originalConsoleLog = console.log;
      let fakeOut = '';

      // Define a function that simulates a scenario with no solution
      function noSolutionQueens() {
          const board: string[][] = Array.from({ length: 3 }, () => Array(3).fill('.'));
          if (!solveQueens(board, 0)) {
              console.log("No solution");
          }
      }

      // Mock console.log to capture output
      console.log = jest.fn((output) => {
          fakeOut += output;
      });

      noSolutionQueens();

      // Restore original console.log
      console.log = originalConsoleLog;

      expect(fakeOut.includes('No solution')).toBe(true, 'Should print "No solution" when no solution exists.');
  });
});
