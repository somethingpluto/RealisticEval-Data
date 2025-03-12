import { Matrix4 } from 'three';

/**
 * Rotate the point cloud around the Y axis by a given angle.
 *
 * @param pointCloud - An Nx3 matrix representing the 3D point cloud.
 * @param rotationAngle - The angle (in radians) to rotate the point cloud.
 * @returns An Nx3 matrix of the rotated point cloud.
 */
function rotatePointCloud(pointCloud: number[][], rotationAngle: number): number[][] {
    const cosTheta = Math.cos(rotationAngle);
    const sinTheta = Math.sin(rotationAngle);
    const rotationMatrix: Matrix4 = new Matrix4().makeRotationY(rotationAngle);

    return pointCloud.map(point => rotationMatrix.applyVector3(new Vector3(...point)));
}
describe('TestRotatePointCloud', () => {
    /**
     * Test when rotation angle is 0 (should return the same point cloud).
     */
    test('no rotation', () => {
        const pointCloud = [[1.0, 2.0, 3.0]];
        const rotationAngle = 0;
        const expectedOutput = pointCloud;

        expect(rotatePointCloud(pointCloud, rotationAngle)).toEqual(expectedOutput);
    });

    /**
     * Test rotation of 180 degrees (π radians) around Y axis.
     */
    test('180 degree rotation', () => {
        const pointCloud = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]];
        const rotationAngle = Math.PI; // 180 degrees
        const expectedOutput = [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]; // [1,0,0] -> [-1,0,0]

        expect(rotatePointCloud(pointCloud, rotationAngle)).toEqual(expectedOutput);
    });

    /**
     * Test rotation of 360 degrees (2π radians) around Y axis (should return same point cloud).
     */
    test('full rotation', () => {
        const pointCloud = [[1.0, 2.0, 3.0]];
        const rotationAngle = 2 * Math.PI; // 360 degrees
        const expectedOutput = pointCloud; // Should return the same point cloud

        expect(rotatePointCloud(pointCloud, rotationAngle)).toEqual(expectedOutput);
    });
});
