#include <vector>
#include <iostream>

std::vector<int> spiral_order(const std::vector<std::vector<int>>& matrix) {
    std::vector<int> result;
    if (matrix.empty() || matrix[0].empty()) {
        return result;
    }

    int rows = matrix.size();
    int cols = matrix[0].size();
    int top = 0, bottom = rows - 1, left = 0, right = cols - 1;

    while (top <= bottom && left <= right) {
        // Traverse from left to right along the top row
        for (int i = left; i <= right; ++i) {
            result.push_back(matrix[top][i]);
        }
        top++;

        // Traverse downwards along the right column
        for (int i = top; i <= bottom; ++i) {
            result.push_back(matrix[i][right]);
        }
        right--;

        // Traverse from right to left along the bottom row, if still within bounds
        if (top <= bottom) {
            for (int i = right; i >= left; --i) {
                result.push_back(matrix[bottom][i]);
            }
            bottom--;
        }

        // Traverse upwards along the left column, if still within bounds
        if (left <= right) {
            for (int i = bottom; i >= top; --i) {
                result.push_back(matrix[i][left]);
            }
            left++;
        }
    }

    return result;
}
