/**
 * Translate the point cloud by a given vector.
 *
 * @param {Array<Array<number>>} pointCloud - An N x 3 array representing the 3D point cloud.
 * @param {Array<number>} translationVector - A 1 x 3 array representing the translation vector.
 * @returns {Array<Array<number>>} - An N x 3 array of the translated point cloud.
 */
function translatePointCloud(pointCloud, translationVector) {
    return pointCloud.map(point => [
        point[0] + translationVector[0],
        point[1] + translationVector[1],
        point[2] + translationVector[2]
    ]);
}
describe('TestTranslatePointCloud', () => {
    describe('test_simple_translation', () => {
        it('should correctly translate a single point', () => {
            const pointCloud = [[1.0, 2.0, 3.0]];
            const translationVector = [1.0, 1.0, 1.0];
            const expectedOutput = [[2.0, 3.0, 4.0]];
            expect(translatePointCloud(pointCloud, translationVector)).toEqual(expectedOutput);
        });
    });

    describe('test_multiple_points_translation', () => {
        it('should correctly translate multiple points', () => {
            const pointCloud = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
            const translationVector = [1.0, 2.0, 3.0];
            const expectedOutput = [[2.0, 4.0, 6.0], [5.0, 7.0, 9.0]];
            expect(translatePointCloud(pointCloud, translationVector)).toEqual(expectedOutput);
        });
    });

    describe('test_zero_translation', () => {
        it('should return the same point cloud when translating by a zero vector', () => {
            const pointCloud = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
            const translationVector = [0.0, 0.0, 0.0];
            const expectedOutput = pointCloud;
            expect(translatePointCloud(pointCloud, translationVector)).toEqual(expectedOutput);
        });
    });

    describe('test_negative_translation', () => {
        it('should correctly translate with negative values', () => {
            const pointCloud = [[1.0, 2.0, 3.0]];
            const translationVector = [-1.0, -2.0, -3.0];
            const expectedOutput = [[0.0, 0.0, 0.0]];
            expect(translatePointCloud(pointCloud, translationVector)).toEqual(expectedOutput);
        });
    });
});
