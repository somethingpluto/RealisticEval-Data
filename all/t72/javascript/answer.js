function get3DCoordinates(K, d, x, y) {
    /**
     * Converts pixel coordinates to 3D coordinates in camera RDF coordinates.
     *
     * @param {Array} K - Camera intrinsic matrix (3x3 array)
     * @param {number} d - Depth (distance along z-axis)
     * @param {number} x - Pixel x coordinate
     * @param {number} y - Pixel y coordinate
     * @returns {Array} - x, y, z 3D point coordinates in camera RDF coordinates
     */

    // Step 1: Convert pixel coordinates to normalized device coordinates (NDC)
    const cx = K[0][2];
    const cy = K[1][2];
    const fx = K[0][0];
    const fy = K[1][1];

    const NDC_x = (x - cx) / fx;
    const NDC_y = (y - cy) / fy;

    // Step 2: Get the 3D world coordinates (W)
    const W_x = NDC_x * d;
    const W_y = NDC_y * d;
    const W_z = d;

    return [W_x, W_y, W_z];
}