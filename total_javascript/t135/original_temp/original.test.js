describe('isValidPort', () => {
    test('returns true for a valid port number in the middle of the range', () => {
        expect(isValidPort(8080)).toBe(true);
    });

    test('returns true for the lowest valid port number', () => {
        expect(isValidPort(1)).toBe(true);
    });

    test('returns true for the highest valid port number', () => {
        expect(isValidPort(65535)).toBe(true);
    });

    test('returns false for a port number below the valid range', () => {
        expect(isValidPort(0)).toBe(false);
    });

    test('returns false for a port number above the valid range', () => {
        expect(isValidPort(65536)).toBe(false);
    });

    test('throws TypeError for non-integer values', () => {
        expect(() => isValidPort('3000')).toThrow(TypeError);
        expect(() => isValidPort(300.5)).toThrow(TypeError);
    });

    test('throws TypeError for NaN or undefined values', () => {
        expect(() => isValidPort(NaN)).toThrow(TypeError);
        expect(() => isValidPort(undefined)).toThrow(TypeError);
    });
});
  // Generated Using ChatGPT
  
  export function isValidPort(port) {
    const portRegex =
      /^(?:[1-9]\d{0,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$/;
    return portRegex.test(port);
  }
  