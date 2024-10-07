describe('calculateGoodFriday', () => {
    it('should correctly calculate Good Friday for 2024', () => {
        const result = calculateGoodFriday(2024);
        expect(result.toDateString()).toBe('Fri Mar 29 2024');
    });

    it('should correctly calculate Good Friday for 2021', () => {
        const result = calculateGoodFriday(2021);
        expect(result.toDateString()).toBe('Fri Apr 02 2021');
    });

    it('should correctly calculate Good Friday for 2000', () => {
        const result = calculateGoodFriday(2000);
        expect(result.toDateString()).toBe('Fri Apr 21 2000');
    });

    it('should correctly calculate Good Friday for 2019', () => {
        const result = calculateGoodFriday(2019);
        expect(result.toDateString()).toBe('Fri Apr 19 2019');
    });

    it('should correctly calculate Good Friday for 1999', () => {
        const result = calculateGoodFriday(1999);
        expect(result.toDateString()).toBe('Fri Apr 02 1999');
    });

    it('should correctly calculate Good Friday for 1981', () => {
        const result = calculateGoodFriday(1981);
        expect(result.toDateString()).toBe('Fri Apr 17 1981');
    });

    it('should correctly calculate Good Friday for 1954', () => {
        const result = calculateGoodFriday(1954);
        expect(result.toDateString()).toBe('Fri Apr 16 1954');
    });
});