/**
 * Parse a cron expression and determine whether it is between 2 a.m. and 4 a.m.
 * @param cronExpression
 */
function isCronBetween2And4AM(cronExpression) {
    // Split the cron expression into its components
    const parts = cronExpression.trim().split(/\s+/);

    // Ensure the cron expression has the correct number of components
    if (parts.length !== 5) {
        throw new Error("Invalid cron expression");
    }

    // Extract the minute, hour, day of month, month, and day of week components
    const [minute, hour, dayOfMonth, month, dayOfWeek] = parts;

    // Function to parse hour component
    function parseHour(hour) {
        if (hour === "*") {
            return null; // Any hour
        } else if (hour.includes(",")) {
            return hour.split(",").map(h => parseInt(h, 10));
        } else if (hour.includes("-")) {
            const [start, end] = hour.split("-").map(h => parseInt(h, 10));
            return Array.from({ length: end - start + 1 }, (_, i) => start + i);
        } else if (hour.includes("/")) {
            const [start, step] = hour.split("/").map(h => parseInt(h, 10));
            return Array.from({ length: 24 / step }, (_, i) => start + i * step);
        } else {
            return [parseInt(hour, 10)];
        }
    }

    // Parse the hour component
    const hours = parseHour(hour);

    // Check if the cron expression is between 2 a.m. and 4 a.m.
    if (hours === null) {
        return true; // Any hour matches
    } else {
        return hours.some(h => h >= 2 && h <= 4);
    }
}
describe('isCronBetween2And4AM', () => {
    test('should return true for specific hours 2, 3, and 4', () => {
        expect(isCronBetween2And4AM('0 2,3,4 * * *')).toBe(true);
    });

    test('should return false for range that includes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 1-5 * * *')).toBe(false);
    });

    test('should return false for range that excludes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 0-1,5-23 * * *')).toBe(false);
    });

    test('should return true for wildcard in hour field', () => {
        expect(isCronBetween2And4AM('0 * * * *')).toBe(false);
    });
});

