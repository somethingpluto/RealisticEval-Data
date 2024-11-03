describe("Priority Queue - Test Cases", () => {
    let pq;

    beforeEach(() => {
        pq = new PriorityQueue();
    });

    test("Insert and access maximum element", () => {
        pq.push(10);
        pq.push(20);
        pq.push(5);
        pq.push(30);
        pq.push(15);

        expect(pq.top()).toBe(30); // Ensure the max element is 30
    });

    test("Remove maximum element", () => {
        pq.push(10);
        pq.push(20);
        pq.push(5);
        pq.push(30);

        pq.pop(); // Remove 30
        expect(pq.top()).toBe(20); // Now the max should be 20
        pq.pop(); // Remove 20
        expect(pq.top()).toBe(10); // Now the max should be 10
    });

    test("Check empty queue", () => {
        expect(pq.isEmpty()).toBe(true); // Initially empty
        pq.push(10);
        expect(pq.isEmpty()).toBe(false); // Now not empty
        pq.pop();
        expect(pq.isEmpty()).toBe(true); // Back to empty
    });

    test("Pop from empty queue", () => {
        expect(() => pq.pop()).toThrow(Error); // Should throw an error
    });

    test("Access top of empty queue", () => {
        expect(() => pq.top()).toThrow(Error); // Should throw an error
    });

    test("Maintain max-heap property", () => {
        pq.push(3);
        pq.push(1);
        pq.push(4);
        pq.push(2);

        expect(pq.top()).toBe(4); // Ensure max is 4

        pq.pop(); // Remove 4
        expect(pq.top()).toBe(3); // Now max is 3

        pq.push(5); // Add 5
        expect(pq.top()).toBe(5); // Ensure max is now 5
    });
});