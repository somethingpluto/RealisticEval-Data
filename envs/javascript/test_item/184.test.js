class PriorityQueue {
    constructor() {
        this.heap = []; // This will store the elements of the heap
    }

    // Helper function to get the index of the parent
    parent(index) {
        return Math.floor((index - 1) / 2);
    }

    // Helper function to get the index of the left child
    leftChild(index) {
        return 2 * index + 1;
    }

    // Helper function to get the index of the right child
    rightChild(index) {
        return 2 * index + 2;
    }

    // Helper function to swap two elements in the heap
    swap(a, b) {
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
    }

    // Heapify up to maintain the max-heap property after insertion
    heapifyUp(index) {
        while (index > 0 && this.heap[index] > this.heap[this.parent(index)]) {
            this.swap(index, this.parent(index));
            index = this.parent(index);
        }
    }

    // Heapify down to maintain the max-heap property after deletion
    heapifyDown(index) {
        let maxIndex = index;
        let left = this.leftChild(index);
        let right = this.rightChild(index);

        if (left < this.heap.length && this.heap[left] > this.heap[maxIndex]) {
            maxIndex = left;
        }

        if (right < this.heap.length && this.heap[right] > this.heap[maxIndex]) {
            maxIndex = right;
        }

        if (index !== maxIndex) {
            this.swap(index, maxIndex);
            this.heapifyDown(maxIndex);
        }
    }

    // Insert an element into the priority queue
    push(value) {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }

    // Remove the maximum element from the priority queue
    pop() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        let root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown(0);
        return root;
    }

    // Get the maximum element without removing it
    top() {
        return this.heap.length === 0 ? null : this.heap[0];
    }

    // Check if the priority queue is empty
    isEmpty() {
        return this.heap.length === 0;
    }

    // Get the size of the priority queue
    size() {
        return this.heap.length;
    }
}
const PriorityQueue = require('./PriorityQueue'); // Adjust path as necessary

describe("Priority Queue - Test Cases", () => {
    let pq;

    beforeEach(() => {
        pq = new PriorityQueue();
    });

    test("Insert and access maximum element", () => {
        pq.push(10);
        pq.push(20);
        pq.push(5);
        pq.push(30);
        pq.push(15);

        expect(pq.top()).toBe(30); // Ensure the max element is 30
    });

    test("Remove maximum element", () => {
        pq.push(10);
        pq.push(20);
        pq.push(5);
        pq.push(30);

        pq.pop(); // Remove 30
        expect(pq.top()).toBe(20); // Now the max should be 20
        pq.pop(); // Remove 20
        expect(pq.top()).toBe(10); // Now the max should be 10
    });

    test("Check empty queue", () => {
        expect(pq.isEmpty()).toBe(true); // Initially empty
        pq.push(10);
        expect(pq.isEmpty()).toBe(false); // Now not empty
        pq.pop();
        expect(pq.isEmpty()).toBe(true); // Back to empty
    });

    test("Pop from empty queue", () => {
        expect(() => pq.pop()).toThrow(Error); // Should throw an error
    });

    test("Access top of empty queue", () => {
        expect(() => pq.top()).toThrow(Error); // Should throw an error
    });

    test("Maintain max-heap property", () => {
        pq.push(3);
        pq.push(1);
        pq.push(4);
        pq.push(2);

        expect(pq.top()).toBe(4); // Ensure max is 4

        pq.pop(); // Remove 4
        expect(pq.top()).toBe(3); // Now max is 3

        pq.push(5); // Add 5
        expect(pq.top()).toBe(5); // Ensure max is now 5
    });
});
