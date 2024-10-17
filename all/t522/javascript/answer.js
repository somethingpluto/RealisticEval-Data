const math = require('mathjs');

function rotatePointCloud(pointCloud, rotationAngle) {
    /**
     * Rotate the point cloud around the Y axis by a given angle.
     *
     * Parameters:
     * - pointCloud: A N x 3 array representing the 3D point cloud.
     * - rotationAngle: The angle (in radians) to rotate the point cloud.
     *
     * Returns:
     * - A N x 3 array of the rotated point cloud.
     */

    // Create the rotation matrix for a rotation around the Y axis
    const rotationMatrix = math.matrix([
        [math.cos(rotationAngle), 0, math.sin(rotationAngle)],
        [0, 1, 0],
        [-math.sin(rotationAngle), 0, math.cos(rotationAngle)]
    ]);

    // Rotate the point cloud by multiplying with the rotation matrix
    const rotatedPointCloud = math.multiply(pointCloud, rotationMatrix);

    return rotatedPointCloud;
}
