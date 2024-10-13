describe('TestFloydWarshallShortestPaths', () => {
    it('should handle basic functionality with a simple graph', () => {
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

    it('should handle a single vertex graph (1x1 matrix)', () => {
        const matrix = [
            [0]
        ];
        const expected = [
            [0]
        ];
        const result = floydWarshallShortestPaths(matrix);
        expect(result).toEqual(expected);
    });

    it('should handle a two vertices graph', () => {
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

    it('should handle large infinite weights', () => {
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

    it('should handle a negative cycle', () => {
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