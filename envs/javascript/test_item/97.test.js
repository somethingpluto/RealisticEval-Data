/**
 * Realize the basic functions of the question structure queue: enqueue, dequeue, get the front element of the queue, judge whether it is empty, output all elements.
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
        let str = "";
        for (let i = 0; i < this.items.length; i++) {
            str += this.items[i] + " ";
        }
        return str.trim();
    }
}
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
