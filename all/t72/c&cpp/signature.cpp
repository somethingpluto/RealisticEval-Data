/**
 * Converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
 *
 * @param K A 3x3 Eigen::Matrix representing the camera intrinsic matrix.
 * @param d The depth (distance along the z-axis).
 * @param x The pixel x-coordinate.
 * @param y The pixel y-coordinate.
 * @return An Eigen::Vector3d representing the x, y, z 3D point coordinates in camera RDF coordinates.
 */
Eigen::Vector3d get_3d_coordinates(const Eigen::Matrix3d& K, double d, double x, double y) {}