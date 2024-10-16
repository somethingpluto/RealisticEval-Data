function getDaysInMonth(year: number, month: number): number {
    // Check if the month is valid
    if (month < 1 || month > 12) {
        throw new Error("Month must be between 1 and 12.");
    }

    // Array of days in each month; index 0 is unused, 1-12 corresponds to Jan-Dec
    const daysInMonth: number[] = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    // Handle February's case
    if (month === 2) {
        // Determine if it is a leap year
        if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
            return 29; // Leap year
        } else {
            return 28; // Non-leap year
        }
    }

    // Return the number of days for the specified month
    return daysInMonth[month];
}