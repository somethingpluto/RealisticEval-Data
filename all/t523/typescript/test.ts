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
