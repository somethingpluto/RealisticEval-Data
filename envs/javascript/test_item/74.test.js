/**
 * Converts a decimal number to its binary representation in either 32-bit or 64-bit format.
 *
 * @param {number} decimalValue - The decimal number to convert.
 * @param {number} bitLength - The desired bit length for the binary representation (32 or 64).
 * @returns {string|null} The binary string representation of the decimal number if the bit length
 *                        is valid, otherwise `null`.
 * @throws {Error} Throws an error if the bit length is not 32 or 64.
 */
function convertDecimalToBinary(decimalValue, bitLength) {
  if (bitLength !== 32 && bitLength !== 64) {
    throw new Error('Invalid bit length. Please use 32 or 64.');
  }

  const binaryString = decimalValue.toString(2);

  if (bitLength === 32) {
    return binaryString.padStart(32, '0');
  } else if (bitLength === 64) {
    return binaryString.padStart(64, '0');
  }

  return null;
}
describe('convertDecimalToBinary', () => {
    test('basic 32-bit conversion for 3.14', () => {
        expect(convertDecimalToBinary(3.14, 32)).toBe('01000000010010001111010111000011');
    });

    test('basic 64-bit conversion for 3.14', () => {
        expect(convertDecimalToBinary(3.14, 64)).toBe('0100000000001001000111101011100001010001111010111000010100011111');
    });

    test('advanced 32-bit conversion for 1.5', () => {
        expect(convertDecimalToBinary(1.5, 32)).toBe('00111111110000000000000000000000');
    });

    test('advanced 64-bit conversion for 1.5', () => {
        expect(convertDecimalToBinary(1.5, 64)).toBe('0011111111111000000000000000000000000000000000000000000000000000');
    });
});

