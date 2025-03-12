import { formatDistance } from 'date-fns';

/**
 * Computes the difference between the specified date and the current time, returning it in a human-readable way
 *
 * @param {Date} createdAt - The date to calculate the time difference from.
 * @returns {string} A string indicating the time elapsed, e.g., "3 days ago", "5 hours ago".
 */
export const getTimestamp = (createdAt: Date): string => {
  return formatDistance(createdAt, new Date());
};
describe('getTimestamp', () => {
    test('should return "1 second ago" for a date 1 second ago', () => {
        const oneSecondAgo = new Date(new Date().getTime() - 1000); // 1 second ago
        // @ts-ignore
        expect(getTimestamp(oneSecondAgo)).toBe('1 second ago');
    });

    test('should return "5 minutes ago" for a date 5 minutes ago', () => {
        const fiveMinutesAgo = new Date(new Date().getTime() - 5 * 60 * 1000); // 5 minutes ago
        // @ts-ignore
        expect(getTimestamp(fiveMinutesAgo)).toBe('5 minutes ago');
    });

    test('should return "2 hours ago" for a date 2 hours ago', () => {
        const twoHoursAgo = new Date(new Date().getTime() - 2 * 60 * 60 * 1000); // 2 hours ago
        // @ts-ignore
        expect(getTimestamp(twoHoursAgo)).toBe('2 hours ago');
    });

    test('should return "3 days ago" for a date 3 days ago', () => {
        const threeDaysAgo = new Date(new Date().getTime() - 3 * 24 * 60 * 60 * 1000); // 3 days ago
        // @ts-ignore
        expect(getTimestamp(threeDaysAgo)).toBe('3 days ago');
    });

});

