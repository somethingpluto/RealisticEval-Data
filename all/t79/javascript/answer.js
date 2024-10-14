function dateRangeString(start_date, end_date) {
    /**
     * Generate a formatted date range string.
     *
     * @param {string} start_date - The start date in 'YYYY-MM-DD' format.
     * @param {string} end_date - The end date in 'YYYY-MM-DD' format.
     * @returns {string} A string representing the date range in a human-readable format.
     * @throws {Error} If the start_date or end_date are not in the correct format or if start_date is after end_date.
     */
    try {
        const startDt = new Date(start_date);
        const endDt = new Date(end_date);

        // Check if the dates are valid
        if (isNaN(startDt.getTime()) || isNaN(endDt.getTime())) {
            throw new Error("Date must be in 'YYYY-MM-DD' format.");
        }

        // Check if start_date is after end_date
        if (startDt > endDt) {
            throw new Error("start_date cannot be after end_date.");
        }

        const startMonth = getFullMonthName(startDt.getMonth());
        const endMonth = getFullMonthName(endDt.getMonth());
        const startDay = startDt.getDate().toString();
        const endDay = endDt.getDate().toString();
        const startYear = startDt.getFullYear().toString();
        const endYear = endDt.getFullYear().toString();

        // Format output based on whether dates are within the same month and/or year
        if (startYear !== endYear) {
            return `${startMonth} ${startDay}, ${startYear} to ${endMonth} ${endDay}, ${endYear}`;
        } else if (startMonth === endMonth) {
            return `${startMonth} ${startDay} to ${endDay}, ${startYear}`;
        } else {
            return `${startMonth} ${startDay} to ${endMonth} ${endDay}, ${startYear}`;
        }
    } catch (e) {
        throw new Error(`Date must be in 'YYYY-MM-DD' format. ${e.message}`);
    }
}

function getFullMonthName(monthIndex) {
    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    return months[monthIndex];
}