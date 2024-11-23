import { Float32Array } from "typed-array";

/**
 * Translate the point cloud by a given vector.
 *
 * @param pointCloud - A N x 3 Float32Array representing the 3D point cloud.
 * @param translationVector - A 1 x 3 Float32Array or array representing the translation vector.
 * @returns A N x 3 Float32Array of the translated point cloud.
 */
function translatePointCloud(pointCloud: Float32Array, translationVector: Float32Array | number[]): Float32Array {
    // Ensure the translationVector is a Float32Array for broadcasting
    const translationVectorTyped = new Float32Array(translationVector);

    // Check if translationVector is of correct shape
    if (translationVectorTyped.length !== 3) {
        throw new Error("translationVector must be a 1D array of length 3");
    }

    // Calculate the number of points in the point cloud
    const numPoints = pointCloud.length / 3;

    // Create a new Float32Array for the translated point cloud
    const translatedPointCloud = new Float32Array(pointCloud.length);

    // Translate the point cloud by adding the translation vector to each point
    for (let i = 0; i < numPoints; i++) {
        const index = i * 3;
        translatedPointCloud[index] = pointCloud[index] + translationVectorTyped[0];
        translatedPointCloud[index + 1] = pointCloud[index + 1] + translationVectorTyped[1];
        translatedPointCloud[index + 2] = pointCloud[index + 2] + translationVectorTyped[2];
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

