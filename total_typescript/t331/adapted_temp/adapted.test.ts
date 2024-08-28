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
/**
 * Calculates the final price after applying a discount to the original price.
 * Both price and discount are expected as strings and should represent valid numbers.
 * The discount should be a percentage value between 0 and 100.
 *
 * @param price The original price as a string.
 * @param discount The discount percentage as a string.
 * @returns The final price after applying the discount, rounded to two decimal places.
 * @throws Will throw an error if price or discount aren't valid numbers or if the discount is out of the expected range.
 */
function calculateFinalPrice(price: string, discount: string): number {
    const priceValue = parseFloat(price);
    const discountValue = parseFloat(discount);

    if (isNaN(priceValue) || isNaN(discountValue)) {
        throw new Error('Invalid price or discount value.');
    }

    if (discountValue < 0 || discountValue > 100) {
        throw new Error('Discount percentage must be between 0 and 100.');
    }

    const discountAmount = priceValue * discountValue / 100;
    const finalPrice = priceValue - discountAmount;

    return Math.round(finalPrice * 100) / 100;
}