/**
 * Converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
 * 
 * @param {Array} K - Camera intrinsic matrix (3x3 array)
 * @param {number} d - Depth (distance along z-axis)
 * @param {number} x - Pixel x coordinate
 * @param {number} y - Pixel y coordinate
 * @returns {Array} - x, y, z 3D point coordinates in camera RDF coordinates
 */
function get3DCoordinates(K, d, x, y) {}