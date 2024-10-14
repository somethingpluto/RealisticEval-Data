describe('TestDateRangeString', () => {
    it('should correctly format dates within the same month', () => {
        const result = dateRangeString("2023-08-01", "2023-08-15");
        expect(result).toBe("August 1 to 15, 2023");
    });

    it('should correctly format dates within the same month (start to end)', () => {
        const result = dateRangeString("2023-08-01", "2023-08-31");
        expect(result).toBe("August 1 to 31, 2023");
    });

    it('should correctly format dates across different months within the same year', () => {
        const result = dateRangeString("2023-08-30", "2023-09-05");
        expect(result).toBe("August 30, 2023 to September 5, 2023");
    });

    it('should correctly format dates across different years', () => {
        const result = dateRangeString("2023-12-30", "2024-01-02");
        expect(result).toBe("December 30, 2023 to January 2, 2024");
    });
});