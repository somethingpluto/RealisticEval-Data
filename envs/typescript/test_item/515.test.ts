import { format, parse } from 'date-fns';

/**
 * Converts a date string from the format '%a, %d %b %Y %H:%M:%S %z (%Z)'
 * to the format '%Y-%m-%d_%H:%M:%S'.
 *
 * @param dateStr - The input date string.
 * @returns The formatted date string in the format '%Y-%m-%d_%H:%M:%S', or null if the input date string is invalid.
 */
function formatDateString(dateStr: string): string | null {
    try {
        const parsedDate = parse(dateStr, "%a, %d %b %Y %H:%M:%S %z (%Z)", new Date());
        return format(parsedDate, "%Y-%m-%d_%H:%M:%S");
    } catch (error) {
        console.error("Invalid date string:", error);
        return null;
    }
}
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

    it('should return null for a date string missing components', () => {
        const dateStr = "Fri, 28 Sep 2023 14:45:00 +0000";
        expect(formatDateString(dateStr)).toBeNull();
    });

    it('should correctly convert an edge case date string (e.g., leap year)', () => {
        const dateStr = "Sun, 29 Feb 2024 14:45:00 +0000 (UTC)";
        const expectedDate = "2024-02-29_14:45:00";
        expect(formatDateString(dateStr)).toBe(expectedDate);
    });
});
