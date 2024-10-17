import { Matrix } from 'mathjs';

/**
 * Scale the point cloud by a given factor.
 *
 * @param pointCloud - A N x 3 matrix representing the 3D point cloud.
 * @param scaleFactor - A number representing the scaling factor.
 * @returns A N x 3 matrix of the scaled point cloud.
 */
function scalePointCloud(pointCloud: Matrix, scaleFactor: number): Matrix {
    // Ensure pointCloud is a matrix
    pointCloud = Matrix(pointCloud);

    // Validate input shape
    const shape = pointCloud.size();
    if (shape.length !== 2 || shape[1] !== 3) {
        throw new Error('pointCloud must be a 2D array with shape (N, 3)');
    }

    // Scale the point cloud by the given factor
    const scaledPointCloud = pointCloud.multiply(scaleFactor);

    return scaledPointCloud;
}