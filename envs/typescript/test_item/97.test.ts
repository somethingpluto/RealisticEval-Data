class Queue<T> {
    private items: T[];

    constructor() {
        this.items = [];
    }

    enqueue(element: T): void {
        this.items.push(element);
    }

    dequeue(): T | string {
        if (this.isEmpty()) {
            return "Underflow";
        }
        return this.items.shift() as T;
    }

    front(): T | string {
        if (this.isEmpty()) {
            return "No elements in Queue";
        }
        return this.items[0];
    }

    isEmpty(): boolean {
        return this.items.length === 0;
    }

    printQueue(): string {
        return this.items.join(' ');
    }
}
describe('Queue Class', () => {
    let queue: Queue<number>;

    beforeEach(() => {
        queue = new Queue<number>();
    });

    test('should initialize an empty queue', () => {
        expect(queue.isEmpty()).toBe(true);
    });

    test('should enqueue elements to the queue', () => {
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        expect(queue.printQueue()).toBe('1 2 3');
        expect(queue.isEmpty()).toBe(false);
    });

    test('should dequeue elements from the queue', () => {
        queue.enqueue(1);
        queue.enqueue(2);
        const dequeuedElement = queue.dequeue();
        expect(dequeuedElement).toBe(1);
    });

    test('should return the front element without removing it', () => {
        queue.enqueue(10);
        queue.enqueue(20);
        const frontElement = queue.front();
        expect(frontElement).toBe(10);
    });

    test('should check if the queue is empty', () => {
        expect(queue.isEmpty()).toBe(true);
        queue.enqueue(5);
        expect(queue.isEmpty()).toBe(false);
        queue.dequeue();
        expect(queue.isEmpty()).toBe(true);
    });
});
