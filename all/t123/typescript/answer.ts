function scaleToRange(
    inputArray: number[],
    inputMin: number,
    inputMax: number,
    outputMin: number,
    outputMax: number
): number[] {
    // Ensure all values in inputArray are within the input range
    inputArray.forEach(value => {
        if (value < inputMin || value > inputMax) {
            throw new Error(`Value ${value} in inputArray is outside the range [${inputMin}, ${inputMax}].`);
        }
    });

    const scale = (outputMax - outputMin) / (inputMax - inputMin);

    return inputArray.map(value => ((value - inputMin) * scale) + outputMin);
}