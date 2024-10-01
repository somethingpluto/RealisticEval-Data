describe('getTime', () => {
    // Mock the Date object to control the current time for testing
    const mockDate = new Date('2024-10-01T14:30:00Z'); // Set mock time to 2:30 PM UTC

    beforeAll(() => {
        // Mock the global Date object
        jest.spyOn(global, 'Date').mockImplementation(() => mockDate);
    });

    afterAll(() => {
        // Restore the original Date object
        global.Date.mockRestore();
    });

    test('returns time in "hh:mm AM/PM" format', () => {
        const result = getTime();
        expect(result).toBe('2:30 PM');
    });

    test('returns correct hour', () => {
        const result = getTime();
        expect(result).toMatch(/2/); // Should match "2"
    });

    test('returns correct minutes', () => {
        const result = getTime();
        expect(result).toMatch(/30/); // Should match "30"
    });

    test('returns "PM" when time is in the afternoon', () => {
        const result = getTime();
        expect(result).toMatch(/PM/); // Should contain "PM"
    });

    test('returns "AM" when time is in the morning', () => {
        // Mock the date to a morning time
        const morningMockDate = new Date('2024-10-01T09:15:00Z'); // 9:15 AM
        jest.spyOn(global, 'Date').mockImplementation(() => morningMockDate);
        const result = getTime();
        expect(result).toBe('9:15 AM'); // Should be "9:15 AM"
        global.Date.mockRestore(); // Restore after test
    });

    test('handles edge case at noon', () => {
        const noonMockDate = new Date('2024-10-01T12:00:00Z'); // 12:00 PM
        jest.spyOn(global, 'Date').mockImplementation(() => noonMockDate);
        const result = getTime();
        expect(result).toBe('12:00 PM'); // Should be "12:00 PM"
        global.Date.mockRestore(); // Restore after test
    });

    test('handles edge case at midnight', () => {
        const midnightMockDate = new Date('2024-10-01T00:00:00Z'); // 12:00 AM
        jest.spyOn(global, 'Date').mockImplementation(() => midnightMockDate);
        const result = getTime();
        expect(result).toBe('12:00 AM'); // Should be "12:00 AM"
        global.Date.mockRestore(); // Restore after test
    });

    test('returns time as a string', () => {
        const result = getTime();
        expect(typeof result).toBe('string'); // Should return a string
    });
});