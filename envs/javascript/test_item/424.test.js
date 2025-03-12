/**
 * Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.
 * @param {Object} graph - An object representing the adjacency list of the graph. Each key is a node, and the value is an array of objects {neighbor, weight}.
 * @param {string} start - The starting node for the shortest path search.
 * @returns {Object} - An object with the shortest distance from the start node to each node.
 */
function dijkstra(graph, start) {
    // Initialize distances with infinity for all nodes except the start node
    const distances = {};
    const visited = new Set();
    const priorityQueue = new MinHeap();

    for (const node in graph) {
        distances[node] = Infinity;
    }
    distances[start] = 0;

    // Insert the start node into the priority queue
    priorityQueue.insert(start, 0);

    while (!priorityQueue.isEmpty()) {
        const currentNode = priorityQueue.extractMin();

        if (visited.has(currentNode)) continue;
        visited.add(currentNode);

        // Explore neighbors
        for (const { neighbor, weight } of graph[currentNode]) {
            if (visited.has(neighbor)) continue;

            const newDistance = distances[currentNode] + weight;
            if (newDistance < distances[neighbor]) {
                distances[neighbor] = newDistance;
                priorityQueue.insert(neighbor, newDistance);
            }
        }
    }

    return distances;
}

// MinHeap class for the priority queue
class MinHeap {
    constructor() {
        this.heap = [];
        this.nodeIndexMap = new Map();
    }

    insert(node, priority) {
        this.heap.push({ node, priority });
        this.nodeIndexMap.set(node, this.heap.length - 1);
        this.bubbleUp(this.heap.length - 1);
    }

    extractMin() {
        if (this.heap.length === 1) {
            const min = this.heap.pop();
            this.nodeIndexMap.clear();
            return min.node;
        }

        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.nodeIndexMap.set(this.heap[0].node, 0);
        this.nodeIndexMap.delete(min.node);
        this.bubbleDown(0);

        return min.node;
    }

    isEmpty() {
        return this.heap.length === 0;
    }

    bubbleUp(index) {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[index].priority < this.heap[parentIndex].priority) {
                this.swap(index, parentIndex);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    bubbleDown(index) {
        const length = this.heap.length;
        while (true) {
            const leftChildIndex = 2 * index + 1;
            const rightChildIndex = 2 * index + 2;
            let smallestIndex = index;

            if (leftChildIndex < length && this.heap[leftChildIndex].priority < this.heap[smallestIndex].priority) {
                smallestIndex = leftChildIndex;
            }

            if (rightChildIndex < length && this.heap[rightChildIndex].priority < this.heap[smallestIndex].priority) {
                smallestIndex = rightChildIndex;
            }

            if (smallestIndex !== index) {
                this.swap(index, smallestIndex);
                index = smallestIndex;
            } else {
                break;
            }
        }
    }

    swap(index1, index2) {
        const temp = this.heap[index1];
        this.heap[index1] = this.heap[index2];
        this.heap[index2] = temp;

        this.nodeIndexMap.set(this.heap[index1].node, index1);
        this.nodeIndexMap.set(this.heap[index2].node, index2);
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
