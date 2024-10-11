function eightQueens(): void {
    const N: number = 8;
    let board: string[][] = Array.from({ length: N }, () => Array(N).fill('.'));

    function isSafe(row: number, col: number): boolean {
        for (let i = 0; i < col; i++) {
            if (board[row][i] === 'Q') return false;
        }

        for (let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') return false;
        }

        for (let i = row, j = col; i < N && j >= 0; i++, j--) {
            if (board[i][j] === 'Q') return false;
        }

        return true;
    }

    function solveNQueens(col: number): boolean {
        if (col >= N) {
            console.log(printBoard(board));
            return true;
        }

        for (let i = 0; i < N; i++) {
            if (isSafe(i, col)) {
                board[i][col] = 'Q';
                if (solveNQueens(col + 1)) {
                    return true;
                }
                board[i][col] = '.';
            }
        }

        return false;
    }

    function printBoard(board: string[][]): string {
        return board.map(row => row.join(' ')).join('\n');
    }

    if (!solveNQueens(0)) {
        console.log("No solution");
    }
}