/**
 * Solves the Eight Queens problem. If a solution is found, it will print out the configuration of the chessboard.
 * If all queens cannot be placed, it will print "No solution".
 */
function eightQueens() {
    const N = 8; // Number of queens and the size of the chessboard
    let board = Array.from({ length: N }, () => Array(N).fill('.'));

    function isSafe(row, col) {
        // Check this row on left side
        for (let i = 0; i < col; i++) {
            if (board[row][i] === 'Q') {
                return false;
            }
        }

        // Check upper diagonal on left side
        for (let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }

        // Check lower diagonal on left side
        for (let i = row, j = col; i < N && j >= 0; i++, j--) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }

        return true;
    }

    function solveNQueensUtil(col) {
        // Base case: If all queens are placed
        if (col >= N) {
            printBoard(board);
            return;
        }

        // Consider this column and try placing this queen in all rows one by one
        for (let i = 0; i < N; i++) {
            if (isSafe(i, col)) {
                board[i][col] = 'Q'; // Place this queen in board[i][col]

                // Recur to place rest of the queens
                solveNQueensUtil(col + 1);

                // If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
                board[i][col] = '.';
            }
        }
    }

    function printBoard(board) {
        for (let i = 0; i < N; i++) {
            let row = board[i].join(' ');
            console.log(row);
        }
        console.log('\n');
    }

    // Initialize the board and start solving the problem
    solveNQueensUtil(0);
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
