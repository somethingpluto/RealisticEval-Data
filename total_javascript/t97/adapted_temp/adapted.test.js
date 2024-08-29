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
/**
 * realize the basic functions of the data structure queue: enqueue, dequeue, get the front element of the queue, judge whether it is empty, output all elements
 */
class Queue {
    constructor() {
        this.items = [];
    }

    /**
     * Adds an element to the end of the queue.
     * @param {*} element - The element to be added to the queue.
     */
    enqueue(element) {
        this.items.push(element);
    }

    /**
     * Removes and returns the element from the front of the queue.
     * @returns {*} The removed element from the front of the queue, or "Underflow" if the queue is empty.
     */
    dequeue() {
        if (this.isEmpty()) {
            return "Underflow";
        }
        return this.items.shift();
    }

    /**
     * Returns the front element of the queue without removing it.
     * @returns {*} The front element of the queue, or "No elements in Queue" if the queue is empty.
     */
    front() {
        if (this.isEmpty()) {
            return "No elements in Queue";
        }
        return this.items[0];
    }

    /**
     * Checks if the queue is empty.
     * @returns {boolean} True if the queue is empty, otherwise false.
     */
    isEmpty() {
        return this.items.length === 0;
    }

    /**
     * Returns a string representation of all the elements in the queue.
     * @returns {string} A string containing all elements in the queue, separated by spaces.
     */
    printQueue() {
        return this.items.join(" ");
    }
}

// export default Queue;

// Example usage of the Queue class
let queue = new Queue();

queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);

console.log(queue.printQueue()); // Output: "10 20 30"

queue.dequeue();

console.log(queue.front()); // Output: 20
