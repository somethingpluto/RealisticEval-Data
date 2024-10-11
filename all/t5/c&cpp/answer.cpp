#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> matrix_multiply(const vector<vector<int>>& matrixA, const vector<vector<int>>& matrixB) {
    // Get dimensions
    int rowsA = matrixA.size();
    int colsA = matrixA[0].size();
    int rowsB = matrixB.size();
    int colsB = matrixB[0].size();

    // Check if multiplication is possible
    if (colsA != rowsB) {
        throw invalid_argument("Number of columns in matrixA must equal number of rows in matrixB.");
    }

    // Initialize result matrix with zeroes
    vector<vector<int>> result(rowsA, vector<int>(colsB, 0));

    // Perform matrix multiplication
    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            for (int k = 0; k < colsA; ++k) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    return result;
}
