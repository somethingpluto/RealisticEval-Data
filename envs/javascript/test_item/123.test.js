/**
 * Scales the values in an array from one range to another.
 * 
 * @param {number[]} inputArray - The array of input values to be scaled.
 * @param {number} inputMin - The minimum value in the input range.
 * @param {number} inputMax - The maximum value in the input range.
 * @param {number} outputMin - The minimum value in the output range.
 * @param {number} outputMax - The maximum value in the output range.
 * @returns {number[]} - A new array with values scaled to the output range.
 * @throws {Error} - Throws an error if any value in inputArray is outside the range [inputMin, inputMax].
 */
function scaleToRange(inputArray, inputMin, inputMax, outputMin, outputMax) {
    // Validate input values
    for (let value of inputArray) {
        if (value < inputMin || value > inputMax) {
            throw new Error(`Value ${value} is outside the range [${inputMin}, ${inputMax}].`);
        }
    }

    // Calculate the scaling factor
    const scaleFactor = (outputMax - outputMin) / (inputMax - inputMin);

    // Scale the values
    return inputArray.map(value => {
        return outputMin + (value - inputMin) * scaleFactor;
    });
}
describe('scaleToRange function tests', () => {
    test('simple scaling', () => {
        const result = scaleToRange([1, 2, 3, 4, 5], 1, 5, 10, 50);
        expect(result).toEqual([10, 20, 30, 40, 50]);
    });

    test('scaling with negative input range', () => {
        const result = scaleToRange([-5, 0, 5], -5, 5, 0, 100);
        expect(result).toEqual([0, 50, 100]);
    });

    test('scaling with negative output range', () => {
        const result = scaleToRange([0, 50, 100], 0, 100, -100, 100);
        expect(result).toEqual([-100, 0, 100]);
    });

    test('input array containing the same value', () => {
        const result = scaleToRange([2, 2, 2], 1, 3, 0, 10);
        expect(result).toEqual([5, 5, 5]);
    });

    test('input value out of range should throw an error', () => {
        expect(() => {
            scaleToRange([1, 2, 3, 6], 1, 5, 0, 10);
        }).toThrow();
    });
});
