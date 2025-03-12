import { formatDistance } from 'date-fns';

function formatDate(dateString: string): string {
  const now = new Date();
  const targetDate = new Date(dateString);
  if (isNaN(now.getTime()) || isNaN(targetDate.getTime())) {
    return 'Invalid date';
  }
  return formatDistance(targetDate, now, { addSuffix: true });
}
describe('formatDate', () => {
    beforeAll(() => {
        // Set the system time to a fixed date for consistent testing
        jest.useFakeTimers().setSystemTime(new Date('2024-08-25T12:00:00'));
    });

    afterAll(() => {
        // Restore the real system time after tests
        jest.useRealTimers();
    });

    test('should return "1 day ago" for a date exactly one day before', () => {
        const dateString = '2024-08-24T12:00:00';
        const result = formatDate(dateString);
        expect(['1 day ago', '24 hours ago']).toContain(result)
    });

    test('should return "5 hours ago" for a date 5 hours before the current time', () => {
        const dateString = '2024-08-25T07:00:00';
        const result = formatDate(dateString);
        expect(result).toBe('5 hours ago');
    });

    test('should return "2 minutes ago" for a date 2 minutes before the current time', () => {
        const dateString = '2024-08-25T11:58:00';
        const result = formatDate(dateString);
        expect(result).toBe('2 minutes ago');
    });

    test('should return "just now" for a date within the last second', () => {
        const dateString = '2024-08-25T11:59:59';
        const result = formatDate(dateString);
        expect(['1 second ago', '1 seconds ago']).toContain(result)
    });

});
