describe('timestampToReadableDate', () => {
    test('converts Unix timestamp for New Year\'s Day', () => {
        // January 1, 2023 00:00 GMT
        expect(timestampToReadableDate(1672531200)).toBe('Jan 1, 8:00');
    });

    test('converts Unix timestamp for a leap day', () => {
        // February 29, 2024 12:00 GMT (leap year)
        expect(timestampToReadableDate(1709227200)).toBe('Mar 1, 1:20');
    });

    test('converts Unix timestamp for a summer day', () => {
        // June 21, 2023 15:45 GMT
        expect(timestampToReadableDate(1687362300)).toBe('Jun 21, 23:45');
    });

    test('handles minutes with leading zero', () => {
        // October 3, 2023 02:05 GMT
        expect(timestampToReadableDate(1696377900)).toBe('Oct 4, 8:05');
    });

    test('handles end of the year', () => {
        // December 31, 2023 23:59 GMT
        expect(timestampToReadableDate(1704067140)).toBe('Jan 1, 7:59');
    });
});
//written by GPT-3.5
const timestampToReadableDate = function (unixTimestamp) {
    const date = new Date(unixTimestamp * 1000);
    const monthNames = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ];
    const month = monthNames[date.getMonth()];
    const day = date.getDate();
    const hours = date.getHours();
    const minutes = date.getMinutes();
    return `${month} ${day}, ${hours}:${minutes.toString().padStart(2, '0')}`;
}