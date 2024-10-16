class Node {
    constructor(val) { // Constructor to initialize the node
        this.data = val;   // Data value of the node
        this.next = null;  // Pointer to the next node in the linked list
    }
}

// Queue class
class Queue {
    constructor() { // Constructor to initialize the queue
        this.head = null;  // Pointer to the front of the queue
        this.tail = null;  // Pointer to the end of the queue
    }

    // Destructor to clean up the queue (handled by JavaScript's garbage collector)
    // In JavaScript, we do not need a destructor like in C++
    // So this can be omitted or handled in a different way if necessary

    // Function to check if the queue is empty
    isEmpty() { 
        return this.head === null; // Return true if the queue is empty
    }

    // Function to add an element to the end of the queue
    enqueue(value) {
        const newNode = new Node(value); // Create a new node

        if (this.tail) {
            this.tail.next = newNode; // Link the new node at the end
        } else {
            this.head = newNode; // If the queue is empty, the new node is also the head
        }
        this.tail = newNode; // Update the tail to the new node
    }

    // Function to remove and return the front element of the queue
    dequeue() {
        if (this.isEmpty()) {
            console.error("Queue is empty. Cannot dequeue.");
            return null; // Return null if the queue is empty
        }

        const temp = this.head; // Temporarily store the head node
        const value = this.head.data; // Get the data from the head node
        this.head = this.head.next; // Move head to the next node

        if (this.head === null) {
            this.tail = null; // If the queue becomes empty, update the tail as well
        }

        return value; // Return the dequeued value
    }

    // Function to get the front element without removing it
    front() {
        if (this.isEmpty()) {
            console.error("Queue is empty. Cannot access front.");
            return null; // Return null for invalid access
        }
        return this.head.data; // Return the front value
    }
}