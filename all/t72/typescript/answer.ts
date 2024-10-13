import * as math from 'mathjs';

interface CameraIntrinsicMatrix {
    0: number;
    1: number;
    2: number;
    3: number;
    4: number;
    5: number;
    6: number;
    7: number;
    8: number;
}

function get3DCoordinates(K: CameraIntrinsicMatrix, d: number, x: number, y: number): [number, number, number] {
    // Step 1: Convert pixel coordinates to normalized device coordinates (NDC)
    const cx = K[0 * 3 + 2];
    const cy = K[1 * 3 + 2];
    const fx = K[0 * 3 + 0];
    const fy = K[1 * 3 + 1];

    const NDC_x = (x - cx) / fx;
    const NDC_y = (y - cy) / fy;

    // Step 2: Get the 3D world coordinates (W)
    const W_x = NDC_x * d;
    const W_y = NDC_y * d;
    const W_z = d;

    return [W_x, W_y, W_z];
}