/**
 * Calculate the years, months, days, hours, and minutes that have passed from the birth date to the current date and return them as an array. The contents of the array are the values of these units.
 * @param {Date} birthDate
 * @return {Array} [years, months, days, hours, minutes]
 */
function getTimeSinceBornUntilNow(birthDate) {
    const now = new Date();
    const diffInMs = now - birthDate;

    const millisecondsPerMinute = 60 * 1000;
    const millisecondsPerHour = 60 * millisecondsPerMinute;
    const millisecondsPerDay = 24 * millisecondsPerHour;
    const millisecondsPerMonth = 30 * millisecondsPerDay; // Approximation
    const millisecondsPerYear = 365 * millisecondsPerDay; // Approximation

    const years = Math.floor(diffInMs / millisecondsPerYear);
    const months = Math.floor((diffInMs % millisecondsPerYear) / millisecondsPerMonth);
    const days = Math.floor((diffInMs % millisecondsPerMonth) / millisecondsPerDay);
    const hours = Math.floor((diffInMs % millisecondsPerDay) / millisecondsPerHour);
    const minutes = Math.floor((diffInMs % millisecondsPerHour) / millisecondsPerMinute);

    return [years, months, days, hours, minutes];
}
describe('getTimeSinceBornUntilNow', () => {
    beforeAll(() => {
        jest.useFakeTimers().setSystemTime(new Date('2024-08-23T15:45:00'));
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    test('should return the correct difference for a typical birth date', () => {
        const birthDate = new Date('1990-05-15T10:30:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([34, 3, 8, 5, 15]); // Example output: 34 years, 3 months, 8 days, 5 hours, 15 minutes
    });

    test('should return the correct difference for a recent birth date', () => {
        const birthDate = new Date('2024-08-20T12:00:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([0, 0, 3, 3, 45]); // 3 days, 3 hours, 45 minutes
    });

    test('should handle edge cases at the end of the year', () => {
        const birthDate = new Date('2023-12-31T23:59:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([0, 7, 22, 15, 46]); // 7 months, 22 days, 15 hours, 46 minutes
    });

    test('should handle birthdays earlier in the current month', () => {
        const birthDate = new Date('2024-08-01T00:00:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([0, 0, 22, 15, 45]); // 22 days, 15 hours, 45 minutes
    });

    test('should handle birthdays later in the current year before the current month', () => {
        const birthDate = new Date('2024-01-01T01:00:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([0, 7, 22, 14, 45]); // 7 months, 22 days, 14 hours, 45 minutes
    });

    test('should handle birthdays in the previous month of the same year', () => {
        const birthDate = new Date('2024-07-30T10:00:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([0, 0, 24, 5, 45]); // 24 days, 5 hours, 45 minutes
    });
});
