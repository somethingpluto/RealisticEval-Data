/**
 * Calculates the discount percentage based on the given price and the actual price paid.
 *
 * @param {number} originalPrice - The original price of the item.
 * @param {number} actualPrice - The actual price paid for the item.
 * @returns {number} - The discount percentage, rounded to two decimal places.
 */
function calculateDiscount(originalPrice: number, actualPrice: number): number {
    // Validate input
    if (originalPrice <= 0) {
        throw new Error('Original price must be greater than zero.');
    }
    if (actualPrice < 0) {
        throw new Error('Actual price cannot be negative.');
    }

    // Calculate the discount
    const discountAmount = originalPrice - actualPrice;
    const discountPercentage = (discountAmount / originalPrice) * 100;

    // Return the discount percentage, rounded to two decimal places
    return parseFloat(discountPercentage.toFixed(2));
}