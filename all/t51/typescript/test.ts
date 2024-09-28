import { NDArray } from 'numeric';
import numeric from 'numeric';
import { changeReferenceFrame } from './yourModule'; // Ensure to import your function 

describe('changeReferenceFrame function', () => {
    let pointCloud: NDArray;
    let refFramePoints: NDArray[];

    beforeEach(() => {
        // Basic setup for tests, initialize some common point clouds and frames
        pointCloud = numeric.clone([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
        refFramePoints = [numeric.clone([0, 0, 0]), numeric.clone([1, 0, 0]), numeric.clone([0, 1, 0])];
    });

    test('identity transformation', () => {
        // Test with an identity transformation where the reference frame is the standard basis
        const result = changeReferenceFrame(pointCloud, refFramePoints);
        expect(result).toEqual(numeric.sub(pointCloud, [0, 0, 0]));
    });

    test('translation', () => {
        // Only translation no rotation; move the origin
        const framePoints = [numeric.clone([1, 1, 1]), numeric.clone([2, 1, 1]), numeric.clone([1, 2, 1])];
        const result = changeReferenceFrame(pointCloud, framePoints);
        const expected = numeric.clone([[-1, 0, 1], [2, 3, 4], [5, 6, 7]]);
        expect(result).toEqual(expected);
    });

    test('rotation', () => {
        // Rotation about z-axis by 90 degrees
        const framePoints = [numeric.clone([0, 0, 0]), numeric.clone([0, 1, 0]), numeric.clone([0, 1, 1])];
        const result = changeReferenceFrame(pointCloud, framePoints);
        const expected = numeric.clone([[2, 3, 1], [5, 6, 4], [8, 9, 7]]);
        expect(result).toEqual(expected);
    });

    test('non-orthonormal frame', () => {
        // Use non-orthonormal frame to see how function handles it (should normalize internally)
        const framePoints = [numeric.clone([0, 0, 0]), numeric.clone([1, 0, 0]), numeric.clone([1, 1, 0])];
        const result = changeReferenceFrame(pointCloud, framePoints);

        const u = numeric.clone([1, 0, 0]);
        const v = numeric.clone([0, 1, 0]);
        const w = numeric.cross(u, v);
        const rotationMatrix = numeric.transpose([u, v, w]);
        const expected = numeric.dot(pointCloud, rotationMatrix);
        
        expect(result).toEqual(expected);
    });

    test('inverted frame', () => {
        // Inverting the frame to see if negatives are handled
        const framePoints = [numeric.clone([0, 0, 0]), numeric.clone([-1, 0, 0]), numeric.clone([0, -1, 0])];
        const result = changeReferenceFrame(pointCloud, framePoints);
        const expected = numeric.dot(pointCloud, [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]);
        expect(result).toEqual(expected);
    });
});