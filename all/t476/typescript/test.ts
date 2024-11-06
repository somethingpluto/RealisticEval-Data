describe('TestTopologicalSortDFS', () => {
    describe('test_simple_chain', () => {
        it('should sort a simple chain correctly', () => {
            const vertices = [1, 2, 3];
            const edges = [[1, 2], [2, 3]];
            expect(topologicalSortDFS(vertices, edges)).toEqual([1, 2, 3]);
        });
    });

    describe('test_disconnected_graph', () => {
        it('should handle a disconnected graph correctly', () => {
            const vertices = [1, 2, 3, 4];
            const edges = [[1, 2]];
            const result = topologicalSortDFS(vertices, edges);

            expect(result.indexOf(1)).toBeLessThan(result.indexOf(2));
            expect(result.includes(3) && result.includes(4)).toBeTruthy();
        });
    });

    describe('test_complex_graph', () => {
        it('should handle a complex graph correctly', () => {
            const vertices = [1, 2, 3, 4, 5, 6];
            const edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [6, 1]];
            const result = topologicalSortDFS(vertices, edges);

            expect(result.indexOf(1)).toBeLessThan(result.indexOf(2));
            expect(result.indexOf(1)).toBeLessThan(result.indexOf(3));
            expect(result.indexOf(2)).toBeLessThan(result.indexOf(4));
            expect(result.indexOf(3)).toBeLessThan(result.indexOf(4));
            expect(result.indexOf(4)).toBeLessThan(result.indexOf(5));
            expect(result.indexOf(6)).toBeLessThan(result.indexOf(1));
        });
    });

    describe('test_single_vertex', () => {
        it('should handle a single vertex correctly', () => {
            const vertices = [1];
            const edges = [];
            expect(topologicalSortDFS(vertices, edges)).toEqual([1]);
        });
    });
});