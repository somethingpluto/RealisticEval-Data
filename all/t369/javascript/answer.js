function printBoard(board) {
    for (let row of board) {
        console.log(row.join(" "));
    }
    console.log();
}

function isSafe(board, row, col) {
    // Check this row on the left side
    for (let i = 0; i < col; i++) {
        if (board[row][i] === 'Q') {
            return false;
        }
    }

    // Check upper diagonal on the left side
    for (let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] === 'Q') {
            return false;
        }
    }

    // Check lower diagonal on the left side
    for (let i = row, j = col; i < board.length && j >= 0; i++, j--) {
        if (board[i][j] === 'Q') {
            return false;
        }
    }

    return true;
}

function solveQueens(board, col) {
    // Base case: If all queens are placed
    if (col >= board.length) {
        printBoard(board);
        return true;
    }

    // Consider this column and try placing this queen in all rows one by one
    let solutionFound = false;
    for (let i = 0; i < board.length; i++) {
        if (isSafe(board, i, col)) {
            board[i][col] = 'Q';
            if (solveQueens(board, col + 1)) {
                solutionFound = true;
            }
            board[i][col] = '.';  // Backtrack
        }
    }

    return solutionFound;
}

function eightQueens() {
    let board = Array.from({ length: 8 }, () => Array(8).fill('.'));
    if (!solveQueens(board, 0)) {
        console.log("No solution");
    }
}