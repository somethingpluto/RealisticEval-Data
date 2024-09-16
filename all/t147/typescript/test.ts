describe('arrayBufferToString', () => {
    test('should return an empty string for an empty ArrayBuffer', () => {
        const buffer1 = new ArrayBuffer(0);
        const result = arrayBufferToString(buffer1);
        expect(result).toBe(''); // Expected: ""
    });

    test('should return "A" for a buffer containing the character "A"', () => {
        const buffer2 = new TextEncoder().encode("A").buffer;
        const result = arrayBufferToString(buffer2);
        expect(result).toBe('A'); // Expected: "A"
    });

    test('should return "Hello" for a buffer containing the string "Hello"', () => {
        const buffer3 = new TextEncoder().encode("Hello").buffer;
        const result = arrayBufferToString(buffer3);
        expect(result).toBe('Hello'); // Expected: "Hello"
    });

    test('should return "¡Hola!" for a buffer containing the string "¡Hola!"', () => {
        const buffer4 = new TextEncoder().encode("¡Hola!").buffer;
        const result = arrayBufferToString(buffer4);
        expect(result).toBe('¡Hola!'); // Expected: "¡Hola!"
    });

    test('should return "Hello 🌍" for a buffer containing the string "Hello 🌍"', () => {
        const buffer5 = new TextEncoder().encode("Hello 🌍").buffer;
        const result = arrayBufferToString(buffer5);
        expect(result).toBe('Hello 🌍'); // Expected: "Hello 🌍"
    });
});