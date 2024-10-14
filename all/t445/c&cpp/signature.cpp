#include <Eigen/Dense>
#include <string>

/**
 * @brief Create a pose matrix representing a rotation about a given axis.
 *
 * @param angle_deg Rotation angle in degrees.
 * @param axis Axis to rotate about, must be one of 'X', 'Y', or 'Z'.
 * @return Eigen::Matrix4d 4x4 pose matrix representing the rotation.
 */
Eigen::Matrix4d create_rot_matrix(double angle_deg, const std::string& axis);