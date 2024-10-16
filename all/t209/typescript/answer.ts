class Node {
    data: number;      // Data held by the node
    next: Node | null; // Pointer to the next node in the list

    constructor(value: number) {
        this.data = value;
        this.next = null;
    }
}

class LinkedList {
    private head: Node | null; // Pointer to the first node in the list

    constructor() {
        this.head = null; // Initializes an empty list
    }

    // Method to add a node at the beginning of the list
    insertAtHead(value: number): void {
        const newNode = new Node(value); // Create a new node
        newNode.next = this.head;         // Link the new node to the current head
        this.head = newNode;              // Update the head to the new node
    }

    // Method to add a node at the end of the list
    insertAtTail(value: number): void {
        const newNode = new Node(value);
        if (this.head === null) {
            this.head = newNode; // New node becomes the head if the list is empty
        } else {
            let current = this.head;
            while (current.next !== null) {
                current = current.next; // Traverse to the end of the list
            }
            current.next = newNode; // Link the last node to the new node
        }
    }

    // Method to delete a node with a specific value
    deleteValue(value: number): void {
        if (this.head === null) return; // List is empty, nothing to delete

        // If the head needs to be deleted
        if (this.head.data === value) {
            const temp = this.head;
            this.head = this.head.next; // Update head to the next node
            return; // Delete is handled by garbage collection
        }

        // Traverse to find the node to delete
        let current: Node | null = this.head;
        while (current?.next !== null && current.next.data !== value) {
            current = current.next;
        }

        // If the node was found, delete it
        if (current?.next !== null) {
            const temp = current.next;
            current.next = current.next.next; // Unlink the node from the list
            // Delete is handled by garbage collection
        }
    }

    // Method to search for a value in the list
    search(value: number): boolean {
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
    printList(): void {
        let current = this.head;
        while (current !== null) {
            process.stdout.write(`${current.data} -> `);
            current = current.next;
        }
        console.log("null");
    }
}