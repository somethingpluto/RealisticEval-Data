describe('isValidNumber', () => {

    test('should return "Not Numerical" when input is not a number', () => {
        const result = isValidNumber('abc123');
        expect(result).toBe("Not Numerical");
    });

    test('should return "Invalid Length, Must Be Between 5-18" when input length is less than 5', () => {
        const result = isValidNumber('1234');
        expect(result).toBe("Invalid Length, Must Be Between 5-18");
    });

    test('should return "Invalid Length, Must Be Between 5-18" when input length is greater than 18', () => {
        const result = isValidNumber('1234567890123456789');
        expect(result).toBe("Invalid Length, Must Be Between 5-18");
    });

    test('should return true for a valid number within the length range', () => {
        const result = isValidNumber('123456');
        expect(result).toBe(true);
    });

    test('should return "Invalid Input" when an unexpected error occurs', () => {
        // This test simulates an error scenario,
        // which is tricky since the function does not throw errors naturally.
        // Here, we use a mock to simulate this behavior.
        const originalTrim = String.prototype.trim;
        String.prototype.trim = () => { throw new Error(); }; // Force an error

        const result = isValidNumber(' 12345 ');
        expect(result).toBe("Invalid Input");

        // Restore original trim method
        String.prototype.trim = originalTrim;
    });

});
/**
 * Tests whether the input string is a valid number between 5 and 18
 *
 * @param {string} inputNumber - The input string to validate.
 * @returns {string|boolean} - Returns "Not Numerical" if the input is not a number,
 *                             "Invalid Length, Must Be Between 5-18" if the input length
 *                             is not within the required range, true if the input is valid,
 *                             or "Invalid Input" in case of unexpected errors.
 */
function isValidNumber(inputNumber) {
    try {
        const trimmedNumber = inputNumber.trim();

        // Check if the trimmed input is a valid number
        if (isNaN(Number(trimmedNumber))) {
            return "Not Numerical";
        }

        // Check if the number length is between 5 and 18 characters
        if (trimmedNumber.length < 5 || trimmedNumber.length > 18) {
            return "Invalid Length, Must Be Between 5-18";
        }

        return true;
    } catch {
        return "Invalid Input";
    }
}
