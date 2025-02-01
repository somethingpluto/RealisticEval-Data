/**
 * Calculates the discount percentage based on the given price and the actual price paid.
 *
 * @param {number} originalPrice - The original price of the item.
 * @param {number} actualPrice - The actual price paid for the item.
 * @returns {number} - The discount percentage, rounded to two decimal places.
 */
function calculateDiscount(originalPrice, actualPrice) {
    if (originalPrice <= 0 || actualPrice <= 0 || actualPrice > originalPrice) {
        throw new Error('Invalid input values');
    }

    const discountPercentage = ((originalPrice - actualPrice) / originalPrice) * 100;
    return Math.round(discountPercentage * 100) / 100;
}
describe('calculateDiscount', () => {
    test('should return 25.00% discount for original price of 100 and actual price of 75', () => {
        expect(calculateDiscount(100, 75)).toBe(25.00);
    });

    test('should return 0.00% discount for original price of 50 and actual price of 50', () => {
        expect(calculateDiscount(50, 50)).toBe(0.00);
    });

    test('should return 100.00% discount for original price of 100 and actual price of 0', () => {
        expect(calculateDiscount(100, 0)).toBe(100.00);
    });

    test('should return 50.00% discount for original price of 200 and actual price of 100', () => {
        expect(calculateDiscount(200, 100)).toBe(50.00);
    });
});
