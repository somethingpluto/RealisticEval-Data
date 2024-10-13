/**
 * Converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
 * 
 * @param K - A 3x3 camera intrinsic matrix.
 * @param d - Depth (distance along the z-axis).
 * @param x - Pixel x coordinate.
 * @param y - Pixel y coordinate.
 * @returns A tuple representing the x, y, z 3D point coordinates in camera RDF coordinates.
 */
function get3DCoordinates(K: number[][], d: number, x: number, y: number): [number, number, number] {}