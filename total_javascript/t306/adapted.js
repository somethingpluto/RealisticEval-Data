/**
 * The recipe ID is hashed to produce a price in the specified range
 *
 * @param {string} recipeId - The ID of the recipe to hash.
 * @param {number} [minVal=10] - The minimum value of the price range.
 * @param {number} [maxVal=30] - The maximum value of the price range.
 * @returns {number} - The hashed price, mapped to the specified range with two decimal places.
 */
function getPrice(recipeId, minVal = 10, maxVal = 30) {
    let hash = 0;

    // Generate a hash from the recipe ID
    for (let i = 0; i < recipeId.length; i++) {
        const char = recipeId.charCodeAt(i);
        hash = (hash << 5) - hash + char; // Equivalent to hash * 31 + char
        hash |= 0; // Ensure the result is a 32-bit integer
    }

    // Convert the hash to a positive value
    const decimalValue = Math.abs(hash);

    // Map the decimal value to the specified price range
    const mappedValue = (decimalValue % ((maxVal - minVal) * 100)) / 100 + minVal;

    // Ensure the final value has exactly two decimal places
    const finalValue = Math.round(mappedValue * 100) / 100;

    return finalValue;
}

module.exports = getPrice;
