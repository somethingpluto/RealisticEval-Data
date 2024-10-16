function getDaysInMonth(year, month) {
    // Check if month is valid
    if (month < 1 || month > 12) {
        throw new Error("Month must be between 1 and 12.");
    }

    // Array of days in each month, index 0 is unused
    const daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    // Handle February
    if (month === 2) {
        // Check for leap year
        if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
            return 29; // Leap year
        } else {
            return 28; // Non-leap year
        }
    }

    // Return the number of days for the month
    return daysInMonth[month];
}