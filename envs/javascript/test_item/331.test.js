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
function calculateFinalPrice(price, discount) {
    // Validate that price and discount are valid numbers
    const priceNum = parseFloat(price);
    const discountNum = parseFloat(discount);

    if (isNaN(priceNum) || isNaN(discountNum)) {
        throw new Error('Price and discount must be valid numbers.');
    }

    // Validate that the discount is between 0 and 100
    if (discountNum < 0 || discountNum > 100) {
        throw new Error('Discount must be between 0 and 100.');
    }

    // Calculate the discount amount
    const discountAmount = priceNum * (discountNum / 100);

    // Calculate the final price
    const finalPrice = priceNum - discountAmount;

    // Return the final price rounded to two decimal places
    return finalPrice.toFixed(2);
}
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
