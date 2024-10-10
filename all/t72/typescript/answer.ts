interface Matrix {
    [index: number]: number[];
}

function get3DCoordinates(K: Matrix, d: number, x: number, y: number): number[] {
    /**
     * Converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
     * @param K - Camera intrinsic matrix (3x3).
     * @param d - Depth (distance along z-axis).
     * @param x - Pixel x-coordinate.
     * @param y - Pixel y-coordinate.
     * @returns 3D point coordinates in camera RDF coordinates.
     */

    // Extracting elements from the camera intrinsic matrix K
    const fx = K[0][0];
    const fy = K[1][1];
    const cx = K[0][2];
    const cy = K[1][2];

    // Calculating 3D coordinates
    const X = (x - cx) * d / fx;
    const Y = (y - cy) * d / fy;
    const Z = d;

    return [X, Y, Z];
}