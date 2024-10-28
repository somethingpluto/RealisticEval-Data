/**
 * Generates integer coordinates on the line from (x1, y1) to (x2, y2) using Bresenham's line algorithm.
 *
 * Bresenham's algorithm calculates the points of an approximately straight line between two given points on a grid.
 * It is particularly well-suited for computer graphics where an efficient, integer-based algorithm is needed to
 * determine which points should be rasterized to represent the line.
 *
 * @param {number} x1 - The x-coordinate of the starting point of the line.
 * @param {number} y1 - The y-coordinate of the starting point of the line.
 * @param {number} x2 - The x-coordinate of the ending point of the line.
 * @param {number} y2 - The y-coordinate of the ending point of the line.
 * @returns {Array.<Array.<number>>} An array where each sub-array contains the x and y coordinates of a point on the line.
 */
function bresenhamLine(x1, y1, x2, y2) {}