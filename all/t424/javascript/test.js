describe('Dijkstra Algorithm Tests', () => {
    beforeEach(() => {
        // Sample graphs for testing
        this.graph1 = {
            'A': [{ neighbor: 'B', weight: 1 }, { neighbor: 'C', weight: 4 }],
            'B': [{ neighbor: 'A', weight: 1 }, { neighbor: 'C', weight: 2 }, { neighbor: 'D', weight: 5 }],
            'C': [{ neighbor: 'A', weight: 4 }, { neighbor: 'B', weight: 2 }, { neighbor: 'D', weight: 1 }],
            'D': [{ neighbor: 'B', weight: 5 }, { neighbor: 'C', weight: 1 }],
        };

        this.graph2 = {
            'A': [{ neighbor: 'B', weight: 2 }],
            'B': [{ neighbor: 'A', weight: 2 }, { neighbor: 'C', weight: 3 }],
            'C': [{ neighbor: 'B', weight: 3 }, { neighbor: 'D', weight: 1 }],
            'D': [{ neighbor: 'C', weight: 1 }],
        };

        this.graphWithIsolatedNode = {
            'A': [{ neighbor: 'B', weight: 1 }],
            'B': [{ neighbor: 'A', weight: 1 }],
            'C': [],  // Isolated node
        };

        this.graphWithNegativeWeight = {
            'A': [{ neighbor: 'B', weight: 2 }, { neighbor: 'C', weight: 1 }],
            'B': [{ neighbor: 'D', weight: 3 }],
            'C': [{ neighbor: 'B', weight: -1 }, { neighbor: 'D', weight: 4 }],
            'D': [],
        };
    });

    it('should compute shortest paths in a normal graph', () => {
        const expected = { 'A': 0, 'B': 1, 'C': 3, 'D': 4 };
        const result = dijkstra(this.graph1, 'A');
        expect(result).toEqual(expected);
    });

    it('should compute shortest paths in a different normal graph', () => {
        const expected = { 'A': 0, 'B': 2, 'C': 5, 'D': 6 };
        const result = dijkstra(this.graph2, 'A');
        expect(result).toEqual(expected);
    });

    it('should compute shortest paths with an isolated node', () => {
        const expected = { 'A': 0, 'B': 1, 'C': Infinity };
        const result = dijkstra(this.graphWithIsolatedNode, 'A');
        expect(result).toEqual(expected);
    });

    it('should compute shortest paths when starting at an isolated node', () => {
        const expected = { 'C': 0, 'A': Infinity, 'B': Infinity };
        const result = dijkstra(this.graphWithIsolatedNode, 'C');
        expect(result).toEqual(expected);
    });
});