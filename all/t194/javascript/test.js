describe('returnString Test Cases', () => {
    // Test Case 1: Copy a non-empty string
    test('should copy a non-empty string', () => {
        const original1 = "Hello, World!";
        const copy1 = returnString(original1);
        expect(copy1).toBe(original1);
    });

    // Test Case 2: Copy an empty string
    test('should copy an empty string', () => {
        const original2 = "";
        const copy2 = returnString(original2);
        expect(copy2).toBe(original2);
    });

    // Test Case 3: Copy a string with special characters
    test('should copy a string with special characters', () => {
        const original3 = "C++ is fun! @#$%^&*()";
        const copy3 = returnString(original3);
        expect(copy3).toBe(original3);
    });

    // Test Case 4: Copy a single character string
    test('should copy a single character string', () => {
        const original4 = "A";
        const copy4 = returnString(original4);
        expect(copy4).toBe(original4);
    });

    // Test Case 5: Passing a null pointer (should throw an exception)
    test('should throw an error when passing null', () => {
        expect(() => returnString(null)).toThrow(Error);
    });
});