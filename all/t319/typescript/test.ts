describe('countDashes', () => {
    test('should return 0 for a string with no dashes', () => {
        const result: number = countDashes('hello world');
        expect(result).toBe(0); // 'hello world' contains no dashes
    });

    test('should return 1 for a string with one dash', () => {
        const result: number = countDashes('hello-world');
        expect(result).toBe(1); // 'hello-world' contains one dash
    });

    test('should return 4 for a string with multiple dashes', () => {
        const result: number = countDashes('a-b-c-d-e');
        expect(result).toBe(4); // 'a-b-c-d-e' contains four dashes
    });

    test('should return 3 for a string with dashes at the beginning and end', () => {
        const result: number = countDashes('-start-end-');
        expect(result).toBe(3); // '-start-end-' contains three dashes
    });

    test('should return 0 for an empty string', () => {
        const result: number = countDashes('');
        expect(result).toBe(0); // An empty string contains no dashes
    });
});