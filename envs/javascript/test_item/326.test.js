/**
 * Calculates the time difference between a given date and the current date.
 *
 * @param {Date | string} givenDate - The date to compare against the current date.
 * @returns {Object} - An object containing days, hours, and minutes elapsed.
 * {
 *         days: days,
 *         hours: remainingHours,
 *         minutes: remainingMinutes,
 * }
 */
function calculateTimeDifference(givenDate) {
    // Convert givenDate to a Date object if it's a string
    if (typeof givenDate === 'string') {
        givenDate = new Date(givenDate);
    }

    // Get the current date and time
    const currentDate = new Date();

    // Calculate the difference in milliseconds
    const timeDifference = currentDate - givenDate;

    // Convert milliseconds to days, hours, and minutes
    const totalMinutes = Math.floor(timeDifference / (1000 * 60));
    const days = Math.floor(totalMinutes / (60 * 24));
    const remainingMinutes = totalMinutes % (60 * 24);
    const hours = Math.floor(remainingMinutes / 60);
    const minutes = remainingMinutes % 60;

    // Return the result as an object
    return {
        days: days,
        hours: hours,
        minutes: minutes,
    };
}
describe('calculateTimeDifference', () => {
    test('should return correct time difference for a date in the past', () => {
        const pastDate = new Date(Date.now() - 3 * 24 * 60 * 60 * 1000 - 5 * 60 * 1000); // 3 days and 5 minutes ago
        const result = calculateTimeDifference(pastDate);
        expect(result).toEqual({ days: 3, hours: 0, minutes: 5 });
    });

    test('should return correct time difference for a date that is exactly now', () => {
        const now = new Date();
        const result = calculateTimeDifference(now);
        expect(result).toEqual({ days: 0, hours: 0, minutes: 0 });
    });

    test('should return correct time difference for a date just seconds ago', () => {
        const justNow = new Date(Date.now() - 45 * 1000); // 45 seconds ago
        const result = calculateTimeDifference(justNow);
        expect(result).toEqual({ days: 0, hours: 0, minutes: 0 });
    });


    test('should return correct time difference for a date with only hours difference', () => {
        const hoursAgo = new Date(Date.now() - 7 * 60 * 60 * 1000); // 7 hours ago
        const result = calculateTimeDifference(hoursAgo);
        expect(result).toEqual({ days: 0, hours: 7, minutes: 0 });
    });

    test('should return correct time difference for a date with hours and minutes difference', () => {
        const hoursAndMinutesAgo = new Date(Date.now() - (1 * 24 * 60 * 60 * 1000 + 3 * 60 * 1000)); // 1 day and 3 minutes ago
        const result = calculateTimeDifference(hoursAndMinutesAgo);
        expect(result).toEqual({ days: 1, hours: 0, minutes: 3 });
    });

});

