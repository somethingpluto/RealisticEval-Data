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