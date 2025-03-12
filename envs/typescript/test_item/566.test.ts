import { DateTime } from 'luxon';

/**
 * Checks if two timestamps correspond to the same day.
 *
 * @param timestamp1 - The first timestamp to compare.
 * @param timestamp2 - The second timestamp to compare.
 * @returns True if both timestamps are on the same day, false otherwise.
 */
function isSameDay(timestamp1: number, timestamp2: number): boolean {
    const date1 = DateTime.fromMillis(timestamp1);
    const date2 = DateTime.fromMillis(timestamp2);
    return date1.startOf('day').isEqual(date2.startOf('day'));
}
describe('isSameDay', () => {
    test('should return false for timestamps on different days', () => {
        const timestamp1 = new Date(Date.UTC(2024, 9, 1, 10, 0, 0)).getTime(); // October 1, 2024, 10:00 AM UTC
        const timestamp2 = new Date(Date.UTC(2024, 9, 2, 10, 0, 0)).getTime(); // October 2, 2024, 10:00 AM UTC
        expect(isSameDay(timestamp1, timestamp2)).toBe(false);
    });

    test('should return true for timestamps on the same day but different times', () => {
        const timestamp1 = new Date(Date.UTC(2024, 9, 1, 0, 0, 0)).getTime(); // October 1, 2024, 12:00 AM UTC
        const timestamp2 = new Date(Date.UTC(2024, 9, 1, 12, 30, 0)).getTime(); // October 1, 2024, 12:30 PM UTC
        expect(isSameDay(timestamp1, timestamp2)).toBe(true);
    });

    test('should return true for timestamps on the same day in different time zones', () => {
        const timestamp1 = new Date(Date.UTC(2024, 9, 1, 10, 0, 0)).getTime(); // UTC
        const timestamp2 = new Date('2024-10-01T12:00:00+02:00').getTime(); // October 1, 2024, 12:00 PM UTC+2
        expect(isSameDay(timestamp1, timestamp2)).toBe(true);
    });

    test('should return true for timestamps at midnight on the same day', () => {
        const timestamp1 = new Date(Date.UTC(2024, 9, 1, 0, 0, 0)).getTime(); // October 1, 2024, 12:00 AM UTC
        const timestamp2 = new Date(Date.UTC(2024, 9, 1, 0, 0, 0)).getTime(); // Same timestamp
        expect(isSameDay(timestamp1, timestamp2)).toBe(true);
    });


    test('should return false for timestamps in different years', () => {
        const timestamp1 = new Date(Date.UTC(2023, 9, 1, 10, 0, 0)).getTime(); // October 1, 2023, 10:00 AM UTC
        const timestamp2 = new Date(Date.UTC(2024, 9, 1, 10, 0, 0)).getTime(); // October 1, 2024, 10:00 AM UTC
        expect(isSameDay(timestamp1, timestamp2)).toBe(false);
    });

    test('should return false for invalid timestamps', () => {
        const timestamp1 = new Date('invalid').getTime(); // Invalid timestamp
        const timestamp2 = new Date(Date.UTC(2024, 9, 1, 10, 0, 0)).getTime(); // Valid timestamp
        expect(isSameDay(timestamp1, timestamp2)).toBe(false);
    });
});
