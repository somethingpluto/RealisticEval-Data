describe('calculateFinalPrice', () => {
    test('should calculate the final price correctly with valid inputs', () => {
        const result = calculateFinalPrice('200', '10');
        expect(result).toBe(180);
    });

    test('should return the original price when the discount is 0%', () => {
        const result = calculateFinalPrice('150', '0');
        expect(result).toBe(150);
    });

    test('should return zero when the discount is 100%', () => {
        const result = calculateFinalPrice('100', '100');
        expect(result).toBe(0);
    });

    test('should throw an error for invalid numerical input', () => {
        expect(() => calculateFinalPrice('abc', '10')).toThrow('Invalid price or discount value.');
        expect(() => calculateFinalPrice('100', 'xyz')).toThrow('Invalid price or discount value.');
    });

    test('should throw an error when discount is out of range', () => {
        expect(() => calculateFinalPrice('100', '-1')).toThrow('Discount percentage must be between 0 and 100.');
        expect(() => calculateFinalPrice('100', '101')).toThrow('Discount percentage must be between 0 and 100.');
    });
});