import { Decimal } from 'decimal.js';

function computePi(digits: number): string {
    const precision = new Decimal(10).pow(new Decimal(digits));
    let a = new Decimal(1);
    let b = new Decimal(1).div(new Decimal(2).sqrt());
    let t = new Decimal(1).div(4);
    let p = new Decimal(1);

    while (a.comparedTo(precision) < 0) {
        let aNext = a.add(b).div(new Decimal(2));
        let bNext = a.mul(b).sqrt();
        let tNext = t.sub(p.mul(a.sub(aNext).pow(2)));
        let pNext = p.mul(new Decimal(2));

        a = aNext;
        b = bNext;
        t = tNext;
        p = pNext;
    }

    return a.toDecimalPlaces(digits).toString();
}
describe('computePi', () => {
    test('should calculate pi to 5 decimal places correctly', () => {
        const digits: number = 5;
        const expected: string = '3.14159';
        const result: string = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 10 decimal places correctly', () => {
        const digits: number = 10;
        const expected: string = '3.1415926536';
        const result: string = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 15 decimal places correctly', () => {
        const digits: number = 15;
        const expected: string = '3.141592653589793';
        const result: string = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 20 decimal places correctly', () => {
        const digits: number = 20;
        const expected: string = '3.14159265358979323846';
        const result: string = computePi(digits);
        expect(result).toBe(expected);
    });

    test('should calculate pi to 30 decimal places correctly', () => {
        const digits: number = 30;
        const expected: string = '3.141592653589793238462643383280';
        const result: string = computePi(digits);
        expect(result).toBe(expected);
    });
});
