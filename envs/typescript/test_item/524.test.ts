import { Matrix } from './Matrix'; // Assuming Matrix is a class in a local file

/**
 * Scale the point cloud by a given factor.
 *
 * @param pointCloud - A N x 3 matrix representing the 3D point cloud.
 * @param scaleFactor - A number representing the scaling factor.
 * @returns A N x 3 matrix of the scaled point cloud.
 */
function scalePointCloud(pointCloud: Matrix, scaleFactor: number): Matrix {
    // Validate input
    if (!pointCloud || !Array.isArray(pointCloud.data) || !pointCloud.data.every(row => Array.isArray(row) && row.length === 3)) {
        throw new Error('Invalid point cloud data');
    }
    if (typeof scaleFactor !== 'number' || scaleFactor === 0) {
        throw new Error('Invalid scale factor');
    }

    // Scale the point cloud
    const scaledData = pointCloud.data.map(row => row.map(value => value * scaleFactor));

    // Return a new Matrix instance with the scaled data
    return new Matrix(scaledData);
}
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
