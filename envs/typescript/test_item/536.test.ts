import { format } from 'date-fns';

/**
 * Gets the current date formatted as 'Month Day, Year'.
 *
 * @returns {string} The formatted date string.
 */
function getDate(): string {
  return format(new Date(), 'MMMM d, yyyy');
}
describe('getDate', () => {
    // Mock the Date object to control the current date for testing
    const mockDate: Date = new Date('2024-10-01T00:00:00Z');

    beforeAll(() => {
        // Mock the global Date object
        jest.spyOn(global, 'Date').mockImplementation(() => mockDate as any);
    });

    afterAll(() => {
        // Restore the original Date object
        (global.Date as jest.Mock).mockRestore();
    });

    test('returns date in "Month Day, Year" format', () => {
        const result: string = getDate();
        expect(result).toBe('October 1, 2024');
    });

    test('returns correct year', () => {
        const result: string = getDate();
        expect(result).toMatch(/2024/);
    });

    test('returns correct month', () => {
        const result: string = getDate();
        expect(result).toMatch(/October/);
    });

    test('returns correct day', () => {
        const result: string = getDate();
        expect(result).toMatch(/1/);
    });

    test('returns date as a string', () => {
        const result: string = getDate();
        expect(typeof result).toBe('string');
    });

    test('does not return undefined', () => {
        const result: string = getDate();
        expect(result).not.toBeUndefined();
    });
});
