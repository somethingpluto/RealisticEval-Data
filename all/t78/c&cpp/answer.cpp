#include <iostream>
#include <cmath> // For sin, cos, and M_PI
#include <Eigen/Dense> // For matrix operations

using Eigen::Matrix3f; // Define a 3x3 float matrix

// Function to convert Euler angles (roll, pitch, yaw) to a rotation matrix
Matrix3f euler_to_rotation_matrix(float roll, float pitch, float yaw) {
    // Convert degrees to radians
    float roll_rad = roll * M_PI / 180.0f;
    float pitch_rad = pitch * M_PI / 180.0f;
    float yaw_rad = yaw * M_PI / 180.0f;

    // Rotation matrix around x-axis (roll)
    Matrix3f Rx;
    Rx << 1, 0, 0,
          0, std::cos(roll_rad), -std::sin(roll_rad),
          0, std::sin(roll_rad), std::cos(roll_rad);

    // Rotation matrix around y-axis (pitch)
    Matrix3f Ry;
    Ry << std::cos(pitch_rad), 0, std::sin(pitch_rad),
          0, 1, 0,
          -std::sin(pitch_rad), 0, std::cos(pitch_rad);

    // Rotation matrix around z-axis (yaw)
    Matrix3f Rz;
    Rz << std::cos(yaw_rad), -std::sin(yaw_rad), 0,
          std::sin(yaw_rad), std::cos(yaw_rad), 0,
          0, 0, 1;

    // Combined rotation matrix, R = Rz * Ry * Rx
    Matrix3f R = Rz * Ry * Rx;

    return R;
}