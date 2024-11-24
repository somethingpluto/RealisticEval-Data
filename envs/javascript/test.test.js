function cleanPattern(x, pattern) {
    const inputString = String(x);

    // Create a RegExp object from the pattern
    const regex = new RegExp(pattern);

    // Search for the pattern in the input string
    const match = inputString.match(regex);

    if (match) {
        // Extract the weight value from the first matching group
        const weight = match[1];  // Can also use match[3] if needed

        try {
            // Convert the weight to a float and return it
            const weightValue = parseFloat(weight);
            if (!isNaN(weightValue)) {
                return weightValue;
            } else {
                console.warn(`Warning: Unable to convert '${weight}' to float.`);
                return '';
            }
        } catch (error) {
            // Handle cases where conversion to float fails
            console.warn(`Warning: Unable to convert '${weight}' to float.`);
            return '';
        }
    } else {
        return '';  // Return empty string if no match is found
    }
}
describe('TestCleanPattern', () => {
    let pattern;

    beforeEach(() => {
        // Sets up a common regex pattern for testing
        pattern = /(\d+\.?\d*) kg/;
    });

    it('test_valid_integer_weight', () => {
        // Test case for valid integer weight
        const inputString = "The weight is 25 kg";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe(25.0);
    });

    it('test_valid_float_weight', () => {
        // Test case for valid float weight
        const inputString = "Weight measured at 15.75 kg";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe(15.75);
    });

    it('test_no_weight_found', () => {
        // Test case where no weight is present
        const inputString = "No weight provided.";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe('');
    });

    it('test_invalid_float_conversion', () => {
        // Test case for non-numeric weight
        const inputString = "The weight is thirty kg";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe('');
    });

    it('test_weight_with_extra_text', () => {
        // Test case for weight with additional text
        const inputString = "The total weight is 45.3 kg as per the last measurement.";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe(45.3);
    });
});
