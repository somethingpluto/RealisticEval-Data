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
        expect(result).toBe('Day: -2 Hour: -5 Minutes: -45'); // 2 days, 5 hours, 45 minutes in the future
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
// Written by ChatGPT

/**
 * Get the time difference between now and a target date
 * @param {Date} targetDate The target date to compare against
 * @returns {string} A human-readable string representing the time difference
 */

export default function getTimeDifferenceText(targetDate) {
    const now = new Date();
    const difference = targetDate - now;
  
    const minutes = Math.floor((difference / 1000 / 60) % 60);
    const hours = Math.floor((difference / (1000 * 60 * 60)) % 24);
    const days = Math.floor(difference / (1000 * 60 * 60 * 24));
  
    const timeSegments = [];
    if (days > 0) {
      timeSegments.push(days + " days");
    }
    if (hours > 0) {
      timeSegments.push(hours + " hours");
    }
    if (minutes > 0) {
      timeSegments.push(minutes + " minutes");
    }
  
    // Add "and" before the last item in the array
    if (timeSegments.length > 1) {
      const lastSegment = timeSegments.pop();
      timeSegments.push("and " + lastSegment);
    }
  
    return timeSegments.join(", ");
  }