describe("Queue Operations", () => {
    let queue;

    beforeEach(() => {
        queue = new Queue(); // Create a new queue before each test
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
        expect(value).toBe(null); // Should indicate that the queue is empty
    });

    test("Front element of an empty queue", () => {
        const frontValue = queue.front();
        expect(frontValue).toBe(null); // Should indicate that the queue is empty
    });

    test("Queue should become empty after dequeuing all elements", () => {
        queue.enqueue(10);
        queue.enqueue(20);

        queue.dequeue(); // Remove 10
        queue.dequeue(); // Remove 20

        expect(queue.isEmpty()).toBe(true); // Queue should be empty
    });
});