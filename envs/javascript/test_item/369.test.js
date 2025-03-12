/**
 * Solves the Eight Queens problem. If a solution is found, it will print out the configuration of the chessboard.
 * If all queens cannot be placed, it will print "No solution".
 */
function eightQueens() {
    const N = 8;
    let board = Array.from({ length: N }, () => Array(N).fill('.'));

    function isSafe(board, row, col) {
        // Check this row on left side
        for (let i = 0; i < col; i++) {
            if (board[row][i] === 'Q') return false;
        }

        // Check upper diagonal on left side
        for (let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') return false;
        }

        // Check lower diagonal on left side
        for (let i = row, j = col; j >= 0 && i < N; i++, j--) {
            if (board[i][j] === 'Q') return false;
        }

        return true;
    }

    function solveNQueensUtil(board, col) {
        if (col >= N) return true;

        for (let i = 0; i < N; i++) {
            if (isSafe(board, i, col)) {
                board[i][col] = 'Q';

                if (solveNQueensUtil(board, col + 1)) return true;

                board[i][col] = '.'; // Backtrack
            }
        }

        return false;
    }

    if (!solveNQueensUtil(board, 0)) {
        console.log("No solution");
    } else {
        board.forEach(row => console.log(row.join(' ')));
    }
}

// Call the function to solve the Eight Queens problem
eightQueens();
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
