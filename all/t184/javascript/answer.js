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
        const temp = this.heap[a];
        this.heap[a] = this.heap[b];
        this.heap[b] = temp;
    }

    // Heapify up to maintain the max-heap property after insertion
    heapifyUp(index) {
        while (index > 0 && this.heap[this.parent(index)] < this.heap[index]) {
            this.swap(this.parent(index), index);
            index = this.parent(index);
        }
    }

    // Heapify down to maintain the max-heap property after deletion
    heapifyDown(index) {
        const size = this.heap.length;
        let largest = index;

        const left = this.leftChild(index);
        const right = this.rightChild(index);

        if (left < size && this.heap[left] > this.heap[largest]) {
            largest = left;
        }

        if (right < size && this.heap[right] > this.heap[largest]) {
            largest = right;
        }

        if (largest !== index) {
            this.swap(index, largest);
            this.heapifyDown(largest);
        }
    }

    // Insert an element into the priority queue
    push(value) {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }

    // Remove the maximum element from the priority queue
    pop() {
        if (this.isEmpty()) {
            throw new Error("Priority queue is empty");
        }
        this.heap[0] = this.heap[this.heap.length - 1];
        this.heap.pop();
        if (!this.isEmpty()) {
            this.heapifyDown(0);
        }
    }

    // Get the maximum element without removing it
    top() {
        if (this.isEmpty()) {
            throw new Error("Priority queue is empty");
        }
        return this.heap[0];
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