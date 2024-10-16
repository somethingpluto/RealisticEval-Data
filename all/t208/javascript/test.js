describe("PriorityQueue", () => {
    // Test Case 1: Test insertion and extraction of the minimum element
    test("Insertion and extraction of minimum element", () => {
        const pq = new PriorityQueue();

        // Inserting elements into the priority queue
        pq.insert(5);
        pq.insert(2);
        pq.insert(8);
        pq.insert(1);
        pq.insert(3);

        expect(pq.size()).toBe(5);
        expect(pq.peekMin()).toBe(1);

        // Extracting the minimum element
        expect(pq.extractMin()).toBe(1);
        expect(pq.extractMin()).toBe(2);
        expect(pq.extractMin()).toBe(3);
        expect(pq.extractMin()).toBe(5);
        expect(pq.extractMin()).toBe(8);
        expect(pq.isEmpty()).toBe(true);
    });

    // Test Case 2: Test peekMin operation
    test("Peek minimum element", () => {
        const pq = new PriorityQueue();

        pq.insert(10);
        pq.insert(4);
        pq.insert(15);

        expect(pq.peekMin()).toBe(4);
        expect(pq.size()).toBe(3); // Size should remain the same
        expect(pq.peekMin()).toBe(4); // Peek should not remove the element
    });

    // Test Case 3: Test edge case of extracting from an empty queue
    test("Extract from empty queue", () => {
        const pq = new PriorityQueue();

        expect(() => pq.extractMin()).toThrow(Error);
    });

    // Test Case 4: Test isEmpty function
    test("Check if the priority queue is empty", () => {
        const pq = new PriorityQueue();

        // Newly created queue should be empty
        expect(pq.isEmpty()).toBe(true);

        // Queue should not be empty after insertion
        pq.insert(7);
        expect(pq.isEmpty()).toBe(false);

        // Queue should be empty after extracting all elements
        pq.extractMin();
        expect(pq.isEmpty()).toBe(true);
    });

    // Test Case 5: Test multiple insertions and order of extraction
    test("Multiple insertions and extraction order", () => {
        const pq = new PriorityQueue();

        pq.insert(9);
        pq.insert(4);
        pq.insert(6);
        pq.insert(1);
        pq.insert(8);

        const extractedElements = [];
        while (!pq.isEmpty()) {
            extractedElements.push(pq.extractMin());
        }

        const expectedOrder = [1, 4, 6, 8, 9];
        expect(extractedElements).toEqual(expectedOrder);
    });
});