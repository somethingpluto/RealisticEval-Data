/**
 * Computing PI (π) Using Gauss-Legendre Algorithm with High-precision Arithmetic Library decimal.js
 *
 * @param {number} digits - The number of decimal digits to compute π to.
 * @returns {string} - The value of π to the specified number of digits.
 */
function computePi(digits) {
  // Importing the decimal.js library
  const Decimal = require('decimal.js');

  // Set the precision for decimal.js
  Decimal.set({ precision: digits + 2, rounding: Decimal.ROUND_HALF_UP });

  // Initialize variables
  let a = new Decimal(1);
  let b = new Decimal(1).dividedBy(Math.sqrt(2));
  let t = new Decimal(1).dividedBy(4);
  let p = new Decimal(1);

  // Perform the Gauss-Legendre algorithm
  while (true) {
    let a_next = a.plus(b).dividedBy(2);
    let b = Math.sqrt(a.times(b));
    let t = t.minus(p.times(a.minus(a_next).pow(2)));
    let p = p.times(2);

    // Check if the desired precision is reached
    if (a_next.minus(a).abs().lt(new Decimal(10).pow(-digits))) {
      break;
    }

    a = a_next;
  }

  // Calculate π
  let pi = a_next.plus(b).pow(2).dividedBy(4).dividedBy(t);

  // Return π as a string with the specified number of digits
  return pi.toFixed(digits);
}

// Export the function for use in other modules
module.exports = computePi;
describe('computePi', () => {
    test('should calculate pi to 5 decimal places correctly', () => {
        const digits = 5;
        const expected = '3.14159';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 10 decimal places correctly', () => {
        const digits = 10;
        const expected = '3.1415926536';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 15 decimal places correctly', () => {
        const digits = 15;
        const expected = '3.141592653589793';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 20 decimal places correctly', () => {
        const digits = 20;
        const expected = '3.14159265358979323846';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 30 decimal places correctly', () => {
        const digits = 30;
        const expected = '3.141592653589793238462643383280';
        const result = computePi(digits);
        expect(result).toBe(expected);
    });
});
