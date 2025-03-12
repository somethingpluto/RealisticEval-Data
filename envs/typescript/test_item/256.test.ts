// ... (previous code for context)
function bitsToBytes(bits: number[]): Uint8Array {
  if (!Array.isArray(bits) || bits.some(bit => bit !== 0 && bit !== 1)) {
    throw new Error('Input must be an array of binary bits (0 or 1).');
  }
  // ... (rest of the function remains unchanged)
}

// ... (rest of the code for context)
describe('TestBitsToBytes', () => {
  it('test_exact_multiple_of_eight', () => {
    /** Test bit arrays that are exact multiples of 8 bits. */
    const bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1];
    const expected = new Uint8Array([0b10110010, 0b01001111]);
    const result = bitsToBytes(bits);
    expect(result).toEqual(expected);
  });

  it('test_incomplete_byte_discarded', () => {
    /** Test bit arrays where the last bits do not make up a full byte. */
    const bits = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]; // Last two bits should be discarded
    const expected = new Uint8Array([0b10110010]);
    const result = bitsToBytes(bits);
    expect(result).toEqual(expected);
  });

  it('test_empty_bit_array', () => {
    /** Test an empty bit array. */
    const bits = [];
    const expected = new Uint8Array([]);
    const result = bitsToBytes(bits);
    expect(result).toEqual(expected);
  });

  it('test_single_full_byte', () => {
    /** Test bit arrays that exactly make one byte. */
    const bits = [1, 1, 1, 1, 1, 1, 1, 1]; // Represents the byte 0xFF
    const expected = new Uint8Array([0xFF]);
    const result = bitsToBytes(bits);
    expect(result).toEqual(expected);
  });

  it('test_no_bits_discarded', () => {
    /** Test bit arrays with multiple of 8 bits and no extra bits. */
    const bits = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1];
    const expected = new Uint8Array([0xCC, 0x77]); // Corrected the second byte from 0xB7 to 0x77
    const result = bitsToBytes(bits);
    expect(result).toEqual(expected);
  });
});
