import { Matrix4 } from 'three';

function transformPointCloudToReferenceFrame(
    pointCloud: number[][],
    refFramePoints: number[][]
): number[][] {
    if (pointCloud.length < 3 || refFramePoints.length < 3) {
        throw new Error('Both pointCloud and refFramePoints must contain at least three points.');
    }

    if (pointCloud.some(point => point.length !== 3) || refFramePoints.some(point => point.length !== 3)) {
        throw new Error('All points must be 3-dimensional.');
    }

    // Create transformation matrix
    const matrix = Matrix4.fromArray([
        refFramePoints[0][0], refFramePoints[0][1], refFramePoints[0][2], 0,
        refFramePoints[1][0], refFramePoints[1][1], refFramePoints[1][2], 0,
        refFramePoints[2][0], refFramePoints[2][1], refFramePoints[2][2], 0,
        0, 0, 0, 1
    ]);

    // Apply transformation to each point in the point cloud
    return pointCloud.map(point => matrix.applyVector3(new THREE.Vector3(...point)));
}
describe('TestChangeReferenceFrame', () => {
    let pointCloud;
    let refFramePoints;

    beforeEach(() => {
        // Basic setup for tests, initialize some common point clouds and frames
        pointCloud = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ];
        refFramePoints = [
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0]
        ];
    });

    test('identity transformation', () => {
        // Test with an identity transformation where the reference frame is the standard basis
        const result = transformPointCloudToReferenceFrame(pointCloud, refFramePoints);
        const expected = pointCloud.map(point => point.map(coord => coord - 0)); // No change expected
        expect(result).toEqual(expected);
    });

    test('translation', () => {
        // Only translation, no rotation; move the origin
        const framePoints = [
            [1, 1, 1],
            [2, 1, 1],
            [1, 2, 1]
        ];
        const result = transformPointCloudToReferenceFrame(pointCloud, framePoints);
        const expected = [
            [-1, 0, 1],
            [2, 3, 4],
            [5, 6, 7]
        ];
        expect(result).toEqual(expected);
    });

    test('rotation', () => {
        // Rotation about z-axis by 90 degrees
        const framePoints = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 1]
        ];
        const result = transformPointCloudToReferenceFrame(pointCloud, framePoints);
        const expected = [
            [2, 3, 1],
            [5, 6, 4],
            [8, 9, 7]
        ];
        expect(result).toEqual(expected);
    });

    test('non-orthonormal frame', () => {
        // Use non-orthonormal frame to see how function handles it
        const framePoints = [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0]
        ];
        const result = transformPointCloudToReferenceFrame(pointCloud, framePoints);
        // Manually compute expected model_answer_result
        const u = [1, 0, 0];
        const v = [0, 1, 0];
        const w = crossProduct(u, v); // Assuming you have a crossProduct function defined
        const rotationMatrix = [u, v, w];
        const expected = pointCloud.map(point => {
            return point.map((_, i) => point.reduce((sum, val, j) => sum + val * rotationMatrix[j][i], 0));
        });
        expect(result).toEqual(expected);
    });

    test('inverted frame', () => {
        // Inverting the frame to see if negatives are handled
        const framePoints = [
            [0, 0, 0],
            [-1, 0, 0],
            [0, -1, 0]
        ];
        const result = transformPointCloudToReferenceFrame(pointCloud, framePoints);
        const expected = pointCloud.map(point => {
            return [
                -point[0],
                -point[1],
                point[2]
            ];
        });
        expect(result).toEqual(expected);
    });
});
