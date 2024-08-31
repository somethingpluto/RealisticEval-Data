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
function scaleToRange(inputArray, inputMin, inputMax, outputMin, outputMax) {
    // Ensure all values in inputArray are within the input range
    inputArray.forEach(value => {
        if (value < inputMin || value > inputMax) {
            throw new Error(`Value ${value} in inputArray is outside the range [${inputMin}, ${inputMax}].`);
        }
    });

    const scale = (outputMax - outputMin) / (inputMax - inputMin);
    
    return inputArray.map(value => ((value - inputMin) * scale) + outputMin);
}
