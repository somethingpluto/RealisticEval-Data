#include <iostream>
#include <vector>

using namespace std;

typedef pair<double, double> ScaleFactors;
typedef vector<vector<double>> Matrix;

ScaleFactors get_scale(const Matrix& matrix) {
    if (matrix.size() != 3 || matrix[0].size() != 3 || matrix[1].size() != 3 || matrix[2].size() != 3) {
        throw invalid_argument("Matrix must be 3x3");
    }

    double scale_x = sqrt(pow(matrix[0][0], 2) + pow(matrix[1][0], 2));
    double scale_y = sqrt(pow(matrix[0][1], 2) + pow(matrix[1][1], 2));

    return make_pair(scale_x, scale_y);
}
