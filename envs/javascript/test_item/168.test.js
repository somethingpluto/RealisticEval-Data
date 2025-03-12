/**
 * Converts a date string into a relative time description.
 * For example, now time 2024-08-25T12:00:00
 *      input: 2024-08-24T12:00:00 output 1 day ago
 *      input: 2024-08-25T07:00:00 output: 5 hours ago
 *
 * @param {string} dateString - The date string to convert.
 * @returns {string} A user-friendly string representing the relative time difference from the current date.
 */
function formatDate(dateString) {
    const currentDate = new Date();
    const inputDate = new Date(dateString);

    const timeDifference = currentDate - inputDate;

    const seconds = Math.floor(timeDifference / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);
    const months = Math.floor(days / 30);
    const years = Math.floor(months / 12);

    if (years > 0) {
        return `${years} year${years > 1 ? 's' : ''} ago`;
    } else if (months > 0) {
        return `${months} month${months > 1 ? 's' : ''} ago`;
    } else if (days > 0) {
        return `${days} day${days > 1 ? 's' : ''} ago`;
    } else if (hours > 0) {
        return `${hours} hour${hours > 1 ? 's' : ''} ago`;
    } else if (minutes > 0) {
        return `${minutes} minute${minutes > 1 ? 's' : ''} ago`;
    } else {
        return `${seconds} second${seconds !== 1 ? 's' : ''} ago`;
    }
}
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
        expect(['1 day ago', '24 hours ago']).toContain(result);
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
        expect(['1 second ago', '1 seconds ago']).toContain(result);
    });
});
