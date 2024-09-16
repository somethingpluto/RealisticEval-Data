/**
 * realize the basic functions of the question structure queue: enqueue, dequeue, get the front element of the queue, judge whether it is empty, output all elements
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
