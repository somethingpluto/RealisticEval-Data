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
const Decimal = require('decimal.js');

/**
 * Computing PI (π) Using Gauss-Legendre Algorithm with High-precision Arithmetic Library decimal.js
 *
 * @param {number} digits - The number of decimal digits to compute π to.
 * @returns {string} - The value of π to the specified number of digits.
 */
function computePi(digits) {
  // Set the precision for Decimal calculations
  Decimal.set({ precision: digits + 10 }); // Extra precision to ensure accuracy

  const one = new Decimal(1);
  const two = new Decimal(2);
  const four = new Decimal(4);
  const half = new Decimal(0.5);

  // Initialize variables
  let a = one;
  let b = one.dividedBy(two).sqrt(); // b0 = 1 / sqrt(2)
  let t = one.dividedBy(four);       // t0 = 1/4
  let p = one;

  let prevPi = new Decimal(0);
  let pi;

  // Iterate until the desired precision is reached
  for (let i = 0; i < 10; i++) {
    const aNext = a.plus(b).dividedBy(two);
    const bNext = a.times(b).sqrt();
    const diff = a.minus(aNext);
    const tNext = t.minus(p.times(diff.pow(2)));
    const pNext = p.times(two);

    a = aNext;
    b = bNext;
    t = tNext;
    p = pNext;

    pi = a.plus(b).pow(2).dividedBy(t.times(four));

    // Check if the desired precision has been reached
    if (pi.equals(prevPi)) {
      break;
    }
    prevPi = pi;
  }

  // Return π to the specified number of digits
  return pi.toFixed(digits);
}