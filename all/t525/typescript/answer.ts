import * as tf from '@tensorflow/tfjs';

function flipPointCloud(pointCloud: tf.Tensor, axis: number): tf.Tensor {
    /**
     * Flip the point cloud across a specified axis.
     *
     * Parameters:
     * - pointCloud: A N x 3 tensor representing the 3D point cloud.
     * - axis: An integer specifying the axis to flip (0 for x, 1 for y, 2 for z).
     *
     * Returns:
     * - A N x 3 tensor of the flipped point cloud.
     */

    // Validate the axis input
    if (axis < 0 || axis > 2) {
        throw new Error("Axis must be 0 (x-axis), 1 (y-axis), or 2 (z-axis).");
    }

    // Create a scaling factor array with -1 for the specified axis and 1 for others
    const flipFactors = tf.tensor1d([1, 1, 1]);
    flipFactors.set(-1, axis);

    // Flip the point cloud by multiplying with the scaling factor array
    const flippedPointCloud = pointCloud.mul(flipFactors);

    return flippedPointCloud;
}