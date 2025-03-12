class MaxHeap {
    constructor() {
        this.heap = []; // Array to store heap elements
    }

    // Helper function to maintain the max heap property
    heapifyUp(index) {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[index] > this.heap[parentIndex]) {
                // Swap the elements if the child is greater than the parent
                [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    // Helper function to maintain the max heap property after deletion
    heapifyDown(index) {
        const length = this.heap.length;
        while (true) {
            const leftChildIndex = 2 * index + 1;
            const rightChildIndex = 2 * index + 2;
            let largestIndex = index;

            if (leftChildIndex < length && this.heap[leftChildIndex] > this.heap[largestIndex]) {
                largestIndex = leftChildIndex;
            }

            if (rightChildIndex < length && this.heap[rightChildIndex] > this.heap[largestIndex]) {
                largestIndex = rightChildIndex;
            }

            if (largestIndex !== index) {
                // Swap the elements if the child is greater than the parent
                [this.heap[index], this.heap[largestIndex]] = [this.heap[largestIndex], this.heap[index]];
                index = largestIndex;
            } else {
                break;
            }
        }
    }

    // Insert a new element into the heap
    insert(value) {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }

    // Remove and return the maximum element from the heap
    extractMax() {
        if (this.isEmpty()) {
            return null;
        }

        const max = this.heap[0];
        const lastElement = this.heap.pop();

        if (!this.isEmpty()) {
            this.heap[0] = lastElement;
            this.heapifyDown(0);
        }

        return max;
    }

    // Get the maximum element without removing it
    getMax() {
        return this.isEmpty() ? null : this.heap[0];
    }

    // Check if the heap is empty
    isEmpty() {
        return this.heap.length === 0;
    }

    // Get the size of the heap
    size() {
        return this.heap.length;
    }
}
describe("MaxHeap Operations", () => {
    let maxHeap;

    beforeEach(() => {
        maxHeap = new MaxHeap(); // Initialize a new MaxHeap before each test
    });

    test("Initial state of the heap", () => {
        expect(maxHeap.isEmpty()).toBe(true);
        expect(maxHeap.size()).toBe(0);
    });

    test("Insert elements into the heap", () => {
        maxHeap.insert(10);
        maxHeap.insert(20);
        maxHeap.insert(5);

        expect(maxHeap.isEmpty()).toBe(false);
        expect(maxHeap.size()).toBe(3);
        expect(maxHeap.getMax()).toBe(20); // The maximum should be 20
    });

    test("Extract maximum element from the heap", () => {
        maxHeap.insert(10);
        maxHeap.insert(30);
        maxHeap.insert(20);

        const maxElement = maxHeap.extractMax();
        expect(maxElement).toBe(30); // The maximum extracted should be 30
        expect(maxHeap.getMax()).toBe(20); // The next maximum should be 20
        expect(maxHeap.size()).toBe(2); // Size should be 2 after extraction
    });

    test("Heap should maintain max heap property after multiple operations", () => {
        maxHeap.insert(15);
        maxHeap.insert(10);
        maxHeap.insert(30);
        maxHeap.insert(20);
        maxHeap.insert(25);

        // Current max should be 30
        expect(maxHeap.getMax()).toBe(30);

        maxHeap.extractMax(); // Remove 30
        // After removal, the new max should be 25
        expect(maxHeap.getMax()).toBe(25);

        maxHeap.extractMax(); // Remove 25
        // After removal, the new max should be 20
        expect(maxHeap.getMax()).toBe(20);

        // The size of the heap should be 3 now
        expect(maxHeap.size()).toBe(3);
    });
});
