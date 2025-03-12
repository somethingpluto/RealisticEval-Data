import { v4 as uuidv4 } from 'uuid';

class Node {
    // ... (rest of the Node class remains unchanged)

    // Adding a unique identifier to each node
    id: string;

    constructor(value: number) {
        this.data = value;
        this.next = null;
        this.id = uuidv4(); // Assign a unique ID to the node
    }
}

class LinkedList {
    // ... (rest of the LinkedList class remains unchanged)

    // Method to insert a node at a specific position
    insertAtPosition(value: number, position: number): void {
        if (position < 0) {
            throw new Error('Position must be a non-negative integer');
        }

        const newNode = new Node(value);

        if (position === 0) {
            newNode.next = this.head;
            this.head = newNode;
        } else {
            let current = this.head;
            let previous: Node | null = null;
            let index = 0;

            while (current !== null && index < position) {
                previous = current;
                current = current.next;
                index++;
            }

            if (index === position) {
                newNode.next = current;
                previous.next = newNode;
            } else {
                throw new Error('Position out of bounds');
            }
        }
    }

    // Method to reverse the linked list
    reverseList(): void {
        let prev: Node | null = null;
        let current = this.head;
        let next: Node | null = null;

        while (current !== null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }

        this.head = prev;
    }
}
describe('LinkedList operations', () => {

    test('Insertion at the head', () => {
        const list = new LinkedList();
        list.insertAtHead(10);
        list.insertAtHead(20);
        list.insertAtHead(30);

        const output = list.printList(); // Capture the output if implemented
        expect(list.search(10)).toBe(true);
        expect(list.search(20)).toBe(true);
        expect(list.search(30)).toBe(true);
        expect(list.search(40)).toBe(false);
    });

    test('Insertion at the tail', () => {
        const list = new LinkedList();
        list.insertAtTail(1);
        list.insertAtTail(2);
        list.insertAtTail(3);

        const output = list.printList(); // Capture the output if implemented
        expect(list.search(1)).toBe(true);
        expect(list.search(2)).toBe(true);
        expect(list.search(3)).toBe(true);
        expect(list.search(4)).toBe(false);
    });

    test('Deletion of elements', () => {
        const list = new LinkedList();
        list.insertAtHead(5);
        list.insertAtHead(10);
        list.insertAtHead(15);

        list.deleteValue(10);
        const output = list.printList(); // Capture the output if implemented
        expect(list.search(10)).toBe(false);
        expect(list.search(15)).toBe(true);
        expect(list.search(5)).toBe(true);

        list.deleteValue(15);
        expect(list.printList()).toBe('5 -> null'); // Adjust based on printList implementation
        expect(list.search(15)).toBe(false);
        expect(list.search(5)).toBe(true);

        list.deleteValue(5);
        expect(list.printList()).toBe('null'); // Adjust based on printList implementation
        expect(list.search(5)).toBe(false);
    });

    test('Search functionality', () => {
        const list = new LinkedList();
        list.insertAtTail(100);
        list.insertAtTail(200);
        list.insertAtTail(300);

        expect(list.search(100)).toBe(true);
        expect(list.search(200)).toBe(true);
        expect(list.search(300)).toBe(true);
        expect(list.search(400)).toBe(false);
    });

    test('Edge case: Empty list', () => {
        const list = new LinkedList();

        expect(list.search(1)).toBe(false);  // Searching in an empty list
        list.deleteValue(1);                  // Deleting from an empty list should not crash
        const output = list.printList();      // Expected: 'null' (still empty)
        expect(output).toBe('null');          // Adjust based on printList implementation
    });
});
