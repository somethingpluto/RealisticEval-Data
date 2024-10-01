describe('incrementNumber', () => {
    test('should return 6 when input is 5', () => {
        expect(incrementNumber(5)).toBe(6);
    });

    test('should return 0 when input is 0', () => {
        expect(incrementNumber(0)).toBe(0);
    });

    test('should return -3 when input is -3', () => {
        expect(incrementNumber(-3)).toBe(-3);
    });

    test('should return 1 when input is 0.5', () => {
        expect(incrementNumber(0.5)).toBe(1.5);
    });

    test('should return 1 when input is 1', () => {
        expect(incrementNumber(1)).toBe(2);
    });

    test('should return -1 when input is -1', () => {
        expect(incrementNumber(-1)).toBe(-1);
    });
});