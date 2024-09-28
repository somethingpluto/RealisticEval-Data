function getCurrentDateInfo(testDate = null) {
    /**
     * Returns the current time information including year, month, week of the month, and day of the week.
     * Optionally takes a date object for testing purposes.
     *
     * @param {Date|null} testDate - The date to compute information for, defaults to today's date if not provided.
     * @returns {Object} An object containing the year, month, week of the month, and day of the week.
     */
    const today = testDate ? new Date(testDate) : new Date();

    const year = today.getFullYear();
    const month = today.getMonth(); // 0-indexed
    const dayOfWeek = today.toLocaleString('default', { weekday: 'long' });

    // Calculate the week of the month
    const firstDayOfMonth = new Date(year, month, 1);
    const firstDayWeekday = firstDayOfMonth.getDay(); // 0 = Sunday, 1 = Monday, etc.
    
    // Adjust for 1-indexed days in JavaScript
    const weekOfMonth = Math.floor((today.getDate() + firstDayWeekday) / 7) + 1;

    const monthNames = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];

    return {
        year: year,
        month: monthNames[month],
        week_of_the_month: weekOfMonth,
        day_of_the_week: dayOfWeek
    };
}

// Example usage
console.log(getCurrentDateInfo());