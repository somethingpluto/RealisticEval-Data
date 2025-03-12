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
    // Validate price
    if (typeof price !== 'string' || isNaN(price)) {
        throw new Error('Invalid price: price must be a valid number string.');
    }

    // Validate discount
    if (typeof discount !== 'string' || isNaN(discount)) {
        throw new Error('Invalid discount: discount must be a valid number string.');
    }

    const priceNum = parseFloat(price);
    const discountNum = parseFloat(discount);

    // Validate discount range
    if (discountNum < 0 || discountNum > 100) {
        throw new Error('Invalid discount: discount must be a percentage value between 0 and 100.');
    }

    // Calculate the final price
    const finalPrice = priceNum * (1 - discountNum / 100);

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
