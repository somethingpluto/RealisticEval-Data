describe('UniqueDeque', () => {
    let deque: UniqueDeque;

    beforeEach(() => {
        deque = new UniqueDeque();
    });

    test('should add items only once', () => {
        expect(deque.add(1)).toBe(true);
        expect(deque.add(2)).toBe(true);
        expect(deque.add(1)).toBe(false); // Duplicate item
        expect(deque.length).toBe(2);
    });

    test('should delete existing items', () => {
        deque.add(3);
        expect(deque.delete(3)).toBe(true);
        expect(deque.delete(4)).toBe(false); // Non-existing item
        expect(deque.length).toBe(0);
    });

    test('should contain items correctly', () => {
        deque.add(5);
        expect(deque.contains(5)).toBe(true);
        expect(deque.contains(6)).toBe(false); // Non-existing item
    });

    test('should iterate over items', () => {
        deque.add(7);
        deque.add(8);

        const iterator = deque[Symbol.iterator]();
        expect(iterator.next().value).toBe(7);
        expect(iterator.next().value).toBe(8);
        expect(iterator.next().done).toBe(true);
    });
});