class Queue<T> {
    private items: T[];

    constructor() {
        this.items = [];
    }

    /**
     * Adds an element to the end of the queue.
     * @param element - The element to be added to the queue.
     */
    enqueue(element: T): void {
        this.items.push(element);
    }

    /**
     * Removes and returns the element from the front of the queue.
     * @returns The removed element from the front of the queue, or "Underflow" if the queue is empty.
     */
    dequeue(): T | string {
        if (this.isEmpty()) {
            return "Underflow";
        }
        return this.items.shift()!;
    }

    /**
     * Returns the front element of the queue without removing it.
     * @returns The front element of the queue, or "No elements in Queue" if the queue is empty.
     */
    front(): T | string {
        if (this.isEmpty()) {
            return "No elements in Queue";
        }
        return this.items[0];
    }

    /**
     * Checks if the queue is empty.
     * @returns True if the queue is empty, otherwise false.
     */
    isEmpty(): boolean {
        return this.items.length === 0;
    }

    /**
     * Returns a string representation of all the elements in the queue.
     * @returns A string containing all elements in the queue, separated by spaces.
     */
    printQueue(): string {
        return this.items.join(" ");
    }
}