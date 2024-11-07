/**
 * Flip the point cloud across a specified axis.
 *
 * @param {Array<Array<number>>} pointCloud - A N x 3 array representing the 3D point cloud.
 * @param {number} axis - An integer specifying the axis to flip (0 for x, 1 for y, 2 for z).
 * @returns {Array<Array<number>>} - A N x 3 array of the flipped point cloud.
 */
function flipPointCloud(pointCloud: Array<[number, number, number]>, axis: number): Array<[number, number, number]> {
    // Validate the axis input
    if (axis !== 0 && axis !== 1 && axis !== 2) {
        throw new Error("Axis must be 0 (x-axis), 1 (y-axis), or 2 (z-axis).");
    }

    // Create a scaling factor array with -1 for the specified axis and 1 for others
    const flipFactors: [number, number, number] = [1, 1, 1];
    flipFactors[axis] = -1;

    // Flip the point cloud by multiplying with the scaling factor array
    const flippedPointCloud = pointCloud.map(row => {
        return row.map((value, index) => value * flipFactors[index]);
    });

    return flippedPointCloud;
}
