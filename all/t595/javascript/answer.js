
function getDaysInMonth(year, month) {
    // Array storing the number of days in each month (index 0 is unused)
    const daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    // Validate month input
    if (month < 1 || month > 12) {
        throw new RangeError("Month must be between 1 and 12");
    }

    // Adjust for leap years if the month is February (month === 2)
    if (month === 2) {
        const isLeapYear = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
        return isLeapYear ? 29 : 28; // Return 29 if leap year, otherwise 28
    }

    // Return the number of days in the specified month
    return daysInMonth[month];
}