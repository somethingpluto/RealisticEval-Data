/**
 * Converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
 *
 * @param K   The camera intrinsic matrix (3x3).
 * @param d   The depth (distance along z-axis).
 * @param x   The pixel x coordinate.
 * @param y   The pixel y coordinate.
 * @return A RealVector representing the x, y, z 3D point coordinates in camera RDF coordinates.
 */
public static RealVector get3DCoordinates(RealMatrix K, double d, double x, double y) {}