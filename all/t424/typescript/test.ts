describe('Dijkstra Algorithm Tests', () => {
    let graph1: Record<string, Array<[string, number]>>;
    let graph2: Record<string, Array<[string, number]>>;
    let graphWithIsolatedNode: Record<string, Array<[string, number]>>;
    let graphWithNegativeWeight: Record<string, Array<[string, number]>>;

    beforeEach(() => {
        // Sample graphs for testing
        graph1 = {
            'A': [['B', 1], ['C', 4]],
            'B': [['A', 1], ['C', 2], ['D', 5]],
            'C': [['A', 4], ['B', 2], ['D', 1]],
            'D': [['B', 5], ['C', 1]],
        };

        graph2 = {
            'A': [['B', 2]],
            'B': [['A', 2], ['C', 3]],
            'C': [['B', 3], ['D', 1]],
            'D': [['C', 1]],
        };

        graphWithIsolatedNode = {
            'A': [['B', 1]],
            'B': [['A', 1]],
            'C': [],  // Isolated node
        };

        graphWithNegativeWeight = {
            'A': [['B', 2], ['C', 1]],
            'B': [['D', 3]],
            'C': [['B', -1], ['D', 4]],
            'D': [],
        };
    });

    it('should compute shortest paths in a normal graph', () => {
        const expected = { 'A': 0, 'B': 1, 'C': 3, 'D': 4 };
        const result = dijkstra(graph1, 'A');
        expect(result).toEqual(expected);
    });

    it('should compute shortest paths in a different normal graph', () => {
        const expected = { 'A': 0, 'B': 2, 'C': 5, 'D': 6 };
        const result = dijkstra(graph2, 'A');
        expect(result).toEqual(expected);
    });

    it('should handle an isolated node', () => {
        const expected = { 'A': 0, 'B': 1, 'C': Infinity };
        const result = dijkstra(graphWithIsolatedNode, 'A');
        expect(result).toEqual(expected);
    });

    it('should handle starting at an isolated node', () => {
        const expected = { 'C': 0, 'A': Infinity, 'B': Infinity };
        const result = dijkstra(graphWithIsolatedNode, 'C');
        expect(result).toEqual(expected);
    });
});