#include <Eigen/Dense>
#include <cmath>

// Function to rotate a point cloud around the Y-axis by a given angle
Eigen::MatrixXd rotatePointCloud(const Eigen::MatrixXd& pointCloud, double rotationAngle) {
    /**
     * Rotate the point cloud around the Y axis by a given angle.
     *
     * Parameters:
     * - pointCloud: An N x 3 Eigen matrix representing the 3D point cloud.
     * - rotationAngle: The angle (in radians) to rotate the point cloud.
     *
     * Returns:
     * - An N x 3 Eigen matrix of the rotated point cloud.
     */

    // Create the rotation matrix for a rotation around the Y axis
    Eigen::Matrix3d rotationMatrix;
    rotationMatrix << cos(rotationAngle), 0, sin(rotationAngle),
                      0, 1, 0,
                     -sin(rotationAngle), 0, cos(rotationAngle);

    // Rotate the point cloud by multiplying with the rotation matrix
    Eigen::MatrixXd rotatedPointCloud = pointCloud * rotationMatrix;

    return rotatedPointCloud;
}