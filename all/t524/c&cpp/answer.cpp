#include <iostream>
#include <Eigen/Dense>
#include <stdexcept>

// Function to scale a point cloud by a given factor
Eigen::MatrixXd scalePointCloud(const Eigen::MatrixXd& pointCloud, double scaleFactor) {
    // Validate input shape
    if (pointCloud.cols() != 3) {
        throw std::invalid_argument("pointCloud must be a 2D array with shape (N, 3)");
    }

    // Scale the point cloud by the given factor
    Eigen::MatrixXd scaledPointCloud = pointCloud * scaleFactor;

    return scaledPointCloud;
}
