/**
 * Formats the given timestamp as a string according to the specified format, using the system's local time zone.
 *
 * @param {number} timestamp - The time value representing the seconds since the epoch.
 * @param {string} [dateFormat='%a %b %d %I:%M:%S %p %z %Y'] - The format string to use for formatting the timestamp.
 *                                                          Defaults to '%a %b %d %I:%M:%S %p %z %Y'.
 * @returns {string} - The formatted date and time string.
 */
function formatTimestampToString(timestamp, dateFormat = '%a %b %d %I:%M:%S %p %z %Y') {
    // Convert the timestamp to milliseconds
    const date = new Date(timestamp * 1000);

    // Define a mapping for the format string
    const formatMap = {
        '%a': date.toLocaleDateString(undefined, { weekday: 'short' }),
        '%A': date.toLocaleDateString(undefined, { weekday: 'long' }),
        '%b': date.toLocaleDateString(undefined, { month: 'short' }),
        '%B': date.toLocaleDateString(undefined, { month: 'long' }),
        '%d': String(date.getDate()).padStart(2, '0'),
        '%I': String(date.getHours() % 12 || 12).padStart(2, '0'),
        '%H': String(date.getHours()).padStart(2, '0'),
        '%M': String(date.getMinutes()).padStart(2, '0'),
        '%S': String(date.getSeconds()).padStart(2, '0'),
        '%p': date.getHours() >= 12 ? 'PM' : 'AM',
        '%z': date.toTimeString().split(' ')[1].slice(0, 5),
        '%Y': String(date.getFullYear()),
        '%m': String(date.getMonth() + 1).padStart(2, '0'),
        '%j': String(date.getDay()).padStart(2, '0'),
    };

    // Replace the format string with the actual date values
    return dateFormat.replace(/%[aAbBcdHIJMSpzYmj]/g, (match) => formatMap[match] || match);
}
describe('formatTimestampToString', () => {
    it('test basic functionality with a known timestamp', () => {
        const timestamp = 1655364000.0; // Corresponds to Thu Jun 16 12:00:00 PM UTC 2022
        const expectedDateStr = 'Thu Jun 16 03:20:00 PM +0800 2022';
        expect(formatTimestampToString(timestamp)).toBe(expectedDateStr);
    });

    it('test using the default format string', () => {
        const timestamp = 1655364000.0;
        const expectedDateStr = 'Thu Jun 16 03:20:00 PM +0800 2022';
        expect(formatTimestampToString(timestamp)).toBe(expectedDateStr);
    });

    it('test with a custom format string', () => {
        const timestamp = 1655364000.0;
        const customFormat = 'yyyy-MM-dd HH:mm:ss';
        const expectedDateStr = '2022-06-16 15:20:00';
        expect(formatTimestampToString(timestamp, customFormat)).toBe(expectedDateStr);
    });

    it('test with an edge case timestamp (e.g., Unix epoch start)', () => {
        const timestamp = 0.0; // Unix epoch start
        const expectedDateStr = 'Thu Jan 01 08:00:00 AM +0800 1970';
        expect(formatTimestampToString(timestamp)).toBe(expectedDateStr);
    });
});
