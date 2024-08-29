#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to calculate the minimum number of changes needed to make the matrix symmetric
int minChangesToSymmetric(vector<vector<char>>& matrix) {
    int n = matrix.size();
    int minChanges = 0;

    // Traverse only the upper triangle of the matrix, excluding the diagonal
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            // If the corresponding elements are not equal, they need to be changed
            if (matrix[i][j] != matrix[j][i]) {
                ++minChanges;
                // Optionally, you can change matrix[i][j] to matrix[j][i] or vice versa to make it symmetric
                // Uncomment the line below if you want to actually modify the matrix
                // matrix[i][j] = matrix[j][i];
            }
        }
    }

    return minChanges;
}
