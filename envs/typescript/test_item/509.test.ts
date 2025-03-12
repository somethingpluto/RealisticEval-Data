// Start of the TypeScript file

/**
 * Performs modular exponentiation: (base^exponent) % modulus efficiently.
 * This function is now part of a module and can be exported for use in other files.
 *
 * @param base - The base value.
 * @param exponent - The exponent value (should be non-negative).
 * @param modulus - The modulus value (should be positive).
 * @returns The result of (base^exponent) % modulus.
 * @throws {Error} If modulus is less than or equal to zero.
 */
export function modExp(base: number, exponent: number, modulus: number): number {
    if (modulus <= 0) {
        throw new Error("Modulus must be a positive integer.");
    }
    let result = 1;
    base = base % modulus;
    while (exponent > 0) {
        if (exponent % 2 === 1) {
            result = (result * base) % modulus;
        }
        exponent = Math.floor(exponent / 2);
        base = (base * base) % modulus;
    }
    return result;
}

// End of the TypeScript file
describe('TestModExp', () => {
  it('test_case_1', () => {
    // Test with base = 2, exponent = 10, modulus = 1000
    expect(modExp(2, 10, 1000)).toBe(24);
  });

  it('test_case_2', () => {
    // Test with base = 3, exponent = 7, modulus = 50
    expect(modExp(3, 7, 50)).toBe(37);
  });

  it('test_case_3', () => {
    // Test with base = 5, exponent = 0, modulus = 13 (any number^0 = 1)
    expect(modExp(5, 0, 13)).toBe(1);
  });

  it('test_case_4', () => {
    // Test with base = 7, exponent = 5, modulus = 20
    expect(modExp(7, 5, 20)).toBe(7);  // 7^5 = 16807, 16807 % 20 = 7
  });

  it('test_case_5', () => {
    // Test with base = 10, exponent = 5, modulus = 6
    expect(modExp(10, 5, 6)).toBe(4);  // 10^5 = 100000, 100000 % 6 = 4
  });
});
