import { floydWarshallShortestPaths } from './floydWarshall'; // Adjust the import based on your file structure

describe('Floyd-Warshall Algorithm', () => {
    test('basic functionality', () => {
        const matrix: (number | Infinity)[][] = [
            [0, 3, Infinity, 7],
            [8, 0, 2, Infinity],
            [5, Infinity, 0, 1],
            [2, Infinity, Infinity, 0]
        ];
        const expected: (number | Infinity)[][] = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    test('single vertex graph', () => {
        const matrix: (number | Infinity)[][] = [
            [0]
        ];
        const expected: (number | Infinity)[][] = [
            [0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    test('two vertices graph', () => {
        const matrix: (number | Infinity)[][] = [
            [0, 1],
            [1, 0]
        ];
        const expected: (number | Infinity)[][] = [
            [0, 1],
            [1, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    test('large infinite weights', () => {
        const matrix: (number | Infinity)[][] = [
            [0, Infinity],
            [Infinity, 0]
        ];
        const expected: (number | Infinity)[][] = [
            [0, Infinity],
            [Infinity, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    test('negative cycle', () => {
        const matrix: (number | Infinity)[][] = [
            [0, 1, Infinity],
            [Infinity, 0, -1],
            [-1, Infinity, 0]
        ];
        const expected: (number | Infinity)[][] = [
            [-1, 0, -1],
            [-2, -1, -2],
            [-2, -1, -2]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });
});