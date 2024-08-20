describe('Queue', () => {
    let queue;

    beforeEach(() => {
        queue = new Queue();
    });

    test('should add elements to the queue using enqueue', () => {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        expect(queue.printQueue()).toBe('10 20 30');
    });

    test('should remove elements from the front of the queue using dequeue', () => {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        const removedElement = queue.dequeue();
        expect(removedElement).toBe(10);
        expect(queue.printQueue()).toBe('20 30');
    });

    test('should return "Underflow" when dequeue is called on an empty queue', () => {
        const result = queue.dequeue();
        expect(result).toBe('Underflow');
    });

    test('should return the front element using front without removing it', () => {
        queue.enqueue(10);
        queue.enqueue(20);
        const frontElement = queue.front();
        expect(frontElement).toBe(10);
        expect(queue.printQueue()).toBe('10 20'); // Ensure the element is not removed
    });

    test('should return true when isEmpty is called on an empty queue', () => {
        expect(queue.isEmpty()).toBe(true);
        queue.enqueue(10);
        expect(queue.isEmpty()).toBe(false);
    });
});