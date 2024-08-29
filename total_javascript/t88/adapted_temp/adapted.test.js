describe('isCronBetween2And4AM', () => {
    test('should return true for specific hours 2, 3, and 4', () => {
        expect(isCronBetween2And4AM('0 2,3,4 * * *')).toBe(true);
    });

    test('should return true for range that includes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 1-5 * * *')).toBe(true);
    });

    test('should return false for range that excludes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 0-1,5-23 * * *')).toBe(false);
    });

    test('should return true for wildcard in hour field', () => {
        expect(isCronBetween2And4AM('0 * * * *')).toBe(true);
    });

    test('should throw an error for invalid cron expressions', () => {
        expect(() => {
            isCronBetween2And4AM('invalid input');
        }).toThrow('Invalid cron expression');
    });
});
function isCronBetween2And4AM(cronExpression) {
    // Split the cron expression into its components
    const parts = cronExpression.split(' ');
    if (parts.length !== 5) {
        throw new Error('Invalid cron expression');
    }

    const hourField = parts[1]; // Get the hour part of the cron expression

    // Check if the hour field is a specific number or range including 2, 3, or 4
    if (hourField === '*') {
        // '*' means every hour, which includes 2 to 4
        return true;
    }

    // Split the hour field on comma for multiple specific hours or ranges
    const hourSegments = hourField.split(',');

    for (const segment of hourSegments) {
        if (segment.includes('-')) {
            // If the segment is a range, split on the dash and check the range
            const [start, end] = segment.split('-').map(Number);
            if (start <= 4 && end >= 2) {
                // Check if the range includes any of 2, 3, or 4
                return true;
            }
        } else if (['2', '3', '4'].includes(segment)) {
            // Check if the segment is exactly 2, 3, or 4
            return true;
        }
    }

    // If none of the segments include the hours 2, 3, or 4
    return false;
}
