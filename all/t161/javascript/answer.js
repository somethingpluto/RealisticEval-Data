/**
 * Produces all combinations of numeric arrays for each key in the given map object and returns them as a two-dimensional array
 *
 * @param {Map<string, number[]>} map - A map where each key is a string, and each value is an array of numbers.
 * @returns {number[][]} An array of arrays, where each sub-array is a unique combination of numbers from the Map's values.
 */
function generateCombinations(map) {
    const keys = Array.from(map.keys());
    const values = Array.from(map.values());

    const combinations = [];

    /**
     * Helper function to recursively generate combinations.
     *
     * @param {number[]} currentCombination - The current combination being built.
     * @param {number} currentIndex - The current index in the keys/values arrays.
     */
    function generate(currentCombination, currentIndex) {
        // Base case: If we've reached the end of the keys, push the combination to the combinations array.
        if (currentIndex === keys.length) {
            combinations.push(currentCombination.slice());
            return;
        }

        // Recursively generate combinations for the current key's values.
        const currentValues = values[currentIndex];
        for (const value of currentValues) {
            currentCombination[currentIndex] = value;
            generate(currentCombination, currentIndex + 1);
        }
    }

    // Start the recursive combination generation.
    generate([], 0);
    return combinations;
}