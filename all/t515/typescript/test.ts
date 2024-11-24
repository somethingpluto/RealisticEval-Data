describe('formatDateString', () => {
    it('should correctly convert a valid date string', () => {
        const dateStr = "Fri, 28 Sep 2023 14:45:00 +0000 (UTC)";
        const expectedDate = "2023-09-28_14:45:00";
        expect(formatDateString(dateStr)).toBe(expectedDate);
    });

    it('should return null for an invalid date string format', () => {
        const dateStr = "Invalid date format";
        expect(formatDateString(dateStr)).toBeNull();
    });

    it('should correctly convert an edge case date string (e.g., leap year)', () => {
        const dateStr = "Sun, 29 Feb 2024 14:45:00 +0000 (UTC)";
        const expectedDate = "2024-02-29_14:45:00";
        expect(formatDateString(dateStr)).toBe(expectedDate);
    });
});