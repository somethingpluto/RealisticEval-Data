describe('TestScalePointCloud', () => {
    describe('test_simple_scaling', () => {
        it('should scale a single point correctly', () => {
            const pointCloud = [[1.0, 2.0, 3.0]];
            const scaleFactor = 2.0;
            const expectedOutput = [[2.0, 4.0, 6.0]];
            expect(scalePointCloud(pointCloud, scaleFactor)).toEqual(expectedOutput);
        });
    });

    describe('test_multiple_points_scaling', () => {
        it('should scale multiple points correctly', () => {
            const pointCloud = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
            const scaleFactor = 0.5;
            const expectedOutput = [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]];
            expect(scalePointCloud(pointCloud, scaleFactor)).toEqual(expectedOutput);
        });
    });

    describe('test_zero_scaling', () => {
        it('should scale by a factor of zero', () => {
            const pointCloud = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
            const scaleFactor = 0.0;
            const expectedOutput = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]];
            expect(scalePointCloud(pointCloud, scaleFactor)).toEqual(expectedOutput);
        });
    });

    describe('test_negative_scaling', () => {
        it('should scale with a negative factor', () => {
            const pointCloud = [[1.0, 2.0, 3.0]];
            const scaleFactor = -2.0;
            const expectedOutput = [[-2.0, -4.0, -6.0]];
            expect(scalePointCloud(pointCloud, scaleFactor)).toEqual(expectedOutput);
        });
    });
});