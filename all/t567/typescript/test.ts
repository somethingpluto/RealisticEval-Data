describe('getRelativeTime', () => {
    beforeAll(() => {
        // Mock the current date to ensure consistent test results
        jest.useFakeTimers().setSystemTime(new Date('2024-10-01'));
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    test('should return "Today" for a message created today', () => {
        const messageDate = new Date(); // Current date
        expect(getRelativeTime(messageDate)).toBe("Today");
    });

    test('should return "Yesterday" for a message created yesterday', () => {
        const messageDate = new Date(Date.now() - 1000 * 60 * 60 * 24); // Yesterday
        expect(getRelativeTime(messageDate)).toBe("Yesterday");
    });

    test('should return formatted date string for a message created 10 days ago', () => {
        const messageDate = new Date(Date.now() - 1000 * 60 * 60 * 24 * 10); // 10 days ago
        expect(getRelativeTime(messageDate)).toBe("2024/9/21"); // Adjust based on the mock date
    });

    test('should return formatted date string for a message created 15 days ago', () => {
        const messageDate = new Date(Date.now() - 1000 * 60 * 60 * 24 * 15); // 15 days ago
        expect(getRelativeTime(messageDate)).toBe("2024/9/16"); // Adjust based on the mock date
    });
});