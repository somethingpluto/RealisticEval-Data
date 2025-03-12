// Start of the code context
import { Float32Array, DataView } from 'buffer';

/**
 * Converts an array of floating-point numbers to their hexadecimal representation.
 * ...
 */

function floatsToHex(floats: number[]): string[] {
  return floats.map(float => floatToHex(float));
}

function floatToHex(value: number): string {
  const buffer = new ArrayBuffer(4);
  const view = new DataView(buffer);
  view.setFloat32(0, value);
  return Array.from(new Uint8Array(buffer))
    .map(byte => byte.toString(16).padStart(2, '0'))
    .join('');
}
// End of the code context
describe("floatToHex tests", () => {
    test("Test with positive float 123.456", () => {
        const input = 123.456;
        const expected = "42f6e979";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with negative float -123.456", () => {
        const input = -123.456;
        const expected = "c2f6e979";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with zero", () => {
        const input = 0.0;
        const expected = "00000000";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with small positive float 0.0001", () => {
        const input = 0.0001;
        const expected = "38d1b717";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with large float 1e30", () => {
        const input = 1e30;
        const expected = "7149f2ca";
        expect(floatToHex(input)).toBe(expected);
    });
});
