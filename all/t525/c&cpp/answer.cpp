#include <iostream>
#include <Eigen/Dense>

using Eigen::MatrixXd;

// Function to flip the point cloud across a specified axis
MatrixXd flipPointCloud(const MatrixXd& pointCloud, int axis) {
    // Validate the axis input
    if (axis < 0 || axis > 2) {
        throw std::invalid_argument("Axis must be 0 (x-axis), 1 (y-axis), or 2 (z-axis).");
    }

    // Create a scaling factor vector with -1 for the specified axis and 1 for others
    VectorXd flipFactors(3);
    flipFactors << (axis != 0 ? 1 : -1), (axis != 1 ? 1 : -1), (axis != 2 ? 1 : -1);

    // Flip the point cloud by multiplying with the scaling factor vector
    MatrixXd flippedPointCloud = pointCloud.unaryExpr([flipFactors](double val, int row, int col) {
        return val * flipFactors(col);
    });

    return flippedPointCloud;
}
