// Import the updateClock function if it's in another file
// const updateClock = require('./path_to_your_file');

describe('getMinuteAndSecondSinceTime', () => {
    test('should correctly format the time for zero elapsed time', () => {
        const startTime = new Date().getTime();
        expect(updateClock(startTime)).toBe('00:00');
    });

    test('should correctly format the time for exactly one minute', () => {
        const startTime = new Date().getTime() - 60000; // 1 minute ago
        expect(updateClock(startTime)).toBe('01:00');
    });

    test('should correctly format the time when seconds are less than 10', () => {
        const startTime = new Date().getTime() - 65000; // 1 minute and 5 seconds ago
        expect(updateClock(startTime)).toBe('01:05');
    });

    test('should handle edge case where minutes and seconds are just below 10', () => {
        const startTime = new Date().getTime() - 605000; // 10 minutes and 5 seconds ago
        expect(updateClock(startTime)).toBe('10:05');
    });

    test('should handle long duration times correctly', () => {
        const startTime = new Date().getTime() - 3600000; // 1 hour ago
        const minutes = Math.floor(3600000 / 60000);
        const formattedMinutes = minutes < 10 ? '0' + minutes : minutes.toString();
        expect(updateClock(startTime)).toBe(`${formattedMinutes}:00`);
    });
});