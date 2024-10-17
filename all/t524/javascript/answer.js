function scalePointCloud(pointCloud, scaleFactor) {
    /**
     * Scale the point cloud by a given factor.
     *
     * Parameters:
     * - pointCloud: A 2D array representing the 3D point cloud with shape [N, 3].
     * - scaleFactor: A number representing the scaling factor.
     *
     * Returns:
     * - A 2D array of the scaled point cloud with shape [N, 3].
     */

    // Ensure pointCloud is an array
    if (!Array.isArray(pointCloud)) {
        throw new TypeError('pointCloud must be an array');
    }

    // Validate input shape
    if (!Array.isArray(pointCloud[0]) || pointCloud[0].length !== 3) {
        throw new Error('pointCloud must be a 2D array with shape [N, 3]');
    }

    // Scale the point cloud by the given factor
    const scaledPointCloud = pointCloud.map(row => {
        return row.map(value => value * scaleFactor);
    });

    return scaledPointCloud;
}