class PriorityQueue {
    private heap: number[]; // Internal storage for the binary heap

    constructor() {
        this.heap = []; // Initialize the heap
    }

    // Helper function to swap two elements in the heap
    private swap(a: number, b: number): void {
        const temp = this.heap[a];
        this.heap[a] = this.heap[b];
        this.heap[b] = temp;
    }

    // Function to maintain the heap property by "bubbling up" the element at index
    private heapifyUp(index: number): void {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[index] < this.heap[parentIndex]) {
                this.swap(index, parentIndex);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    // Function to maintain the heap property by "bubbling down" the element at index
    private heapifyDown(index: number): void {
        let leftChild = 2 * index + 1;
        let rightChild = 2 * index + 2;
        let smallest = index;

        if (leftChild < this.heap.length && this.heap[leftChild] < this.heap[smallest]) {
            smallest = leftChild;
        }

        if (rightChild < this.heap.length && this.heap[rightChild] < this.heap[smallest]) {
            smallest = rightChild;
        }

        if (smallest !== index) {
            this.swap(index, smallest);
            this.heapifyDown(smallest);
        }
    }

    // Function to insert a new element into the priority queue
    public insert(value: number): void {
        this.heap.push(value);  // Add the new element at the end of the heap
        this.heapifyUp(this.heap.length - 1); // Restore the heap property
    }

    // Function to get and remove the minimum element from the priority queue
    public extractMin(): number {
        if (this.isEmpty()) {
            throw new Error("Priority queue is empty.");
        }

        const minValue = this.heap[0];
        this.heap[0] = this.heap[this.heap.length - 1]; // Move the last element to the root
        this.heap.pop(); // Remove the last element
        this.heapifyDown(0); // Restore the heap property

        return minValue;
    }

    // Function to peek at the minimum element without removing it
    public peekMin(): number {
        if (this.isEmpty()) {
            throw new Error("Priority queue is empty.");
        }
        return this.heap[0];
    }

    // Function to check if the priority queue is empty
    public isEmpty(): boolean {
        return this.heap.length === 0;
    }

    // Function to get the size of the priority queue
    public size(): number {
        return this.heap.length;
    }

    // Function to print the contents of the priority queue (for debugging purposes)
    public print(): void {
        console.log(this.heap.join(" "));
    }
}