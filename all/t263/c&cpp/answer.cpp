#include <vector>
using namespace std;

class MatrixTraversal {
public:
    vector<int> spiralTraver(vector<vector<int>>& matrix) {
        vector<int> result;
        int top = 0, bottom = matrix.size() - 1, left = 0, right = matrix[0].size() - 1;

        while (top <= bottom && left <= right) {
            // traverse from left to right along the top row
            for (int i = left; i <= right; ++i)
                result.push_back(matrix[top][i]);
            ++top;

            // traverse downwards along the right column
            for (int i = top; i <= bottom; ++i)
                result.push_back(matrix[i][right]);
            --right;

            if (top <= bottom) {
                // traverse from right to left along the bottom row
                for (int i = right; i >= left; --i)
                    result.push_back(matrix[bottom][i]);
                --bottom;
            }

            if (left <= right) {
                // traverse upwards along the left column
                for (int i = bottom; i >= top; --i)
                    result.push_back(matrix[i][left]);
                ++left;
            }
        }

        return result;
    }
};