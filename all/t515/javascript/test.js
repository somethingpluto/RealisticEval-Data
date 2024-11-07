describe('TestFormatDateString', () => {
    it('test_valid_date_conversion', () => {
        // Test case for a valid date string.
        const dateStr = "Fri, 28 Sep 2023 14:45:00 +0000 (UTC)";
        const expectedDate = "2023-09-28_14:45:00";
        expect(formatDateString(dateStr)).toEqual(expectedDate);
    });

    it('test_invalid_date_format', () => {
        // Test case for an invalid date string format.
        const dateStr = "Invalid date format";
        expect(formatDateString(dateStr)).toBeNull();
    });

    it('test_missing_components', () => {
        // Test case for a date string missing components.
        const dateStr = "Fri, 28 Sep 2023 14:45:00 +0000";
        expect(formatDateString(dateStr)).toBe('2023-09-28_14:45:00');
    });

    it('test_edge_case_date', () => {
        // Test case for an edge case date string (e.g., leap year).
        const dateStr = "Sun, 29 Feb 2024 14:45:00 +0000 (UTC)";
        const expectedDate = "2024-02-29_14:45:00";
        expect(formatDateString(dateStr)).toEqual(expectedDate);
    });
});