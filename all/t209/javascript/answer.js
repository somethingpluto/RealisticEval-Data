// Node structure for the linked list
class Node {
    constructor(value) { // Constructor to initialize a new node with given data
        this.data = value; // Data held by the node
        this.next = null;  // Pointer to the next node in the list
    }
}

// LinkedList class definition
class LinkedList {
    constructor() {
        this.head = null; // Pointer to the first node in the list
    }

    // Method to add a node at the beginning of the list
    insertAtHead(value) {
        const newNode = new Node(value); // Create a new node
        newNode.next = this.head;         // Link the new node to the current head
        this.head = newNode;              // Update the head to the new node
    }

    // Method to add a node at the end of the list
    insertAtTail(value) {
        const newNode = new Node(value);
        if (this.head === null) {
            this.head = newNode; // If the list is empty, new node becomes the head
        } else {
            let current = this.head;
            while (current.next !== null) {
                current = current.next; // Traverse to the end of the list
            }
            current.next = newNode; // Link the last node to the new node
        }
    }

    // Method to delete a node with a specific value
    deleteValue(value) {
        if (this.head === null) return; // List is empty, nothing to delete

        // If the head needs to be deleted
        if (this.head.data === value) {
            const temp = this.head;
            this.head = this.head.next; // Update head to the next node
            return; // JavaScript handles memory management, no need to delete
        }

        // Traverse to find the node to delete
        let current = this.head;
        while (current.next !== null && current.next.data !== value) {
            current = current.next;
        }

        // If the node was found, delete it
        if (current.next !== null) {
            const temp = current.next;
            current.next = current.next.next; // Unlink the node from the list
            // JavaScript handles memory management, no need to delete
        }
    }

    // Method to search for a value in the list
    search(value) {
        let current = this.head;
        while (current !== null) {
            if (current.data === value) {
                return true; // Value found
            }
            current = current.next;
        }
        return false; // Value not found
    }

    // Method to print all elements in the list
    printList() {
        let current = this.head;
        while (current !== null) {
            process.stdout.write(current.data + " -> "); // Print data
            current = current.next;
        }
        console.log("null"); // End of the list
    }
}