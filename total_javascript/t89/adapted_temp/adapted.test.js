// Import the updateClock function if it's in another file
// const updateClock = require('./path_to_your_file');

describe('getMinuteAndSecondSinceTime', () => {
    test('should correctly format the time for zero elapsed time', () => {
        const startTime = new Date().getTime();
        expect(getMinuteAndSecondSinceTime(startTime)).toBe('00:00');
    });

    test('should correctly format the time for exactly one minute', () => {
        const startTime = new Date().getTime() - 60000; // 1 minute ago
        expect(getMinuteAndSecondSinceTime(startTime)).toBe('01:00');
    });

    test('should correctly format the time when seconds are less than 10', () => {
        const startTime = new Date().getTime() - 65000; // 1 minute and 5 seconds ago
        expect(getMinuteAndSecondSinceTime(startTime)).toBe('01:05');
    });

    test('should handle edge case where minutes and seconds are just below 10', () => {
        const startTime = new Date().getTime() - 605000; // 10 minutes and 5 seconds ago
        expect(getMinuteAndSecondSinceTime(startTime)).toBe('10:05');
    });

    test('should handle long duration times correctly', () => {
        const startTime = new Date().getTime() - 3600000; // 1 hour ago
        const minutes = Math.floor(3600000 / 60000);
        const formattedMinutes = minutes < 10 ? '0' + minutes : minutes.toString();
        expect(getMinuteAndSecondSinceTime(startTime)).toBe(`${formattedMinutes}:00`);
    });
});

// Function to update the clock display by calculating the elapsed time since a given start time
function getMinuteAndSecondSinceTime(startTime) {
    // Get the current time in milliseconds
    const currentTime = new Date().getTime();

    // Calculate the elapsed time in milliseconds
    const elapsedTime = currentTime - startTime;

    // Convert elapsed time to minutes and seconds
    let minutes = Math.floor(elapsedTime / 60000); // 60000 ms in 1 minute
    let seconds = Math.floor((elapsedTime % 60000) / 1000); // Remaining milliseconds converted to seconds

    // Add leading zeros to minutes and seconds if they are less than 10
    minutes = (minutes < 10) ? '0' + minutes : minutes;
    seconds = (seconds < 10) ? '0' + seconds : seconds;

    // Return the formatted time string in mm:ss format
    return minutes + ":" + seconds;
}