describe('TestGetScaleFunction', () => {
    it('test_identity_matrix', () => {
        // Test for the identity matrix (no scaling)
        const matrix: number[][] = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ];
        const expectedScale: [number, number] = [1.0, 1.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });

    it('test_scaling_matrix', () => {
        // Test for a scaling matrix (2x in x and 3x in y)
        const matrix: number[][] = [
            [2, 0, 0],
            [0, 3, 0],
            [0, 0, 1]
        ];
        const expectedScale: [number, number] = [2.0, 3.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });

    it('test_uniform_scaling', () => {
        // Test case with uniform scaling
        const matrix: number[][] = [
            [2, 0, 0],
            [0, 2, 0],
            [0, 0, 1]
        ];
        const expectedScale: [number, number] = [2.0, 2.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });

    it('test_non_uniform_scaling', () => {
        // Test case with non-uniform scaling
        const matrix: number[][] = [
            [3, 0, 0],
            [0, 5, 0],
            [0, 0, 1]
        ];
        const expectedScale: [number, number] = [3.0, 5.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });

    it('test_reflection_matrix', () => {
        // Test case with reflection matrix
        const matrix: number[][] = [
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ];
        const expectedScale: [number, number] = [1.0, 1.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });
});
