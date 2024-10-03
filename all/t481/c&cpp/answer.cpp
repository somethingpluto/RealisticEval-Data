#include <iostream>
#include <vector>

using namespace std;

void printBoard(const vector<vector<char>>& board) {
    const int boardSize = 3; // Size of the board
    cout << "-------------" << endl;

    // Loop through each row
    for (int i = 0; i < boardSize; i++) {
        cout << "| "; // Start of the row

        // Loop through each column in the row
        for (int j = 0; j < boardSize; j++) {
            cout << board[i][j] << " | "; // Print each cell
        }

        cout << endl; // End of the row
        cout << "-------------" << endl; // Print the row separator
    }
}
