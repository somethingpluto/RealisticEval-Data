describe('TestEulerToRotationMatrix', () => {
    it('test_zero_rotation', () => {
        // Test with zero rotation for all axes
        const R = eulerToRotationMatrix(0, 0, 0);
        expect(R).toEqual([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]);
    });

    it('test_rotation_about_x', () => {
        // Test rotation about the x-axis
        const R = eulerToRotationMatrix(90, 0, 0);
        const expected = [
            [1, 0, 0],
            [0, 0, -1],
            [0, 1, 0]
        ];
        expect(R).toEqual(expected);
    });

    it('test_rotation_about_y', () => {
        // Test rotation about the y-axis
        const R = eulerToRotationMatrix(0, 90, 0);
        const expected = [
            [0, 0, 1],
            [0, 1, 0],
            [-1, 0, 0]
        ];
        expect(R).toEqual(expected);
    });

    it('test_rotation_about_z', () => {
        // Test rotation about the z-axis
        const R = eulerToRotationMatrix(0, 0, 90);
        const expected = [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ];
        expect(R).toEqual(expected);
    });

    it('test_combined_rotation', () => {
        // Test combined rotation
        const R = eulerToRotationMatrix(30, 45, 60);
        const expected = [
            [0.35355339, -0.5732233, 0.73919892],
            [0.61237244, 0.73919892, 0.28033009],
            [-0.70710678, 0.35355339, 0.61237244]
        ];
        expect(R).toEqual(expected);
    });
});
