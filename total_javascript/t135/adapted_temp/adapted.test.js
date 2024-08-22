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

    test('throws TypeError for non-integer values', () => {
        expect(() => isValidPortNumber('3000')).toThrow(TypeError);
        expect(() => isValidPortNumber(300.5)).toThrow(TypeError);
    });

    test('throws TypeError for NaN or undefined values', () => {
        expect(() => isValidPortNumber(NaN)).toThrow(TypeError);
        expect(() => isValidPortNumber(undefined)).toThrow(TypeError);
    });
});
/**
 * Checks if the provided port number is within the valid range of TCP/UDP ports.
 * Valid TCP/UDP port numbers range from 1 to 65535.
 *
 * @param {number} port - The port number to verify.
 * @returns {boolean} Returns true if the port number is valid, false otherwise.
 */
function isValidPortNumber(port) {
    if (typeof port !== 'number' || isNaN(port) || Math.floor(port) !== port) {
        throw new TypeError('The port number must be an integer.');
    }

    return port >= 1 && port <= 65535;
}