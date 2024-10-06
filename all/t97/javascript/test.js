describe('Queue Class', () => {
    let queue;

    beforeEach(() => {
        queue = new Queue();
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