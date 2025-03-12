// Start of the code context
import { isPortInRange } from './portValidator';

/**
 * Checks if the provided port number is within the valid range of TCP/UDP ports.
 * Valid TCP/UDP port numbers range from 1 to 65535.
 *
 * @param {number} port - The port number to verify.
 * @returns {boolean} Returns true if the port number is valid, false otherwise.
 */
function isValidPortNumber(port: number): boolean {
    return isPortInRange(port);
}
// End of the code context
describe('isValidPortNumber', () => {
    test('returns true for a valid port number in the middle of the range', () => {
        expect(isValidPortNumber(8080)).toBe(true);
    });

    test('returns true for the lowest valid port number', () => {
        expect(isValidPortNumber(1)).toBe(true);
    });

    test('returns true for the highest valid port number', () => {
        expect(isValidPortNumber(65535)).toBe(true);
    });

    test('returns false for a port number below the valid range', () => {
        expect(isValidPortNumber(0)).toBe(false);
    });

    test('returns false for a port number above the valid range', () => {
        expect(isValidPortNumber(65536)).toBe(false);
    });
});
