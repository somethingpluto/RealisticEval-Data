#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

vector<vector<int>> matrix_multiply(const vector<vector<int>>& matrixA, const vector<vector<int>>& matrixB) {
    // Check if either matrixA or matrixB or their first row is empty
    if (matrixA.empty() || matrixB.empty() || matrixA[0].empty() || matrixB[0].empty()) {
        return {};
    }
    
    // Ensure matrix dimensions are compatible for multiplication
    if (matrixA[0].size() != matrixB.size()) {
        throw invalid_argument("The number of columns in the first matrix must be equal to the number of rows in the second matrix.");
    }
    
    // Initialize the result matrix with zeros
    vector<vector<int>> result(matrixA.size(), vector<int>(matrixB[0].size(), 0));

    // Perform matrix multiplication
    for (size_t i = 0; i < matrixA.size(); ++i) {
        for (size_t j = 0; j < matrixB[0].size(); ++j) {
            for (size_t k = 0; k < matrixB.size(); ++k) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    return result;
}

int main() {
    // Example usage
    vector<vector<int>> matrixA = {{1, 2, 3}, {4, 5, 6}};
    vector<vector<int>> matrixB = {{7, 8}, {9, 10}, {11, 12}};
    
    try {
        vector<vector<int>> result = matrix_multiply(matrixA, matrixB);
        
        for (const auto& row : result) {
            for (int val : row) {
                cout << val << " ";
            }
            cout << endl;
        }
    }
    catch (const exception& e) {
        cerr << e.what() << endl;
    }

    return 0;
}