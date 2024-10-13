describe('TestFloydWarshallShortestPaths', () => {
    it('test basic functionality', () => {
        // Basic test case with a simple graph
        const matrix = [
            [0, 3, Infinity, 7],
            [8, 0, 2, Infinity],
            [5, Infinity, 0, 1],
            [2, Infinity, Infinity, 0]
        ];
        const expected = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('test single vertex graph', () => {
        // Test case with a single vertex graph (1x1 matrix)
        const matrix = [
            [0]
        ];
        const expected = [
            [0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('test two vertices graph', () => {
        // Test case with two vertices
        const matrix = [
            [0, 1],
            [1, 0]
        ];
        const expected = [
            [0, 1],
            [1, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('test large infinite weights', () => {
        // Test case with infinite weights
        const matrix = [
            [0, Infinity],
            [Infinity, 0]
        ];
        const expected = [
            [0, Infinity],
            [Infinity, 0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('test negative cycle', () => {
        // Test case with a negative cycle
        const matrix = [
            [0, 1, Infinity],
            [Infinity, 0, -1],
            [-1, Infinity, 0]
        ];
        const expected = [
            [-1, 0, -1],
            [-2, -1, -2],
            [-2, -1, -2]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });
});