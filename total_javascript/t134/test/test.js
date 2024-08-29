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