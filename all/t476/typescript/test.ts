import { topological_sort_dfs } from './topologicalSort';

describe('topological_sort_dfs', () => {
    test('should return correct topological order', () => {
        const vertices = [5, 4, 3, 2, 1];
        const edges: [number, number][] = [
            [5, 2],
            [5, 0],
            [4, 0],
            [4, 1],
            [2, 3],
            [3, 1]
        ];

        const result = topological_sort_dfs(vertices, edges);
        expect(result).toEqual([5, 4, 2, 3, 1, 0]);
    });

    test('should return empty array if there is a cycle', () => {
        const vertices = [5, 4, 3, 2, 1];
        const edges: [number, number][] = [
            [5, 2],
            [5, 0],
            [4, 0],
            [4, 1],
            [2, 3],
            [3, 1],
            [3, 2] // Cycle detected
        ];

        const result = topological_sort_dfs(vertices, edges);
        expect(result).toEqual([]);
    });
});