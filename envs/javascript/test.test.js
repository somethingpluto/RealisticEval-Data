/**
 * calculate the time difference between the given date and the current date, and convert this time difference to days, hours, and minutes, returning the string Day: Hour: Minutes.for example return Day: 3 Hour: 3 Minutes: 15 means 3 days, 3 hours, 15 minutes before.Day: -2 Hour: -19 Minutes: -15 means 2 days, 5 hours, 45 minutes in the future
 *
 * @param {string|Date} date - The past date from which to calculate the time difference. Can be a Date object or a string that is parseable by the Date constructor.
 * @returns {string} - A formatted string representing the time difference in days, hours, and minutes.
 */
function getTimeDifference(date) {
 // Calculate the time difference between the given date and the current date
 const timeDifference = new Date(date) - new Date();

 // Calculate the number of days, hours, and minutes
 const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
 const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
 const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));

 // Return the formatted time difference
 return `Day: ${days} Hour: ${hours} Minutes: ${minutes}`;
}
// Mock current date for consistent test results
const mockCurrentDate = new Date('2024-08-23T15:45:00');
jest.useFakeTimers().setSystemTime(mockCurrentDate);

describe('getTimeDifference', () => {
    test('should return correct difference for a past date', () => {
        const result = getTimeDifference('2024-08-20T12:30:00');
        expect(result).toBe('Day: 3 Hour: 3 Minutes: 15'); // 3 days, 3 hours, 15 minutes difference
    });

    test('should return correct difference for a future date', () => {
        const result = getTimeDifference('2024-08-25T10:00:00');
        expect(result).toBe('Day: -2 Hour: -19 Minutes: -15'); // 2 days, 5 hours, 45 minutes in the future
    });

    test('should return correct difference for same day with different time', () => {
        const result = getTimeDifference('2024-08-23T10:00:00');
        expect(result).toBe('Day: 0 Hour: 5 Minutes: 45'); // 5 hours, 45 minutes difference on the same day
    });

    test('should return correct difference for date exactly one day ago', () => {
        const result = getTimeDifference('2024-08-22T15:45:00');
        expect(result).toBe('Day: 1 Hour: 0 Minutes: 0'); // 1 day difference exactly
    });

    test('should return correct difference for a few minutes ago', () => {
        const result = getTimeDifference('2024-08-23T15:40:00');
        expect(result).toBe('Day: 0 Hour: 0 Minutes: 5'); // 5 minutes ago
    });
});
