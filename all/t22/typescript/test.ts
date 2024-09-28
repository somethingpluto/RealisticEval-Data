import { calculateEuclideanDistance } from './path/to/your/module'; // Adjust the path as needed

describe('calculateEuclideanDistance', () => {
    test('basic functionality', () => {
        const point1: [number, number] = [0, 0];
        const point2: [number, number] = [3, 4];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    test('negative coordinates', () => {
        const point1: [number, number] = [-1, -1];
        const point2: [number, number] = [-4, -5];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    test('zero distance', () => {
        const point1: [number, number] = [2, 3];
        const point2: [number, number] = [2, 3];
        const expectedDistance = 0.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    test('large coordinates', () => {
        const point1: [number, number] = [1e6, 1e6];
        const point2: [number, number] = [1e6 + 3, 1e6 + 4];
        const expectedDistance = 5.0;
        expect(calculateEuclideanDistance(point1, point2)).toBe(expectedDistance);
    });

    test('invalid input', () => {
        expect(() => {
            calculateEuclideanDistance("invalid" as any, [0, 0]);
        }).toThrow(TypeError);
    });
});