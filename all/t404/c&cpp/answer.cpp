#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

vector<vector<int>> multiply_matrices(const vector<vector<int>>& A, const vector<vector<int>>& B) {
    int rowsA = A.size();
    int colsA = A[0].size();
    int colsB = B[0].size();

    vector<vector<int>> result(rowsA, vector<int>(colsB, 0));

    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            for (int k = 0; k < colsA; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}

vector<vector<int>> power(const vector<vector<int>>& matrix, int n) {
    if (n < 0) {
        throw invalid_argument("The exponent n must be a non-negative integer.");
    }

    int size = matrix.size();
    vector<vector<int>> result(size, vector<int>(size, 0));

    // Initialize identity matrix
    for (int i = 0; i < size; ++i) {
        result[i][i] = 1;
    }

    vector<vector<int>> base = matrix;

    while (n > 0) {
        if (n % 2 == 1) {
            result = multiply_matrices(result, base);
        }
        base = multiply_matrices(base, base);
        n /= 2;
    }

    return result;
}