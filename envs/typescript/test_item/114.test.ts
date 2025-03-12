import { DateTime } from 'luxon';

function sortByTimestamp(array: Array<{ timestamp: string }>): Array<{ timestamp: string }> {
  return array.sort((a, b) => {
    const dateTimeA = DateTime.fromISO(a.timestamp);
    const dateTimeB = DateTime.fromISO(b.timestamp);
    return dateTimeA.diff(dateTimeB, 'milliseconds').milliseconds;
  });
}
describe('sortByTimestamp function', () => {
    test('should return an empty array when input is empty', () => {
        expect(sortByTimestamp([])).toEqual([]);
    });

    test('should correctly handle an array with a single element', () => {
        const singleElementArray: Array<{ id: number; timestamp: string }> = [{ id: 1, timestamp: "2021-07-03T12:00:00Z" }];
        expect(sortByTimestamp(singleElementArray)).toEqual([{ id: 1, timestamp: "2021-07-03T12:00:00Z" }]);
    });

    test('should sort an array of objects by timestamps correctly', () => {
        const testData: Array<{ id: number; timestamp: string }> = [
            { id: 3, timestamp: "2021-07-01T09:45:00Z" },
            { id: 1, timestamp: "2021-07-03T12:00:00Z" },
            { id: 2, timestamp: "2021-07-02T15:30:00Z" }
        ];
        const expected: Array<{ id: number; timestamp: string }> = [
            { id: 3, timestamp: "2021-07-01T09:45:00Z" },
            { id: 2, timestamp: "2021-07-02T15:30:00Z" },
            { id: 1, timestamp: "2021-07-03T12:00:00Z" }
        ];
        expect(sortByTimestamp(testData)).toEqual(expected);
    });

    test('should not alter array if already sorted', () => {
        const sortedArray: Array<{ id: number; timestamp: string }> = [
            { id: 1, timestamp: "2021-07-01T09:45:00Z" },
            { id: 2, timestamp: "2021-07-02T15:30:00Z" },
            { id: 3, timestamp: "2021-07-03T12:00:00Z" }
        ];
        expect(sortByTimestamp(sortedArray)).toEqual(sortedArray);
    });

    test('should handle mixed format timestamps correctly', () => {
        const mixedFormats: Array<{ id: number; timestamp: string }> = [
            { id: 1, timestamp: "2021/07/03 12:00:00" },
            { id: 2, timestamp: "July 2, 2021 15:30:00" },
            { id: 3, timestamp: "2021-07-01T09:45:00Z" }
        ];
        const expected: Array<{ id: number; timestamp: string }> = [
            { id: 3, timestamp: "2021-07-01T09:45:00Z" },
            { id: 2, timestamp: "July 2, 2021 15:30:00" },
            { id: 1, timestamp: "2021/07/03 12:00:00" }
        ];
        expect(sortByTimestamp(mixedFormats)).toEqual(expected);
    });
});
