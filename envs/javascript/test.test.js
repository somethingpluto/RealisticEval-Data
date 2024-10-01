/**
 * Converts a Unix timestamp to a readable date format.
 *
 * @param {number} timestamp - The Unix timestamp in milliseconds.
 * @returns {string} A readable date string in the format "MMM DD, HH:MM".
 */
function timestampToReadableDate(timestamp) {
    const date = new Date(timestamp);

    // Get local time components
    const options = { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false };
    const localDateString = date.toLocaleString('en-US', options);

    // Format the string to remove the AM/PM and format it as needed
    const [datePart, timePart] = localDateString.split(', ');
    const [hour, minute] = timePart.split(':');
    return `${datePart}, ${parseInt(hour)}:${minute}`;
}
describe('timestampToReadableDate Tests', () => {
    test('Converts current timestamp to readable date format', () => {
        const now = Date.now();
        const result = timestampToReadableDate(now);
        const date = new Date(now);
        const expected = `${date.toLocaleString('en-US', { month: 'short' })} ${date.getDate()}, ${date.getHours()}:${date.getMinutes().toString().padStart(2, '0')}`;

        expect(result).toBe(expected);
    });

    test('Handles a timestamp corresponding to midnight', () => {
        const midnight = new Date('2024-01-01T00:00:00Z').getTime();
        const result = timestampToReadableDate(midnight);
        expect(result).toBe('Jan 1, 0:00');
    });

    test('Handles a timestamp at the end of the month', () => {
        const endOfMonth = new Date('2024-01-31T23:59:59Z').getTime();
        const result = timestampToReadableDate(endOfMonth);
        expect(result).toBe('Jan 31, 23:59');
    });

    test('Handles a timestamp in a leap year', () => {
        const leapDay = new Date('2024-02-29T12:30:00Z').getTime();
        const result = timestampToReadableDate(leapDay);
        expect(result).toBe('Feb 29, 12:30');
    });

    test('Handles a timestamp from the previous year', () => {
        const lastYear = new Date('2023-03-15T15:15:00Z').getTime();
        const result = timestampToReadableDate(lastYear);
        expect(result).toBe('Mar 15, 15:15');
    });

    test('Handles a timestamp from the future', () => {
        const futureDate = new Date('2025-12-25T18:45:00Z').getTime();
        const result = timestampToReadableDate(futureDate);
        expect(result).toBe('Dec 25, 18:45');
    });
});
