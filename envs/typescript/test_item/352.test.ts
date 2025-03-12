import { Buffer } from 'buffer';

/**
 * Converts a hexadecimal string into a byte array.
 * ...
 */

function hexStringToByteArray(hexStr: string): Uint8Array {
  // Ensure the string has an even length by adding a leading zero if necessary
  if (hexStr.length % 2 !== 0) {
    hexStr = '0' + hexStr;
  }

  // Use Buffer.from to convert the hex string to a Buffer and then to a Uint8Array
  return new Uint8Array(Buffer.from(hexStr, 'hex'));
}
describe('hexStringToByteArray', () => {
    test('should correctly convert a normal hex string', () => {
        const hexStr = "1a3f";
        const expected = new Uint8Array([0x1A, 0x3F]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });

    test('should handle odd-length hex strings by prepending zero', () => {
        const hexStr = "123";
        const expected = new Uint8Array([0x01, 0x23]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });

    test('should return an empty array for an empty string', () => {
        const hexStr = "";
        const expected = new Uint8Array(0);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });

    test('should correctly handle hex strings with uppercase letters', () => {
        const hexStr = "1A3F";
        const expected = new Uint8Array([0x1A, 0x3F]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });
});
