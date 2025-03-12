/**
 * Converts an array of binary bits to an array of bytes. Traverses through each bit,
 * composing these bits into bytes, forming a byte every 8 bits, and then storing these
 * bytes in an array and returning it. If the length of the bit array is not a multiple
 * of 8, the last incomplete byte will be discarded.
 *
 * @param {Array<number>} bits - The input array of bits (each element should be 0 or 1).
 * @returns {Uint8Array} An array of bytes constructed from the bits.
 */
function bitsToBytes(bits) {
    // Calculate the number of complete bytes that can be formed
    const numBytes = Math.floor(bits.length / 8);
    
    // Create a new Uint8Array to store the bytes
    const bytes = new Uint8Array(numBytes);
    
    // Loop through each byte
    for (let i = 0; i < numBytes; i++) {
        let byteValue = 0;
        
        // Loop through the 8 bits of the current byte
        for (let j = 0; j < 8; j++) {
            // Calculate the bit position in the bits array
            const bitIndex = i * 8 + j;
            
            // Shift the current byte value left by 1 and add the current bit
            byteValue = (byteValue << 1) | bits[bitIndex];
        }
        
        // Store the constructed byte in the bytes array
        bytes[i] = byteValue;
    }
    
    return bytes;
}
describe('TestBitsToBytes', () => {
    describe('test_exact_multiple_of_eight', () => {
        it('should correctly convert bit arrays that are exact multiples of 8 bits', () => {
            const bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1];
            const expected = new Uint8Array([0b10110010, 0b01001111]);
            const result = bitsToBytes(bits);
            expect(result).toEqual(expected);
        });
    });

    describe('test_incomplete_byte_discarded', () => {
        it('should discard the last incomplete byte', () => {
            const bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]; // Last two bits should be discarded
            const expected = new Uint8Array([0b10110010]);
            const result = bitsToBytes(bits);
            expect(result).toEqual(expected);
        });
    });

    describe('test_empty_bit_array', () => {
        it('should handle an empty bit array', () => {
            const bits = [];
            const expected = new Uint8Array([]);
            const result = bitsToBytes(bits);
            expect(result).toEqual(expected);
        });
    });

    describe('test_single_full_byte', () => {
        it('should correctly convert bit arrays that exactly make one byte', () => {
            const bits = [1, 1, 1, 1, 1, 1, 1, 1]; // Represents the byte 0xFF
            const expected = new Uint8Array([0xFF]);
            const result = bitsToBytes(bits);
            expect(result).toEqual(expected);
        });
    });

    describe('test_no_bits_discarded', () => {
        it('should correctly convert bit arrays with multiple of 8 bits and no extra bits', () => {
            const bits = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1];
            const expected = new Uint8Array([0xCC, 0x77]); // Corrected the second byte from 0xB7 to 0x77
            const result = bitsToBytes(bits);
            expect(result).toEqual(expected);
        });
    });
});
