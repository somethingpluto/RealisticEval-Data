describe("MaxHeap Operations", () => {
    let maxHeap: MaxHeap;

    beforeEach(() => {
        maxHeap = new MaxHeap(); // Initialize a new MaxHeap before each test
    });

    test("Initial state of the heap", () => {
        expect(maxHeap.isEmpty()).toBe(true);
        expect(maxHeap.size()).toBe(0);
    });

    test("Insert elements into the heap", () => {
        maxHeap.insert(10);
        maxHeap.insert(20);
        maxHeap.insert(5);

        expect(maxHeap.isEmpty()).toBe(false);
        expect(maxHeap.size()).toBe(3);
        expect(maxHeap.getMax()).toBe(20); // The maximum should be 20
    });

    test("Extract maximum element from the heap", () => {
        maxHeap.insert(10);
        maxHeap.insert(30);
        maxHeap.insert(20);

        const maxElement = maxHeap.extractMax();
        expect(maxElement).toBe(30); // The maximum extracted should be 30
        expect(maxHeap.getMax()).toBe(20); // The next maximum should be 20
        expect(maxHeap.size()).toBe(2); // Size should be 2 after extraction
    });

    test("Heap should maintain max heap property after multiple operations", () => {
        maxHeap.insert(15);
        maxHeap.insert(10);
        maxHeap.insert(30);
        maxHeap.insert(20);
        maxHeap.insert(25);

        // Current max should be 30
        expect(maxHeap.getMax()).toBe(30);

        maxHeap.extractMax(); // Remove 30
        // After removal, the new max should be 25
        expect(maxHeap.getMax()).toBe(25);

        maxHeap.extractMax(); // Remove 25
        // After removal, the new max should be 20
        expect(maxHeap.getMax()).toBe(20);

        // The size of the heap should be 3 now
        expect(maxHeap.size()).toBe(3);
    });
});