describe('isValidUserName', () => {

    test('should return "Invalid Length, Must Be Between 5-16" when input length is less than 5', () => {
        const result = isValidUserName('John');
        expect(result).toBe("Invalid Length, Must Be Between 5-16");
    });

    test('should return "Invalid Length, Must Be Between 5-16" when input length is greater than 16', () => {
        const result = isValidUserName('ThisUserNameIsTooLong');
        expect(result).toBe("Invalid Length, Must Be Between 5-16");
    });

    test('should return "Name Can Only Contain Letters, Numbers, and White Space" when input contains invalid characters', () => {
        const result = isValidUserName('User@Name!');
        expect(result).toBe("Name Can Only Contain Letters, Numbers, and White Space");
    });

    test('should return true for a valid username within the length range and containing only allowed characters', () => {
        const result = isValidUserName('JohnDoe123');
        expect(result).toBe(true);
    });

    test('should return "Invalid Input" when an unexpected error occurs', () => {
        // This test simulates an error scenario,
        // which is tricky since the function does not throw errors naturally.
        // Here, we use a mock to simulate this behavior.
        const originalTrim = String.prototype.trim;
        String.prototype.trim = () => { throw new Error(); }; // Force an error

        const result = isValidUserName(' JohnDoe ');
        expect(result).toBe("Invalid Input");

        // Restore original trim method
        String.prototype.trim = originalTrim;
    });

});
/**
 * Checks whether the username is a string of length 5 to 16 that contains only alphanumeric Spaces
 *
 * @param {string} username - The input string to validate as a username.
 * @returns {string|boolean} - Returns "Invalid Length, Must Be Between 5-16" if the input length
 *                             is not within the required range, "Name Can Only Contain Letters, Numbers, and White Space"
 *                             if the input contains invalid characters, true if the input is valid,
 *                             or "Invalid Input" in case of unexpected errors.
 */
function isValidUserName(username) {
    try {
        const trimmedName = username.trim();

        // Check if the trimmed input length is between 5 and 16 characters
        if (trimmedName.length < 5 || trimmedName.length > 16) {
            return "Invalid Length, Must Be Between 5-16";
        }

        // Regular expression to validate that the name contains only letters, numbers, and white space
        const validNameRegex = /^[a-zA-Z0-9\s]+$/;

        // Check if the name matches the allowed pattern
        if (!validNameRegex.test(trimmedName)) {
            return "Name Can Only Contain Letters, Numbers, and White Space";
        }

        return true;
    } catch {
        return "Invalid Input";
    }
}
