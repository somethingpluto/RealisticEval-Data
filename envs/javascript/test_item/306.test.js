/**
 * The recipe ID is hashed to produce a price in the specified range
 *
 * @param {string} recipeId - The ID of the recipe to hash.
 * @param {number} [minVal=10] - The minimum value of the price range.
 * @param {number} [maxVal=30] - The maximum value of the price range.
 * @returns {number} - The hashed price, mapped to the specified range with two decimal places.
 */
function getPrice(recipeId, minVal = 10, maxVal = 30) {
    // Convert the recipeId to a hash value
    let hash = 0;
    for (let i = 0; i < recipeId.length; i++) {
        hash = (hash << 5) - hash + recipeId.charCodeAt(i);
        hash |= 0; // Convert to 32bit integer
    }

    // Normalize the hash value to a range between 0 and 1
    const normalizedHash = (hash - (-Math.pow(2, 31))) / (Math.pow(2, 31) - (-Math.pow(2, 31)));

    // Map the normalized hash value to the specified price range
    const price = minVal + (maxVal - minVal) * normalizedHash;

    // Return the price rounded to two decimal places
    return parseFloat(price.toFixed(2));
}
describe('getPrice', () => {
    test('should return a number within the default range for a given recipe ID', () => {
        const price = getPrice('recipe123');
        expect(price).toBeGreaterThanOrEqual(10);
        expect(price).toBeLessThanOrEqual(30);
    });

    test('should return the same price for the same recipe ID', () => {
        const price1 = getPrice('recipe123');
        const price2 = getPrice('recipe123');
        expect(price1).toBe(price2);
    });

    test('should return different prices for different recipe IDs', () => {
        const price1 = getPrice('recipe123');
        const price2 = getPrice('recipe456');
        expect(price1).not.toBe(price2);
    });

    test('should return a price within a custom range', () => {
        const minVal = 20;
        const maxVal = 50;
        const price = getPrice('recipe789', minVal, maxVal);
        expect(price).toBeGreaterThanOrEqual(minVal);
        expect(price).toBeLessThanOrEqual(maxVal);
    });

    test('should handle very long recipe IDs without error', () => {
        const longRecipeId = 'recipe' + 'A'.repeat(1000);
        const price = getPrice(longRecipeId);
        expect(price).toBeGreaterThanOrEqual(10);
        expect(price).toBeLessThanOrEqual(30);
    });
});
