function eightQueens() {
    const board = Array.from({ length: 8 }, () => Array(8).fill('.'));

    function isValid(row, col) {
        for (let i = 0; i < row; i++) {
            if (board[i][col] === 'Q') return false;
            if (col - (row - i) >= 0 && board[i][col - (row - i)] === 'Q') return false;
            if (col + (row - i) < 8 && board[i][col + (row - i)] === 'Q') return false;
        }
        return true;
    }

    function placeQueen(row) {
        if (row === 8) {
            console.log(board.map(row => row.join(' ')).join('\n'));
            return true;
        }

        for (let col = 0; col < 8; col++) {
            if (isValid(row, col)) {
                board[row][col] = 'Q';
                if (placeQueen(row + 1)) return true;
                board[row][col] = '.';
            }
        }
        return false;
    }

    if (!placeQueen(0)) {
        console.log("No solution");
    }
}