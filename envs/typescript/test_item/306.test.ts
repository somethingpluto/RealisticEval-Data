import { createHash } from 'crypto';

/**
 * The recipe ID is hashed to produce a price in the specified range
 *
 * @param {string} recipeId - The ID of the recipe to hash.
 * @param {number} [minVal=10] - The minimum value of the price range.
 * @param {number} [maxVal=30] - The maximum value of the price range.
 * @returns {number} - The hashed price, mapped to the specified range with two decimal places.
 */
function getPrice(recipeId: string, minVal: number = 10, maxVal: number = 30): number {
  const hash = createHash('sha256').update(recipeId).digest('hex');
  const hashInt = parseInt(hash, 16);
  const range = maxVal - minVal;
  const normalized = hashInt % range;
  const price = minVal + (normalized / (2 ** 256 - 1)) * range;
  return parseFloat(price.toFixed(2));
}
describe('getPrice', () => {
    test('should return a number within the default range for a given recipe ID', () => {
        const price: number = getPrice('recipe123');
        expect(price).toBeGreaterThanOrEqual(10);
        expect(price).toBeLessThanOrEqual(30);
    });

    test('should return the same price for the same recipe ID', () => {
        const price1: number = getPrice('recipe123');
        const price2: number = getPrice('recipe123');
        expect(price1).toBe(price2);
    });

    test('should return different prices for different recipe IDs', () => {
        const price1: number = getPrice('recipe123');
        const price2: number = getPrice('recipe456');
        expect(price1).not.toBe(price2);
    });

    test('should return a price within a custom range', () => {
        const minVal: number = 20;
        const maxVal: number = 50;
        const price: number = getPrice('recipe789', minVal, maxVal);
        expect(price).toBeGreaterThanOrEqual(minVal);
        expect(price).toBeLessThanOrEqual(maxVal);
    });

    test('should handle very long recipe IDs without error', () => {
        const longRecipeId: string = 'recipe' + 'A'.repeat(1000);
        const price: number = getPrice(longRecipeId);
        expect(price).toBeGreaterThanOrEqual(10);
        expect(price).toBeLessThanOrEqual(30);
    });
});
