/**
 * Gets the current date formatted as 'Month Day, Year'.
 *
 * @returns {string} The formatted date string.
 */
function getDate() {
    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    const now = new Date();
    const month = months[now.getMonth()];
    const day = now.getDate();
    const year = now.getFullYear();

    return `${month} ${day}, ${year}`;
}
describe('getDate', () => {
    // Mock the Date object to control the current date for testing
    const mockDate = new Date('2024-10-01T00:00:00Z');

    beforeAll(() => {
        // Mock the global Date object
        jest.spyOn(global, 'Date').mockImplementation(() => mockDate);
    });

    afterAll(() => {
        // Restore the original Date object
        global.Date.mockRestore();
    });

    test('returns date in "Month Day, Year" format', () => {
        const result = getDate();
        expect(result).toBe('October 1, 2024');
    });

    test('returns correct year', () => {
        const result = getDate();
        expect(result).toMatch(/2024/);
    });

    test('returns correct month', () => {
        const result = getDate();
        expect(result).toMatch(/October/);
    });

    test('returns correct day', () => {
        const result = getDate();
        expect(result).toMatch(/1/);
    });


    test('returns date as a string', () => {
        const result = getDate();
        expect(typeof result).toBe('string');
    });

    test('does not return undefined', () => {
        const result = getDate();
        expect(result).not.toBeUndefined();
    });
});
