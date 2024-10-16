class MaxHeap {
    constructor() {
        this.heap = []; // Array to store heap elements
    }

    // Helper function to maintain the max heap property
    heapifyUp(index) {
        if (index === 0) return; // If the index is 0, it's already the root
        const parentIndex = Math.floor((index - 1) / 2); // Calculate the parent index

        // If the current node is greater than its parent, swap them
        if (this.heap[index] > this.heap[parentIndex]) {
            [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]]; // Swap
            this.heapifyUp(parentIndex); // Recursively heapify up
        }
    }

    // Helper function to maintain the max heap property after deletion
    heapifyDown(index) {
        const leftChild = 2 * index + 1; // Left child index
        const rightChild = 2 * index + 2; // Right child index
        let largest = index;

        // Check if left child exists and is greater than current largest
        if (leftChild < this.heap.length && this.heap[leftChild] > this.heap[largest]) {
            largest = leftChild;
        }

        // Check if right child exists and is greater than current largest
        if (rightChild < this.heap.length && this.heap[rightChild] > this.heap[largest]) {
            largest = rightChild;
        }

        // If largest is not the current index, swap and heapify down
        if (largest !== index) {
            [this.heap[index], this.heap[largest]] = [this.heap[largest], this.heap[index]]; // Swap
            this.heapifyDown(largest); // Recursively heapify down
        }
    }

    // Insert a new element into the heap
    insert(value) {
        this.heap.push(value); // Add value to the end of the array
        this.heapifyUp(this.heap.length - 1); // Restore the heap property
    }

    // Remove and return the maximum element from the heap
    extractMax() {
        if (this.heap.length === 0) {
            throw new Error("Heap is empty");
        }

        const maxElement = this.heap[0]; // Store the max element
        this.heap[0] = this.heap[this.heap.length - 1]; // Move the last element to the root
        this.heap.pop(); // Remove the last element
        this.heapifyDown(0); // Restore the heap property
        return maxElement; // Return the max element
    }

    // Get the maximum element without removing it
    getMax() {
        if (this.heap.length === 0) {
            throw new Error("Heap is empty");
        }
        return this.heap[0]; // Return the root element
    }

    // Check if the heap is empty
    isEmpty() {
        return this.heap.length === 0;
    }

    // Get the size of the heap
    size() {
        return this.heap.length;
    }

    // Display the elements of the heap
    display() {
        if (this.heap.length === 0) {
            console.log("Heap is empty.");
            return;
        }
        console.log("Heap elements:", this.heap.join(" "));
    }
}