describe('TestEightQueens', () => {
  beforeEach(() => {
      // Setup any common state here if needed
  });

  describe('test_solution_exists', () => {
      it('should contain at least one queen', () => {
          const fakeOut = { data: '' };
          const writeMock = (chunk) => {
              fakeOut.data += chunk;
          };

          const originalConsoleLog = console.log;
          console.log = writeMock;

          eightQueens();

          expect(fakeOut.data.includes('Q')).toBe(true);

          console.log = originalConsoleLog;
      });
  });

  describe('test_correct_number_of_queens', () => {
      it('each board should contain exactly 8 queens', () => {
          const fakeOut = { data: '' };
          const writeMock = (chunk) => {
              fakeOut.data += chunk;
          };

          const originalConsoleLog = console.log;
          console.log = writeMock;

          eightQueens();

          const output = fakeOut.data.trim().split('\n\n');
          for (const board of output) {
              const numQueens = (board.match(/Q/g) || []).length;
              expect(numQueens).toEqual(8);
          }

          console.log = originalConsoleLog;
      });
  });

  describe('test_no_solution_scenario', () => {
      it('should print "No solution" when no solution exists', () => {
          const fakeOut = { data: '' };
          const writeMock = (chunk) => {
              fakeOut.data += chunk;
          };

          const originalConsoleLog = console.log;
          console.log = writeMock;

          function noSolutionQueens() {
              const board = Array.from({ length: 3 }, () => Array(3).fill('.'));
              if (!solveQueens(board, 0)) {
                  console.log("No solution");
              }
          }

          noSolutionQueens();

          expect(fakeOut.data.includes('No solution')).toBe(true);

          console.log = originalConsoleLog;
      });
  });
});