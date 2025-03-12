class Node {
    data: number;
    next: Node | null;

    constructor(val: number) {
        this.data = val;
        this.next = null;
    }
}

class Queue {
    private head: Node | null;
    private tail: Node | null;

    constructor() {
        this.head = null;
        this.tail = null;
    }

    isEmpty(): boolean {
        return this.head === null;
    }

    enqueue(value: number): void {
        const newNode = new Node(value);
        if (this.isEmpty()) {
            this.head = newNode;
        } else {
            this.tail!.next = newNode;
        }
        this.tail = newNode;
    }

    dequeue(): number | null {
        if (this.isEmpty()) {
            return null;
        }
        const removedNode = this.head;
        this.head = this.head!.next;
        if (this.head === null) {
            this.tail = null;
        }
        return removedNode!.data;
    }

    front(): number | null {
        return this.isEmpty() ? null : this.head!.data;
    }
}
describe("Queue Operations", () => {
    let queue: Queue;

    beforeEach(() => {
        queue = new Queue(); // Create a new queue instance before each test
    });

    test("Queue should be empty initially", () => {
        expect(queue.isEmpty()).toBe(true);
    });

    test("Enqueue elements", () => {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        expect(queue.isEmpty()).toBe(false);
        expect(queue.front()).toBe(10); // Front element should be 10
    });

    test("Dequeue elements", () => {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        const value = queue.dequeue();
        expect(value).toBe(10); // First dequeued element should be 10
        expect(queue.front()).toBe(20); // Now front should be 20
    });

    test("Dequeue from an empty queue", () => {
        const value = queue.dequeue();
        expect(value).toBe(-1); // Should indicate that the queue is empty
    });

    test("Front element of an empty queue", () => {
        const frontValue = queue.front();
        expect(frontValue).toBe(-1); // Should indicate that the queue is empty
    });

    test("Queue should become empty after dequeuing all elements", () => {
        queue.enqueue(10);
        queue.enqueue(20);

        queue.dequeue(); // Remove 10
        queue.dequeue(); // Remove 20

        expect(queue.isEmpty()).toBe(true); // Queue should be empty
    });
});
