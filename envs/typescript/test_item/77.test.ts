import { format } from 'date-fns-tz';

/**
 * Formats the given timestamp as a string according to the specified format, using the system's local time zone.
 * ...
 */

function formatTimestampToString(timestamp: number, date_format: string = 'ccc LLL d hh:mm:ss a zzzz yyyy'): string {
  const localDate = new Date(timestamp * 1000);
  return format(localDate, date_format, { timeZone: 'local' });
}
describe('TestFormatTimestampToString', () => {
    describe('test_basic_functionality', () => {
        it('should correctly format the timestamp', () => {
            const timestamp = 1655364000.0; // Corresponds to Thu Jun 16 12:00:00 PM UTC 2022
            const expectedDateStr = 'Thu Jun 16 03:20:00 PM +0800 2022';
            expect(formatTimestampToString(timestamp)).toBe(expectedDateStr);
        });
    });

    describe('test_default_format', () => {
        it('default format should match the expected date string', () => {
            const timestamp = 1655364000.0;
            const expectedDateStr = 'Thu Jun 16 03:20:00 PM +0800 2022';
            expect(formatTimestampToString(timestamp)).toBe(expectedDateStr);
        });
    });

    describe('test_custom_format', () => {
        it('should correctly format the timestamp using the custom format', () => {
            const timestamp = 1655364000.0;
            const customFormat = 'yyyy-MM-dd HH:mm:ss';
            const expectedDateStr = '2022-06-16 15:20:00';
            expect(formatTimestampToString(timestamp, customFormat)).toBe(expectedDateStr);
        });
    });

    describe('test_edge_case_boundary_value', () => {
        it('should correctly format the Unix epoch start time', () => {
            const timestamp = 0.0; // Unix epoch start
            const expectedDateStr = 'Thu Jan 01 08:00:00 AM +0800 1970';
            expect(formatTimestampToString(timestamp)).toBe(expectedDateStr);
        });
    });
});
