describe('countNumbers', () => {
    test('should return the correct count for a string with multiple numbers', () => {
        const result: number = countNumbers('There are 123 numbers in this string.');
        expect(result).toBe(3); // '123' contains three numeric characters
    });

    test('should return 0 for a string with no numbers', () => {
        const result: number = countNumbers('No numbers here!');
        expect(result).toBe(0); // No numeric characters in 'No numbers here!'
    });

    test('should return the correct count for a string with mixed characters', () => {
        const result: number = countNumbers('Room 101 and Room 102');
        expect(result).toBe(6); // '101' and '102' together contain six numeric characters
    });

    test('should return the correct count for a string with only numbers', () => {
        const result: number = countNumbers('1234567890');
        expect(result).toBe(10); // '1234567890' contains ten numeric characters
    });

    test('should return 0 for an empty string', () => {
        const result: number = countNumbers('');
        expect(result).toBe(0); // An empty string contains no numeric characters
    });
});