import * as math from 'mathjs';

/**
 * Rotate the point cloud around the Y axis by a given angle.
 *
 * @param pointCloud - An Nx3 matrix representing the 3D point cloud.
 * @param rotationAngle - The angle (in radians) to rotate the point cloud.
 * @returns An Nx3 matrix of the rotated point cloud.
 */
function rotatePointCloud(pointCloud: number[][], rotationAngle: number): number[][] {
    // Create the rotation matrix for a rotation around the Y axis
    const rotationMatrix = math.matrix([
        [math.cos(rotationAngle), 0, math.sin(rotationAngle)],
        [0, 1, 0],
        [-math.sin(rotationAngle), 0, math.cos(rotationAngle)]
    ]);

    // Rotate the point cloud by multiplying with the rotation matrix
    const rotatedPointCloud = pointCloud.map(row => {
        const rowMatrix = math.matrix(row);
        const rotatedRow = math.multiply(rowMatrix, rotationMatrix);
        return math.toArray(rotatedRow) as number[];
    });

    return rotatedPointCloud;
}
