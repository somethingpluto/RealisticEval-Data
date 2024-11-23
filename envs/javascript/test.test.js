import math from 'mathjs'
function rotatePointCloud(pointCloud, rotationAngle) {
    const rotationMatrix = math.matrix([
        [math.cos(rotationAngle), 0, math.sin(rotationAngle)],
        [0, 1, 0],
        [-math.sin(rotationAngle), 0, math.cos(rotationAngle)]
    ]);

    // Rotate the point cloud by multiplying with the rotation matrix
    const rotatedPointCloud = math.multiply(pointCloud, rotationMatrix);

    return rotatedPointCloud;
}
describe('TestRotatePointCloud', () => {
    it('test_no_rotation', () => {
        /** 
         * Test when rotation angle is 0 (should return the same point cloud).
         */
        const pointCloud = [[1.0, 2.0, 3.0]];
        const rotationAngle = 0;
        const expectedOutput = pointCloud;

        const rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);
        expect(rotatedPointCloud).toEqual(expectedOutput);
    });

    it('test_180_degree_rotation', () => {
        /** 
         * Test rotation of 180 degrees (π radians) around Y axis.
         */
        const pointCloud = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]];
        const rotationAngle = Math.PI; // 180 degrees
        const expectedOutput = [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]; // [1,0,0] -> [-1,0,0]

        const rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);
        expect(rotatedPointCloud).toEqual(expectedOutput);
    });

    it('test_full_rotation', () => {
        /** 
         * Test rotation of 360 degrees (2π radians) around Y axis (should return same point cloud).
         */
        const pointCloud = [[1.0, 2.0, 3.0]];
        const rotationAngle = 2 * Math.PI; // 360 degrees
        const expectedOutput = pointCloud; // Should return the same point cloud

        const rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);
        expect(rotatedPointCloud).toEqual(expectedOutput);
    });
});
