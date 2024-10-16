describe("PriorityQueue", () => {
    // Test Case 1: Test insertion and extraction of the minimum element
    describe("Insertion and extraction of minimum element", () => {
        let pq: PriorityQueue;

        beforeEach(() => {
            pq = new PriorityQueue();
        });

        test("Inserting elements into the priority queue", () => {
            pq.insert(5);
            pq.insert(2);
            pq.insert(8);
            pq.insert(1);
            pq.insert(3);

            expect(pq.size()).toBe(5);
            expect(pq.peekMin()).toBe(1);
        });

        test("Extracting the minimum element", () => {
            pq.insert(5);
            pq.insert(2);
            pq.insert(8);
            pq.insert(1);
            pq.insert(3);

            expect(pq.extractMin()).toBe(1);
            expect(pq.extractMin()).toBe(2);
            expect(pq.extractMin()).toBe(3);
            expect(pq.extractMin()).toBe(5);
            expect(pq.extractMin()).toBe(8);
            expect(pq.isEmpty()).toBe(true);
        });
    });

    // Test Case 2: Test peekMin operation
    describe("Peek minimum element", () => {
        let pq: PriorityQueue;

        beforeEach(() => {
            pq = new PriorityQueue();
        });

        test("Peeking at the minimum element without extraction", () => {
            pq.insert(10);
            pq.insert(4);
            pq.insert(15);

            expect(pq.peekMin()).toBe(4);
            expect(pq.size()).toBe(3); // Size should remain the same
            expect(pq.peekMin()).toBe(4); // Peek should not remove the element
        });
    });

    // Test Case 3: Test edge case of extracting from an empty queue
    describe("Extract from empty queue", () => {
        let pq: PriorityQueue;

        beforeEach(() => {
            pq = new PriorityQueue();
        });

        test("Attempting to extract from an empty queue should throw an exception", () => {
            expect(() => pq.extractMin()).toThrow(Error); // Adjusted to throw generic Error
        });
    });

    // Test Case 4: Test isEmpty function
    describe("Check if the priority queue is empty", () => {
        let pq: PriorityQueue;

        beforeEach(() => {
            pq = new PriorityQueue();
        });

        test("Newly created queue should be empty", () => {
            expect(pq.isEmpty()).toBe(true);
        });

        test("Queue should not be empty after insertion", () => {
            pq.insert(7);
            expect(pq.isEmpty()).toBe(false);
        });

        test("Queue should be empty after extracting all elements", () => {
            pq.insert(7);
            pq.extractMin();
            expect(pq.isEmpty()).toBe(true);
        });
    });

    // Test Case 5: Test multiple insertions and order of extraction
    describe("Multiple insertions and extraction order", () => {
        let pq: PriorityQueue;

        beforeEach(() => {
            pq = new PriorityQueue();
        });

        test("Inserting multiple elements and checking extraction order", () => {
            pq.insert(9);
            pq.insert(4);
            pq.insert(6);
            pq.insert(1);
            pq.insert(8);

            const extractedElements: number[] = [];
            while (!pq.isEmpty()) {
                extractedElements.push(pq.extractMin());
            }

            const expectedOrder = [1, 4, 6, 8, 9];
            expect(extractedElements).toEqual(expectedOrder);
        });
    });
});