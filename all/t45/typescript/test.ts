import { getCurrentDateInfo } from './yourModule'; // Adjust the import according to your file structure

describe('getCurrentDateInfo', () => {
    test('beginning of month', () => {
        const result = getCurrentDateInfo(new Date(2023, 0, 1)); // January is month 0
        const expected = {
            year: 2023,
            month: 'January',
            weekOfTheMonth: 1,
            dayOfTheWeek: 'Sunday'
        };
        expect(result).toEqual(expected);
    });

    test('middle of month', () => {
        const result = getCurrentDateInfo(new Date(2023, 0, 15));
        const expected = {
            year: 2023,
            month: 'January',
            weekOfTheMonth: 3,
            dayOfTheWeek: 'Sunday'
        };
        expect(result).toEqual(expected);
    });

    test('end of month', () => {
        const result = getCurrentDateInfo(new Date(2023, 0, 31));
        const expected = {
            year: 2023,
            month: 'January',
            weekOfTheMonth: 6,
            dayOfTheWeek: 'Tuesday'
        };
        expect(result).toEqual(expected);
    });

    test('leap year', () => {
        const result = getCurrentDateInfo(new Date(2024, 1, 29)); // February is month 1
        const expected = {
            year: 2024,
            month: 'February',
            weekOfTheMonth: 5,
            dayOfTheWeek: 'Thursday'
        };
        expect(result).toEqual(expected);
    });

    test('change of year', () => {
        const result = getCurrentDateInfo(new Date(2022, 11, 31)); // December is month 11
        const expected = {
            year: 2022,
            month: 'December',
            weekOfTheMonth: 5,
            dayOfTheWeek: 'Saturday'
        };
        expect(result).toEqual(expected);
    });
});