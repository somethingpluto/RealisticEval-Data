/**
 * Converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
 *
 * @param K A 3x3 matrix representing the camera intrinsic matrix.
 * @param d Depth (distance along the z-axis).
 * @param x Pixel x coordinate.
 * @param y Pixel y coordinate.
 *
 * @return A 3D vector containing the x, y, z coordinates in camera RDF coordinates.
 */
VectorXd get_3d_coordinates(const MatrixXd& K, double d, double x, double y) {}