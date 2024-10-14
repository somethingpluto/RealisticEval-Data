#include <Eigen/Dense>
#include <iostream>

using namespace Eigen;
using namespace std;

MatrixXd applyShearX(const MatrixXd &matrix, double shearFactor) {
    // Create an identity matrix of the same size as input matrix
    MatrixXd shearMatrix = MatrixXd::Identity(matrix.rows(), matrix.cols());

    // Set the value for shear transformation on the top right corner
    shearMatrix(1,0) = shearFactor;

    // Perform matrix multiplication to apply shear transformation
    return shearMatrix * matrix;
}

int main() {
    MatrixXd m(3,3);
    m << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;

    double sf = 0.5;  // Shear factor

    MatrixXd result = applyShearX(m, sf);

    cout << "Original matrix:\n" << m << "\n\n";
    cout << "Sheared matrix:\n" << result << endl;

    return 0;
}