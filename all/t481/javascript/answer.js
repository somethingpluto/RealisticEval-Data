function printBoard(board) {
    const boardSize = 3; // Size of the board
    console.log("-------------");

    // Loop through each row
    for (let i = 0; i < boardSize; i++) {
        let row = "| "; // Start of the row

        // Loop through each column in the row
        for (let j = 0; j < boardSize; j++) {
            row += board[i][j] + " | "; // Append each cell
        }

        console.log(row); // Print the row
        console.log("-------------"); // Print the row separator
    }
}