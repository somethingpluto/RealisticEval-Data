/**
 * Converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
 * @param {number[][]} K - Camera intrinsic matrix of size 3x3.
 * @param {number} d - Depth (distance along z-axis).
 * @param {number} x - Pixel x-coordinate.
 * @param {number} y - Pixel y-coordinate.
 * @returns {number[]} - The 3D point coordinates [x, y, z] in camera RDF coordinates.
 */
function get3DCoordinates(K: number[][], d: number, x: number, y: number): number[] {}