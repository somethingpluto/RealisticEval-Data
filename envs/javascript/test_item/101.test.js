/**
 * Determine whether the current time is within the specified time range (i.e., whether it is a break)
 * 
 * @param {string} startTime - The start time of the break in HH:MM format.
 * @param {string} endTime - The end time of the break in HH:MM format.
 * @param {string} currentTime - The current time in HH:MM format.
 * @returns {boolean} - Returns true if the current time is within the specified time range, otherwise false.
 */
function isBreakTime(startTime, endTime, currentTime) {
    const start = convertToMinutes(startTime);
    const end = convertToMinutes(endTime);
    const current = convertToMinutes(currentTime);

    if (start <= end) {
        // Normal case, no wrap around midnight
        return current >= start && current < end;
    } else {
        // Wrap around midnight
        return current >= start || current < end;
    }
}

/**
 * Helper function to convert time in HH:MM format to minutes since midnight
 * 
 * @param {string} time - Time in HH:MM format
 * @returns {number} - Minutes since midnight
 */
function convertToMinutes(time) {
    const [hours, minutes] = time.split(':').map(Number);
    return hours * 60 + minutes;
}
describe('isBreakTime Function Tests', () => {
    test('should return true when current time is exactly at the start time', () => {
        expect(isBreakTime("09:00", "10:00", "09:00")).toBe(true);
    });

    test('should return true when current time is within the break time range', () => {
        expect(isBreakTime("09:00", "10:00", "09:30")).toBe(true);
    });

    test('should return false when current time is exactly exceed the end time', () => {
        expect(isBreakTime("09:00", "10:00", "20:00")).toBe(false);
    });

    test('should return false when current time is before the break time', () => {
        expect(isBreakTime("09:00", "10:00", "08:59")).toBe(false);
    });

    test('should return false when current time is after the break time', () => {
        expect(isBreakTime("09:00", "10:00", "10:01")).toBe(false);
    });
});
