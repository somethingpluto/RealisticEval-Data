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