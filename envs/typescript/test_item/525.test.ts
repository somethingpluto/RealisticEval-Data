import * as tf from '@tensorflow/tfjs';

/**
 * Flip the point cloud across a specified axis.
 *
 * @param pointCloud - A N x 3 tensor representing the 3D point cloud.
 * @param axis - An integer specifying the axis to flip (0 for x, 1 for y, 2 for z).
 * @returns A N x 3 tensor of the flipped point cloud.
 */
function flipPointCloud(pointCloud: tf.Tensor, axis: number): tf.Tensor {
    if (axis < 0 || axis > 2) {
        throw new Error('Invalid axis. It should be 0, 1, or 2.');
    }

    const flipAxis = [0, 1, 2].filter(a => a !== axis);
    const flippedPointCloud = pointCloud.transpose(flipAxis, axis);

    return flippedPointCloud;
}
describe('TestFlipPointCloud', () => {
    it('test_flip_x_axis', () => {
        /** Test flipping the point cloud across the x-axis. */
        const pointCloud = tf.tensor2d([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]);
        const expectedOutput = tf.tensor2d([[1.0, -2.0, 3.0], [4.0, -5.0, 6.0]]);
        const flippedPointCloud = flipPointCloud(pointCloud, 1);
        expect(flippedPointCloud).toEqual(expectedOutput);
    });

    it('test_flip_y_axis', () => {
        /** Test flipping the point cloud across the y-axis. */
        const pointCloud = tf.tensor2d([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]);
        const expectedOutput = tf.tensor2d([[-1.0, 2.0, 3.0], [-4.0, 5.0, 6.0]]);
        const flippedPointCloud = flipPointCloud(pointCloud, 0);
        expect(flippedPointCloud).toEqual(expectedOutput);
    });

    it('test_flip_z_axis', () => {
        /** Test flipping the point cloud across the z-axis. */
        const pointCloud = tf.tensor2d([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]);
        const expectedOutput = tf.tensor2d([[1.0, 2.0, -3.0], [4.0, 5.0, -6.0]]);
        const flippedPointCloud = flipPointCloud(pointCloud, 2);
        expect(flippedPointCloud).toEqual(expectedOutput);
    });

    it('test_invalid_axis', () => {
        /** Test handling of an invalid axis. */
        const pointCloud = tf.tensor2d([[1.0, 2.0, 3.0]]);
        expect(() => flipPointCloud(pointCloud, 3)).toThrowError(/Axis must be 0 \(x-axis\), 1 \(y-axis\), or 2 \(z-axis\)/);
    });

    it('test_empty_point_cloud', () => {
        /** Test flipping an empty point cloud. */
        const pointCloud = tf.tensor2d([], [0, 3]); // Empty point cloud with shape (0, 3)
        const expectedOutput = tf.tensor2d([], [0, 3]); // Expect the output to be the same
        const flippedPointCloud = flipPointCloud(pointCloud, 0);
        expect(flippedPointCloud).toEqual(expectedOutput);
    });
});
