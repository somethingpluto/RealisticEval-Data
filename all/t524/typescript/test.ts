describe('TestScalePointCloud', () => {
    it('test simple scaling', () => {
        const pointCloud = Matrix([[1.0, 2.0, 3.0]]);
        const scaleFactor = 2.0;
        const expectedOutput = Matrix([[2.0, 4.0, 6.0]]);
        expect(scalePointCloud(pointCloud, scaleFactor)).toEqual(expectedOutput);
    });

    it('test multiple points scaling', () => {
        const pointCloud = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]);
        const scaleFactor = 0.5;
        const expectedOutput = Matrix([[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]);
        expect(scalePointCloud(pointCloud, scaleFactor)).toEqual(expectedOutput);
    });

    it('test zero scaling', () => {
        const pointCloud = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]);
        const scaleFactor = 0.0;
        const expectedOutput = Matrix([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]);
        expect(scalePointCloud(pointCloud, scaleFactor)).toEqual(expectedOutput);
    });

    it('test negative scaling', () => {
        const pointCloud = Matrix([[1.0, 2.0, 3.0]]);
        const scaleFactor = -2.0;
        const expectedOutput = Matrix([[-2.0, -4.0, -6.0]]);
        expect(scalePointCloud(pointCloud, scaleFactor)).toEqual(expectedOutput);
    });
});