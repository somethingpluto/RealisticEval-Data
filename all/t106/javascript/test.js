describe('isBase64Image', () => {
    // Test Case 1: Valid Base64 encoded PNG image
    test('should return true for a valid Base64 encoded PNG image', () => {
        const imageData1 = "question:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA";
        expect(isBase64Image(imageData1)).toBe(true);
    });

    // Test Case 2: Valid Base64 encoded JPEG image
    test('should return true for a valid Base64 encoded JPEG image', () => {
        const imageData2 = "question:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBD";
        expect(isBase64Image(imageData2)).toBe(true);
    });

    // Test Case 3: Invalid Base64 string without proper image MIME type
    test('should return false for a Base64 encoded PDF, not an image', () => {
        const imageData3 = "question:application/pdf;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA";
        expect(isBase64Image(imageData3)).toBe(false);
    });

    // Test Case 4: Invalid string with no Base64 encoding
    test('should return true for a string with valid Base64 image prefix but incorrect Base64 encoding', () => {
        const imageData4 = "question:image/png;base64,ThisIsNotBase64Encoded";
        expect(isBase64Image(imageData4)).toBe(true); // Based on function logic provided in the explanation
    });

    // Test Case 5: Random string without Base64 prefix
    test('should return false for a random string without a Base64 prefix', () => {
        const imageData5 = "This is not a Base64 encoded image string.";
        expect(isBase64Image(imageData5)).toBe(false);
    });
});