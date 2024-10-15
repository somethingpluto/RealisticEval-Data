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