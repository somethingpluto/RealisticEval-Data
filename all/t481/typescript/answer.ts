function printBoard(board: string[][]): void {
    const boardSize = 3; // Size of the board
    console.log("-------------");

    // Loop through each row
    for (let i = 0; i < boardSize; i++) {
        process.stdout.write("| "); // Start of the row

        // Loop through each column in the row
        for (let j = 0; j < boardSize; j++) {
            process.stdout.write(board[i][j] + " | "); // Print each cell
        }

        console.log(); // End of the row
        console.log("-------------"); // Print the row separator
    }
}