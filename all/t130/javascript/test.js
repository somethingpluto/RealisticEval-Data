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