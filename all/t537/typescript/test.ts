describe('getTime', () => {
    const mockDate = (dateString: string): void => {
        const date = new Date(dateString);
        jest.spyOn(global, 'Date').mockImplementation(() => date);
    };

    afterEach(() => {
        jest.restoreAllMocks();
    });

    test('should return a string', () => {
        mockDate('2024-10-01T10:30:00'); // Mocking a specific date and time
        const result: string = getTime();
        expect(typeof result).toBe('string');
    });

    test('should return a formatted time string including AM/PM', () => {
        mockDate('2024-10-01T15:45:00'); // 3:45 PM
        const result: string = getTime();
        expect(result).toMatch(/^\d{1,2}:\d{2} (AM|PM)$/);
    });

    test('should return the correct time during AM hours', () => {
        mockDate('2024-10-01T08:15:00'); // 8:15 AM
        const result: string = getTime();
        expect(result).toBe('8:15 AM');
    });

    test('should return the correct time during PM hours', () => {
        mockDate('2024-10-01T17:20:00'); // 5:20 PM
        const result: string = getTime();
        expect(result).toBe('5:20 PM');
    });

    test('should return "12:00 AM" at midnight', () => {
        mockDate('2024-10-01T00:00:00'); // 12:00 AM
        const result: string = getTime();
        expect(result).toBe('12:00 AM');
    });

    test('should return "12:00 PM" at noon', () => {
        mockDate('2024-10-01T12:00:00'); // 12:00 PM
        const result: string = getTime();
        expect(result).toBe('12:00 PM');
    });

    test('should handle single-digit minutes correctly', () => {
        mockDate('2024-10-01T09:05:00'); // 9:05 AM
        const result: string = getTime();
        expect(result).toBe('9:05 AM');
    });
});