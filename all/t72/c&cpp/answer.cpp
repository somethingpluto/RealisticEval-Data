#include <iostream>
#include <Eigen/Dense>

using Eigen::MatrixXd;
using Eigen::VectorXd;

VectorXd get_3d_coordinates(const MatrixXd& K, double d, double x, double y) {
    // Step 1: Convert pixel coordinates to normalized device coordinates (NDC)
    double cx = K(0, 2);
    double cy = K(1, 2);
    double fx = K(0, 0);
    double fy = K(1, 1);

    double NDC_x = (x - cx) / fx;
    double NDC_y = (y - cy) / fy;

    // Step 2: Get the 3D world coordinates (W)
    double W_x = NDC_x * d;
    double W_y = NDC_y * d;
    double W_z = d;

    return VectorXd::Map(&W_x, 3);  // Map the array to a VectorXd
}

int main() {
    // Example usage
    MatrixXd K(3, 3);
    K << 500, 0, 320,
         0, 500, 240,
         0, 0, 1;

    double d = 10.0;
    double x = 350.0;
    double y = 200.0;

    VectorXd result = get_3d_coordinates(K, d, x, y);

    std::cout << "3D Coordinates: " << result.transpose() << std::endl;

    return 0;
}