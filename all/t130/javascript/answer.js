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