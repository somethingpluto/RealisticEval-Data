import { format, parseISO, addHours } from 'date-fns';

/**
 * Determine whether the current time is within the specified time range (i.e., whether it is a break).
 * 
 * @param {string} startTime - The start time of the break in ISO 8601 format.
 * @param {string} endTime - The end time of the break in ISO 8601 format.
 * @param {string} currentTime - The current time in ISO 8601 format.
 * @returns {boolean} - True if the current time is within the break time range, false otherwise.
 */
function isBreakTime(startTime: string, endTime: string, currentTime: string): boolean {
    const start = parseISO(startTime);
    const end = parseISO(endTime);
    const current = parseISO(currentTime);

    if (start && end && current) {
        return current >= start && current <= end;
    }

    return false;
}
describe('isBreakTime Function Tests', () => {
    test('should return true when current time is exactly at the start time', () => {
        expect(isBreakTime("09:00", "10:00", "09:00")).toBe(true);
    });

    test('should return true when current time is within the break time range', () => {
        expect(isBreakTime("09:00", "10:00", "09:30")).toBe(true);
    });

    test('should return false when current time exactly exceeds the end time', () => {
        expect(isBreakTime("09:00", "10:00", "10:00")).toBe(false);
    });

    test('should return false when current time is before the break time', () => {
        expect(isBreakTime("09:00", "10:00", "08:59")).toBe(false);
    });

    test('should return false when current time is after the break time', () => {
        expect(isBreakTime("09:00", "10:00", "10:01")).toBe(false);
    });
});
