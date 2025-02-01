/**
 * Converts an ArrayBuffer to a string.
 *
 * @param {ArrayBuffer} buffer - The ArrayBuffer to be converted.
 * @returns {string} The string representation of the ArrayBuffer.
 */
function arrayBufferToString(buffer) {
  // Create a Uint8Array view of the ArrayBuffer
  const uint8Array = new Uint8Array(buffer);

  // Convert the Uint8Array to a string using TextDecoder
  const decoder = new TextDecoder('utf-8');
  return decoder.decode(uint8Array);
}
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

    test('should return the correct string for a buffer containing multiple characters', () => {
        const buffer4 = new TextEncoder().encode("Hello, World!").buffer;
        const result = arrayBufferToString(buffer4);
        expect(result).toBe('Hello, World!'); // Expected: "Hello, World!"
    });

    test('should not modify the input buffer', () => {
        const input = "Test input";
        const buffer8 = new TextEncoder().encode(input).buffer;
        arrayBufferToString(buffer8);
        const result = new TextDecoder().decode(buffer8);
        expect(result).toBe(input); // Check if the buffer content remains unchanged
    });
});
