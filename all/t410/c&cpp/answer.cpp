#include <iostream>
#include <Eigen/Dense>

bool check_xor_sum(const Eigen::MatrixXd &combination) {
    // Assuming that the required XOR sum values are stored in a vector or array,
    // and you have defined them before calling this function.
    std::vector<int> requiredXorSum = { /* ... */ };

    // Get the number of rows and columns in the combination matrix
    int numRows = combination.rows();
    int numCols = combination.cols();

    // Iterate over each column in the combination matrix
    for(int col = 0; col < numCols; ++col) {
        int xorSum = 0;
        
        // Calculate the XOR sum of the current column
        for(int row = 0; row < numRows; ++row) {
            xorSum ^= combination(row, col);
        }

        // Check if the calculated XOR sum matches the required XOR sum
        if(xorSum != requiredXorSum[col]) {
            return false;
        }
    }

    // If all columns pass the XOR sum check, return true
    return true;
}