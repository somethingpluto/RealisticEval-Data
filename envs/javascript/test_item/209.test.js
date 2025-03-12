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
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
    }

    // Method to add a node at the end of the list
    insertAtTail(value) {
        const newNode = new Node(value);
        if (this.head === null) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next !== null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    // Method to delete a node with a specific value
    deleteValue(value) {
        if (this.head === null) return;

        if (this.head.data === value) {
            this.head = this.head.next;
            return;
        }

        let current = this.head;
        while (current.next !== null) {
            if (current.next.data === value) {
                current.next = current.next.next;
                return;
            }
            current = current.next;
        }
    }

    // Method to search for a value in the list
    search(value) {
        let current = this.head;
        while (current !== null) {
            if (current.data === value) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    // Method to print all elements in the list
    printList() {
        let current = this.head;
        while (current !== null) {
            console.log(current.data);
            current = current.next;
        }
    }
}
describe("LinkedList operations", () => {
    
    test("Insertion at the head", () => {
        const list = new LinkedList();
        list.insertAtHead(10);
        list.insertAtHead(20);
        list.insertAtHead(30);

        console.log = jest.fn(); // Mock console.log
        list.printList(); // Expected: 30 -> 20 -> 10 -> null

        expect(list.search(10)).toBe(true);
        expect(list.search(20)).toBe(true);
        expect(list.search(30)).toBe(true);
        expect(list.search(40)).toBe(false);
    });

    test("Insertion at the tail", () => {
        const list = new LinkedList();
        list.insertAtTail(1);
        list.insertAtTail(2);
        list.insertAtTail(3);

        console.log = jest.fn(); // Mock console.log
        list.printList(); // Expected: 1 -> 2 -> 3 -> null

        expect(list.search(1)).toBe(true);
        expect(list.search(2)).toBe(true);
        expect(list.search(3)).toBe(true);
        expect(list.search(4)).toBe(false);
    });

    test("Deletion of elements", () => {
        const list = new LinkedList();
        list.insertAtHead(5);
        list.insertAtHead(10);
        list.insertAtHead(15);

        list.deleteValue(10);
        console.log = jest.fn(); // Mock console.log
        list.printList(); // Expected: 15 -> 5 -> null

        expect(list.search(10)).toBe(false);
        expect(list.search(15)).toBe(true);
        expect(list.search(5)).toBe(true);

        list.deleteValue(15);
        list.printList(); // Expected: 5 -> null

        expect(list.search(15)).toBe(false);
        expect(list.search(5)).toBe(true);

        list.deleteValue(5);
        list.printList(); // Expected: null

        expect(list.search(5)).toBe(false);
    });

    test("Search functionality", () => {
        const list = new LinkedList();
        list.insertAtTail(100);
        list.insertAtTail(200);
        list.insertAtTail(300);

        expect(list.search(100)).toBe(true);
        expect(list.search(200)).toBe(true);
        expect(list.search(300)).toBe(true);
        expect(list.search(400)).toBe(false);
    });

    test("Edge case: Empty list", () => {
        const list = new LinkedList();

        expect(list.search(1)).toBe(false);  // Searching in an empty list
        list.deleteValue(1);                  // Deleting from an empty list should not crash
        console.log = jest.fn(); // Mock console.log
        list.printList();          // Expected: null (still empty)
    });
});
