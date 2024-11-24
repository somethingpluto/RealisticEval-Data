function rotatePointCloud(pointCloud, rotationAngle) {
    /**
     * Rotate the point cloud around the Y axis by a given angle.
     *
     * @param {Array} pointCloud - A N x 3 array representing the 3D point cloud.
     * @param {number} rotationAngle - The angle (in radians) to rotate the point cloud.
     * @returns {Array} - A N x 3 array of the rotated point cloud.
     */

    // Create the rotation matrix for a rotation around the Y axis
    const rotationMatrix = [
        [Math.cos(rotationAngle), 0, Math.sin(rotationAngle)],
        [0, 1, 0],
        [-Math.sin(rotationAngle), 0, Math.cos(rotationAngle)]
    ];

    // Rotate the point cloud
    const rotatedPointCloud = pointCloud.map(point => {
        const x = point[0];
        const y = point[1];
        const z = point[2];

        // Perform matrix multiplication for each point (x, y, z)
        const rotatedX = rotationMatrix[0][0] * x + rotationMatrix[0][2] * z;
        const rotatedY = y; // Y remains unchanged
        const rotatedZ = rotationMatrix[2][0] * x + rotationMatrix[2][2] * z;

        return [rotatedX, rotatedY, rotatedZ];
    });

    return rotatedPointCloud;
}
