describe('formatDate', () => {
    beforeAll(() => {
        // Set the system time to a fixed date for consistent testing
        jest.useFakeTimers().setSystemTime(new Date('2024-08-25T12:00:00'));
    });

    afterAll(() => {
        // Restore the real system time after tests
        jest.useRealTimers();
    });

    test('should return "1 day ago" for a date exactly one day before', () => {
        const dateString = '2024-08-24T12:00:00';
        const result = formatDate(dateString);
        expect(result).toBe('1 day ago');
    });

    test('should return "5 hours ago" for a date 5 hours before the current time', () => {
        const dateString = '2024-08-25T07:00:00';
        const result = formatDate(dateString);
        expect(result).toBe('5 hours ago');
    });

    test('should return "2 minutes ago" for a date 2 minutes before the current time', () => {
        const dateString = '2024-08-25T11:58:00';
        const result = formatDate(dateString);
        expect(result).toBe('2 minutes ago');
    });

    test('should return "just now" for a date within the last second', () => {
        const dateString = '2024-08-25T11:59:59';
        const result = formatDate(dateString);
        expect(result).toBe('1 second ago');
    });

    test('should handle invalid date string gracefully', () => {
    const dateString = 'invalid-date';
    expect(() => formatDate(dateString)).toThrow('Invalid Date');
});

});

