import { Vector3 } from 'three';

/**
 * Translate the point cloud by a given vector.
 *
 * @param pointCloud - A N x 3 Float32Array representing the 3D point cloud.
 * @param translationVector - A 1 x 3 Float32Array or array representing the translation vector.
 * @returns A N x 3 Float32Array of the translated point cloud.
 */
function translatePointCloud(pointCloud: Float32Array, translationVector: Float32Array | number[]): Float32Array {
    // Convert the translation vector to a Vector3 instance
    const translation = new Vector3(...(translationVector as number[]));

    // Create a new Float32Array to store the translated point cloud
    const translatedPointCloud = new Float32Array(pointCloud.length);

    // Translate each point in the point cloud
    for (let i = 0; i < pointCloud.length; i += 3) {
        translatedPointCloud[i] = pointCloud[i] + translation.x;
        translatedPointCloud[i + 1] = pointCloud[i + 1] + translation.y;
        translatedPointCloud[i + 2] = pointCloud[i + 2] + translation.z;
    }

    return translatedPointCloud;
}
describe('TestTranslatePointCloud', () => {
    /**
     * Test a simple translation of a single point.
     */
    it('testSimpleTranslation', () => {
        const pointCloud = new Float32Array([1.0, 2.0, 3.0]);
        const translationVector = new Float32Array([1.0, 1.0, 1.0]);
        const expectedOutput = new Float32Array([2.0, 3.0, 4.0]);

        const result = translatePointCloud(pointCloud, translationVector);
        expect(result).toEqual(expectedOutput);
    });

    /**
     * Test translation of multiple points.
     */
    it('testMultiplePointsTranslation', () => {
        const pointCloud = new Float32Array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]);
        const translationVector = new Float32Array([1.0, 2.0, 3.0]);
        const expectedOutput = new Float32Array([2.0, 4.0, 6.0, 5.0, 7.0, 9.0]);

        const result = translatePointCloud(pointCloud, translationVector);
        expect(result).toEqual(expectedOutput);
    });

    /**
     * Test translation by a zero vector (should return the same point cloud).
     */
    it('testZeroTranslation', () => {
        const pointCloud = new Float32Array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]);
        const translationVector = new Float32Array([0.0, 0.0, 0.0]);
        const expectedOutput = new Float32Array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]);

        const result = translatePointCloud(pointCloud, translationVector);
        expect(result).toEqual(expectedOutput);
    });

    /**
     * Test translation with negative values.
     */
    it('testNegativeTranslation', () => {
        const pointCloud = new Float32Array([1.0, 2.0, 3.0]);
        const translationVector = new Float32Array([-1.0, -2.0, -3.0]);
        const expectedOutput = new Float32Array([0.0, 0.0, 0.0]);

        const result = translatePointCloud(pointCloud, translationVector);
        expect(result).toEqual(expectedOutput);
    });
});

