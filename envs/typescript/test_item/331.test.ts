// ... (previous code for context)

function calculateFinalPrice(price: string, discount: string): number {
    // ... (existing code)

    // New code to handle negative prices
    if (parseFloat(price) < 0) {
        throw new Error('Price cannot be negative.');
    }

    // ... (existing code)
}

// ... (rest of the existing code)
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
});
