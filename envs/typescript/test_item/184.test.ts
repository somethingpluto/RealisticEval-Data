class PriorityQueue {
    private heap: number[];

    constructor() {
        this.heap = [];
    }

    private parent(index: number): number {
        return Math.floor((index - 1) / 2);
    }

    private leftChild(index: number): number {
        return 2 * index + 1;
    }

    private rightChild(index: number): number {
        return 2 * index + 2;
    }

    private swap(a: number, b: number): void {
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
    }

    private heapifyUp(index: number): void {
        let currentIndex = index;
        while (
            this.heap[currentIndex] > this.heap[this.parent(currentIndex)]
        ) {
            this.swap(currentIndex, this.parent(currentIndex));
            currentIndex = this.parent(currentIndex);
        }
    }

    private heapifyDown(index: number): void {
        let currentIndex = index;
        let largestIndex = currentIndex;
        const left = this.leftChild(currentIndex);
        const right = this.rightChild(currentIndex);

        if (left < this.heap.length && this.heap[left] > this.heap[largestIndex]) {
            largestIndex = left;
        }

        if (right < this.heap.length && this.heap[right] > this.heap[largestIndex]) {
            largestIndex = right;
        }

        if (currentIndex !== largestIndex) {
            this.swap(currentIndex, largestIndex);
            this.heapifyDown(largestIndex);
        }
    }

    public push(value: number): void {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }

    public pop(): void {
        if (this.isEmpty()) {
            throw new Error("Priority queue is empty");
        }
        this.swap(0, this.heap.length - 1);
        const poppedValue = this.heap.pop()!;
        this.heapifyDown(0);
        return poppedValue;
    }

    public top(): number {
        if (this.isEmpty()) {
            throw new Error("Priority queue is empty");
        }
        return this.heap[0];
    }

    public isEmpty(): boolean {
        return this.heap.length === 0;
    }

    public size(): number {
        return this.heap.length;
    }
}
describe("Priority Queue - Test Cases", () => {
    let pq: PriorityQueue;

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
        expect(() => pq.pop()).toThrowError("Priority queue is empty"); // Should throw an error
    });

    test("Access top of empty queue", () => {
        expect(() => pq.top()).toThrowError("Priority queue is empty"); // Should throw an error
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
