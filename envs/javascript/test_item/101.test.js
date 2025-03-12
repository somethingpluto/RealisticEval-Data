/**
 * Determine whether the current time is within the specified time range (i.e., whether it is a break)
 * 
 * @param {string} startTime - The start time of the break in HH:MM format.
 * @param {string} endTime - The end time of the break in HH:MM format.
 * @param {string} currentTime - The current time in HH:MM format.
 * @returns {boolean} - True if the current time is within the break time, otherwise false.
 */
function isBreakTime(startTime, endTime, currentTime) {
    // Helper function to convert HH:MM format to minutes since midnight
    function timeToMinutes(time) {
        const [hours, minutes] = time.split(':').map(Number);
        return hours * 60 + minutes;
    }

    const startMinutes = timeToMinutes(startTime);
    const endMinutes = timeToMinutes(endTime);
    const currentMinutes = timeToMinutes(currentTime);

    // Check if the end time is less than the start time (indicating a range that spans midnight)
    if (endMinutes < startMinutes) {
        return currentMinutes >= startMinutes || currentMinutes < endMinutes;
    } else {
        return currentMinutes >= startMinutes && currentMinutes < endMinutes;
    }
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
