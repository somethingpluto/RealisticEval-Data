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
