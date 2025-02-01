/**
 * Formats the given timestamp as a string according to the specified format, using the system's local time zone.
 *
 * @param {number} timestamp - The time value representing the seconds since the epoch.
 * @param {string} [dateFormat='%a %b %d %I:%M:%S %p %z %Y'] - The format string to use for formatting the timestamp.
 *                                                          Defaults to '%a %b %d %I:%M:%S %p %z %Y'.
 * @returns {string} - The formatted date and time string.
 */
function formatTimestampToString(timestamp, dateFormat = '%a %b %d %I:%M:%S %p %z %Y') {
    const date = new Date(timestamp * 1000);
    const formatParts = dateFormat.match(/%[a-zA-Z]/g);
    let formattedString = '';

    if (!formatParts) {
        return dateFormat;
    }

    formatParts.forEach(part => {
        switch (part) {
            case '%a':
                formattedString += date.toLocaleDateString(undefined, { weekday: 'short' });
                break;
            case '%A':
                formattedString += date.toLocaleDateString(undefined, { weekday: 'long' });
                break;
            case '%b':
                formattedString += date.toLocaleDateString(undefined, { month: 'short' });
                break;
            case '%B':
                formattedString += date.toLocaleDateString(undefined, { month: 'long' });
                break;
            case '%d':
                formattedString += date.getDate().toString().padStart(2, '0');
                break;
            case '%I':
                formattedString += date.getHours().toString().padStart(2, '0');
                break;
            case '%M':
                formattedString += date.getMinutes().toString().padStart(2, '0');
                break;
            case '%S':
                formattedString += date.getSeconds().toString().padStart(2, '0');
                break;
            case '%p':
                formattedString += date.getHours() >= 12 ? 'PM' : 'AM';
                break;
            case '%z':
                formattedString += date.toTimeString().match(/\(([A-Z]{3})\)/)[1];
                break;
            case '%Y':
                formattedString += date.getFullYear();
                break;
            default:
                formattedString += part;
        }
    });

    return formattedString;
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
