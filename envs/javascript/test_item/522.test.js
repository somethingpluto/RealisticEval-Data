/**
 * Rotate the point cloud around the Y axis by a given angle.
 *
 * @param {Array<Array<number>>} pointCloud - A N x 3 array representing the 3D point cloud.
 * @param {number} rotationAngle - The angle (in radians) to rotate the point cloud.
 * @returns {Array<Array<number>>} - A N x 3 array of the rotated point cloud.
 */
function rotatePointCloud(pointCloud, rotationAngle) {
    // Create a new array to store the rotated points
    const rotatedPointCloud = [];

    // Precompute the cosine and sine of the rotation angle
    const cosAngle = Math.cos(rotationAngle);
    const sinAngle = Math.sin(rotationAngle);

    // Iterate over each point in the point cloud
    for (let i = 0; i < pointCloud.length; i++) {
        const [x, y, z] = pointCloud[i];

        // Apply the rotation matrix around the Y axis
        const rotatedX = x * cosAngle + z * sinAngle;
        const rotatedY = y;
        const rotatedZ = z * cosAngle - x * sinAngle;

        // Add the rotated point to the new point cloud
        rotatedPointCloud.push([rotatedX, rotatedY, rotatedZ]);
    }

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
