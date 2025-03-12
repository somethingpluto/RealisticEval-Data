import { DateTime } from 'luxon';

function findNthWeekdayOfSpecificYear(y: number, m: number, n: number, k: number): DateTime {
    // Validate input parameters
    if (m < 1 || m > 12) {
        throw new Error('Month must be between 1 and 12.');
    }
    if (k < 0 || k > 6) {
        throw new Error('Weekday must be between 0 (Monday) and 6 (Sunday).');
    }
    if (n < 1) {
        throw new Error('n must be a positive integer.');
    }

    // Find the first day of the month
    const firstDayOfMonth = DateTime.local(y, m, 1);

    // Calculate the date of the first occurrence of the weekday in the month
    const firstOccurrence = firstDayOfMonth
        .plus({ days: (k + firstDayOfMonth.weekday) % 7 })
        .startOf('day');

    // Calculate the date of the nth occurrence of the weekday in the month
    const nthOccurrence = firstOccurrence
        .plus({ weeks: n - 1 })
        .startOf('day');

    // If the nth occurrence is in the next month, return the last occurrence of the weekday in the current month
    if (nthOccurrence.month > m) {
        const lastDayOfMonth = firstDayOfMonth.endOf('month');
        const lastOccurrence = lastDayOfMonth
            .plus({ days: (7 - lastDayOfMonth.weekday + k) % 7 })
            .startOf('day');
        return lastOccurrence;
    }

    return nthOccurrence;
}
describe('TestFindNthWeekdayOfSpecificYear', () => {
    it('should return the 2nd Monday of May 2023', () => {
        // Test for the 2nd Monday of May 2023
        const result = findNthWeekdayOfSpecificYear(2023, 5, 2, 0); // Monday is 0
        const expected = DateTime.local(2023, 5, 8);
        expect(result).toEqual(expected);
    });

    it('should return the last Monday of May 2023', () => {
        // Test for the 5th Monday of May 2023, which doesn't exist, should return the last Monday
        const result = findNthWeekdayOfSpecificYear(2023, 5, 5, 0); // Monday is 0
        const expected = DateTime.local(2023, 5, 29);
        expect(result).toEqual(expected);
    });

    it('should return the 1st Tuesday of August 2023', () => {
        // Test for when the first day of the month is the weekday in question, 1st Tuesday of August 2023
        const result = findNthWeekdayOfSpecificYear(2023, 8, 1, 1); // Tuesday is 1
        const expected = DateTime.local(2023, 8, 1);
        expect(result).toEqual(expected);
    });

    it('should return the 1st Friday of December 2023', () => {
        // Test for the 1st Friday of December 2023
        const result = findNthWeekdayOfSpecificYear(2023, 12, 1, 4); // Friday is 4
        const expected = DateTime.local(2023, 12, 1);
        expect(result).toEqual(expected);
    });
});
