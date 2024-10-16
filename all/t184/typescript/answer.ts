class PriorityQueue {
    private heap: number[] = []; // This will store the elements of the heap

    // Helper function to get the index of the parent
    private parent(index: number): number {
        return Math.floor((index - 1) / 2);
    }

    // Helper function to get the index of the left child
    private leftChild(index: number): number {
        return 2 * index + 1;
    }

    // Helper function to get the index of the right child
    private rightChild(index: number): number {
        return 2 * index + 2;
    }

    // Helper function to swap two elements in the heap
    private swap(a: number, b: number): void {
        const temp = this.heap[a];
        this.heap[a] = this.heap[b];
        this.heap[b] = temp;
    }

    // Heapify up to maintain the max-heap property after insertion
    private heapifyUp(index: number): void {
        while (index > 0 && this.heap[this.parent(index)] < this.heap[index]) {
            this.swap(this.parent(index), index);
            index = this.parent(index);
        }
    }

    // Heapify down to maintain the max-heap property after deletion
    private heapifyDown(index: number): void {
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
    public push(value: number): void {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }

    // Remove the maximum element from the priority queue
    public pop(): void {
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
    public top(): number {
        if (this.isEmpty()) {
            throw new Error("Priority queue is empty");
        }
        return this.heap[0];
    }

    // Check if the priority queue is empty
    public isEmpty(): boolean {
        return this.heap.length === 0;
    }

    // Get the size of the priority queue
    public size(): number {
        return this.heap.length;
    }
}