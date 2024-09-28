import { findNthWeekdayOfSpecificYear } from './your-module'; // Adjust the import based on your file structure

describe('findNthWeekdayOfSpecificYear', () => {

    test('regular occurrence', () => {
        // Test for the 2nd Monday of May 2023
        const result = findNthWeekdayOfSpecificYear(2023, 5, 2, 0);
        const expected = new Date(2023, 4, 8); // Months are 0-indexed in JS
        expect(result).toEqual(expected);
    });

    test('last occurrence', () => {
        // Test for the 5th Monday of May 2023, which doesn't exist, should return the last Monday
        const result = findNthWeekdayOfSpecificYear(2023, 5, 5, 0);
        const expected = new Date(2023, 4, 29); // Months are 0-indexed in JS
        expect(result).toEqual(expected);
    });

    test('out of range', () => {
        // Test for the 10th Monday of May 2023, which definitely doesn't exist, should return the last Monday
        const result = findNthWeekdayOfSpecificYear(2023, 5, 10, 0);
        const expected = new Date(2023, 4, 29); // Months are 0-indexed in JS
        expect(result).toEqual(expected);
    });

    test('first day is weekday', () => {
        // Test for when the first day of the month is the weekday in question, 1st Tuesday of August 2023
        const result = findNthWeekdayOfSpecificYear(2023, 8, 1, 1);
        const expected = new Date(2023, 7, 1); // Months are 0-indexed in JS
        expect(result).toEqual(expected);
    });

    test('edge year transition', () => {
        // Test for the 1st Friday of December 2023, checking the transition to a new year boundary condition
        const result = findNthWeekdayOfSpecificYear(2023, 12, 1, 4);
        const expected = new Date(2023, 11, 1); // Months are 0-indexed in JS
        expect(result).toEqual(expected);
    });
});