#include <Eigen/Dense>
#include <stdexcept>

// Function to translate a point cloud by a given vector using Eigen library
Eigen::MatrixXd translatePointCloud(const Eigen::MatrixXd& pointCloud, const Eigen::RowVector3d& translationVector) {
    /**
     * Translate the point cloud by a given vector.
     *
     * Parameters:
     * - pointCloud: An M x 3 Eigen matrix representing the 3D point cloud.
     * - translationVector: A 1 x 3 Eigen row vector representing the translation vector.
     *
     * Returns:
     * - An M x 3 Eigen matrix of the translated point cloud.
     */

    // Check if translationVector is of correct shape
    if (translationVector.size() != 3) {
        throw std::invalid_argument("translationVector must be a 1D array of shape (3,)");
    }

    // Translate the point cloud by adding the translation vector to each point
    Eigen::MatrixXd translatedPointCloud = pointCloud;
    translatedPointCloud.rowwise() += translationVector;

    return translatedPointCloud;
}
