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