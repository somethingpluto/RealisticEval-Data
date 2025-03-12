const Decimal = require('decimal.js');

/**
 * Computing PI (π) Using Gauss-Legendre Algorithm with High-precision Arithmetic Library decimal.js
 *
 * @param {number} digits - The number of decimal digits to compute π to.
 * @returns {string} - The value of π to the specified number of digits.
 */
function computePi(digits) {
    Decimal.set({ precision: digits + 2 });

    let a = new Decimal(1);
    let b = a.div(Decimal.sqrt(2));
    let t = new Decimal(0.25);
    let p = new Decimal(1);

    while (true) {
        let aNext = a.plus(b).div(2);
        let bNext = Decimal.sqrt(a.times(b));
        let tNext = t.minus(p.times(a.minus(aNext).pow(2)));
        let pNext = p.times(2);

        if (a.equals(aNext) && b.equals(bNext)) {
            break;
        }

        a = aNext;
        b = bNext;
        t = tNext;
        p = pNext;
    }

    let pi = a.plus(b).pow(2).div(t.times(4));
    return pi.toFixed(digits);
}

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
