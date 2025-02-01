/**
 * Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
 * @param {Object} graph - An object representing the adjacency list of the graph. Each key is a node, and the value is an array of objects {neighbor, weight}.
 * @param {string} start - The starting node for the shortest path search.
 * @returns {Object} - An object with the shortest distance from the start node to each node.
 */
function dijkstra(graph, start) {
    const distances = {};
    const previous = {};
    const queue = new PriorityQueue((a, b) => a.priority - b.priority);

    // Initialize distances and previous nodes
    for (const node in graph) {
        distances[node] = Infinity;
        previous[node] = null;
    }

    distances[start] = 0;
    queue.enqueue({ node: start, priority: 0 });

    while (!queue.isEmpty()) {
        const { node } = queue.dequeue();

        for (const neighbor of graph[node]) {
            const alt = distances[node] + neighbor.weight;
            if (alt < distances[neighbor.neighbor]) {
                distances[neighbor.neighbor] = alt;
                previous[neighbor.neighbor] = node;
                queue.enqueue({ node: neighbor.neighbor, priority: alt });
            }
        }
    }

    return distances;
}

// PriorityQueue class for managing nodes in the queue
class PriorityQueue {
    constructor(comparator = (a, b) => a - b) {
        this._heap = [];
        this._comparator = comparator;
    }

    size() {
        return this._heap.length;
    }

    isEmpty() {
        return this.size() == 0;
    }

    peek() {
        return this._heap[0];
    }

    push(value) {
        this._heap.push(value);
        this._siftUp();
    }

    pop() {
        const poppedValue = this.peek();
        const bottom = this.size() - 1;
        if (bottom > 0) {
            this._swap(0, bottom);
        }
        this._heap.pop();
        this._siftDown();
        return poppedValue;
    }

    _greater(i, j) {
        return this._comparator(this._heap[i], this._heap[j]) > 0;
    }

    _swap(i, j) {
        [this._heap[i], this._heap[j]] = [this._heap[j], this._heap[i]];
    }

    _siftUp() {
        let node = this.size() - 1;
        while (node > 0 && this._greater(Math.floor((node - 1) / 2), node)) {
            this._swap(node, Math.floor((node - 1) / 2));
            node = Math.floor((node - 1) / 2);
        }
    }

    _siftDown() {
        let node = 0;
        while (
            (2 * node + 1 < this.size() && this._greater(node, 2 * node + 1)) ||
            (2 * node + 2 < this.size() && this._greater(node, 2 * node + 2))
        ) {
            let maxChild = 2 * node + 1;
            if (2 * node + 2 < this.size() && this._greater(2 * node + 2, 2 * node + 1)) {
                maxChild = 2 * node + 2;
            }
            this._swap(node, maxChild);
            node = maxChild;
        }
    }
}
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
