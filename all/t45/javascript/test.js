const { getCurrentDateInfo } = require('./yourModule'); // Adjust the path to where your function is stored

describe('getCurrentDateInfo', () => {
    test('Beginning of month', () => {
        const result = getCurrentDateInfo(new Date(2023, 0, 1)); // Months are 0-indexed in JavaScript
        const expected = {
            year: 2023,
            month: 'January',
            week_of_the_month: 1,
            day_of_the_week: 'Sunday'
        };
        expect(result).toEqual(expected);
    });

    test('Middle of month', () => {
        const result = getCurrentDateInfo(new Date(2023, 0, 15));
        const expected = {
            year: 2023,
            month: 'January',
            week_of_the_month: 3,
            day_of_the_week: 'Sunday'
        };
        expect(result).toEqual(expected);
    });

    test('End of month', () => {
        const result = getCurrentDateInfo(new Date(2023, 0, 31));
        const expected = {
            year: 2023,
            month: 'January',
            week_of_the_month: 6,
            day_of_the_week: 'Tuesday'
        };
        expect(result).toEqual(expected);
    });

    test('Leap year', () => {
        const result = getCurrentDateInfo(new Date(2024, 1, 29));
        const expected = {
            year: 2024,
            month: 'February',
            week_of_the_month: 5,
            day_of_the_week: 'Thursday'
        };
        expect(result).toEqual(expected);
    });

    test('Change of year', () => {
        const result = getCurrentDateInfo(new Date(2022, 11, 31));
        const expected = {
            year: 2022,
            month: 'December',
            week_of_the_month: 5,
            day_of_the_week: 'Saturday'
        };
        expect(result).toEqual(expected);
    });
});