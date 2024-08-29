// Test Case 1: Current time is exactly at the start time.
console.log(isBreakTime("09:00", "10:00", "09:00")); // Expected output: true

// Test Case 2: Current time is within the break time range.
console.log(isBreakTime("09:00", "10:00", "09:30")); // Expected output: true

// Test Case 3: Current time is exactly at the end time.
console.log(isBreakTime("09:00", "10:00", "10:00")); // Expected output: true

// Test Case 4: Current time is before the break time.
console.log(isBreakTime("09:00", "10:00", "08:59")); // Expected output: false

// Test Case 5: Current time is after the break time.
console.log(isBreakTime("09:00", "10:00", "10:01")); // Expected output: false

/**
 * Determines if the current time falls within the break time range.
 * 
 * @param {string} startTime - The start time of the break in HH:MM format.
 * @param {string} endTime - The end time of the break in HH:MM format.
 * @param {string} currentTime - The current time in HH:MM format.
 * @returns {boolean} - Returns true if the current time is within the break time range, false otherwise.
 */
function isBreakTime(startTime, endTime, currentTime) {
    const [startHour, startMinute] = startTime.split(':').map(Number);
    const [endHour, endMinute] = endTime.split(':').map(Number);
    const [currentHour, currentMinute] = currentTime.split(':').map(Number);

    const startTotalMinutes = startHour * 60 + startMinute;
    const endTotalMinutes = endHour * 60 + endMinute;
    const currentTotalMinutes = currentHour * 60 + currentMinute;

    return currentTotalMinutes >= startTotalMinutes && currentTotalMinutes <= endTotalMinutes;
}
