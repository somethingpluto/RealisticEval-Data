class Node {
    data: number;      // Data held by the node
    next: Node | null; // Pointer to the next node in the list

    // Constructor to initialize a new node with given data
    constructor(value: number) {
        this.data = value;
        this.next = null;
    }
}

// LinkedList class definition
class LinkedList {
    // Method to add a node at the beginning of the list
    insertAtHead(value: number): void {
        // Implementation goes here
    }

    // Method to add a node at the end of the list
    insertAtTail(value: number): void {
        // Implementation goes here
    }

    // Method to delete a node with a specific value
    deleteValue(value: number): void {
        // Implementation goes here
    }

    // Method to search for a value in the list
    search(value: number): boolean {
        // Implementation goes here
        return false; // Placeholder return
    }

    // Method to print all elements in the list
    printList(): void {
        // Implementation goes here
    }
}