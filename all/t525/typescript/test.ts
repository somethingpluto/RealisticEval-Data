describe('TestFlipPointCloud', () => {
    describe('test_flip_x_axis', () => {
        it('should flip the point cloud across the x-axis', () => {
            const pointCloud = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
            const expectedOutput = [[1.0, -2.0, 3.0], [4.0, -5.0, 6.0]];
            expect(flipPointCloud(pointCloud, 1)).toEqual(expectedOutput);
        });
    });

    describe('test_flip_y_axis', () => {
        it('should flip the point cloud across the y-axis', () => {
            const pointCloud = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
            const expectedOutput = [[-1.0, 2.0, 3.0], [-4.0, 5.0, 6.0]];
            expect(flipPointCloud(pointCloud, 0)).toEqual(expectedOutput);
        });
    });

    describe('test_flip_z_axis', () => {
        it('should flip the point cloud across the z-axis', () => {
            const pointCloud = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
            const expectedOutput = [[1.0, 2.0, -3.0], [4.0, 5.0, -6.0]];
            expect(flipPointCloud(pointCloud, 2)).toEqual(expectedOutput);
        });
    });

    describe('test_invalid_axis', () => {
        it('should throw an error when an invalid axis is provided', () => {
            const pointCloud = [[1.0, 2.0, 3.0]];
            expect(() => flipPointCloud(pointCloud, 3)).toThrow('Axis must be 0 (x-axis), 1 (y-axis), or 2 (z-axis).');
        });
    });

    describe('test_empty_point_cloud', () => {
        it('should handle an empty point cloud correctly', () => {
            const pointCloud = [];
            const expectedOutput = [];
            expect(flipPointCloud(pointCloud, 0)).toEqual(expectedOutput);
        });
    });
});