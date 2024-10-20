describe('binarySearchClosest', () => {
    
    test('target present', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 7;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(3); // Target should be found at index 3.
    });

    test('closest element smaller', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 6;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(2); // Closest element should be 5 at index 2.
    });

    test('closest element larger', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 8;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(3); // Closest element should be 7 at index 3.
    });

    test('target smaller than all', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 0;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(0); // Closest element should be 1 at index 0.
    });

    test('target larger than all', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 12;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(5); // Closest element should be 11 at index 5.
    });
});