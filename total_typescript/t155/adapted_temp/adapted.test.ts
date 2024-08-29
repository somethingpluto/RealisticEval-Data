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

    test('should return "1 year ago" for a date 1 year ago', () => {
        const oneYearAgo = new Date(new Date().getTime() - 365 * 24 * 60 * 60 * 1000); // 1 year ago
        // @ts-ignore
        expect(getTimestamp(oneYearAgo)).toBe('1 year ago');
    });
});
/**
 * Computes the difference between the specified date and the current time, returning it in a human-readable way
 *
 * @param {Date} createdAt - The date to calculate the time difference from.
 * @returns {string} A string indicating the time elapsed, e.g., "3 days ago", "5 hours ago".
 */
export const getTimestamp = (createdAt: Date): string => {
    const now = new Date();
    const diffInSeconds = Math.floor((now.getTime() - createdAt.getTime()) / 1000);

    // Define time intervals in seconds
    const intervals = {
        year: 31536000,
        month: 2592000,
        week: 604800,
        day: 86400,
        hour: 3600,
        minute: 60,
    };

    // Determine the most appropriate time interval and its unit
    let intervalCount: number;
    let intervalUnit: string;

    if (diffInSeconds >= intervals.year) {
        intervalCount = Math.floor(diffInSeconds / intervals.year);
        intervalUnit = intervalCount === 1 ? 'year' : 'years';
    } else if (diffInSeconds >= intervals.month) {
        intervalCount = Math.floor(diffInSeconds / intervals.month);
        intervalUnit = intervalCount === 1 ? 'month' : 'months';
    } else if (diffInSeconds >= intervals.week) {
        intervalCount = Math.floor(diffInSeconds / intervals.week);
        intervalUnit = intervalCount === 1 ? 'week' : 'weeks';
    } else if (diffInSeconds >= intervals.day) {
        intervalCount = Math.floor(diffInSeconds / intervals.day);
        intervalUnit = intervalCount === 1 ? 'day' : 'days';
    } else if (diffInSeconds >= intervals.hour) {
        intervalCount = Math.floor(diffInSeconds / intervals.hour);
        intervalUnit = intervalCount === 1 ? 'hour' : 'hours';
    } else if (diffInSeconds >= intervals.minute) {
        intervalCount = Math.floor(diffInSeconds / intervals.minute);
        intervalUnit = intervalCount === 1 ? 'minute' : 'minutes';
    } else {
        intervalCount = diffInSeconds;
        intervalUnit = intervalCount === 1 ? 'second' : 'seconds';
    }

    return `${intervalCount} ${intervalUnit} ago`;
};
