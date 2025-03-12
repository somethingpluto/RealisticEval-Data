/**
 * Generates a string based on the entered start and end dates. If the start date and end date are in the same month,
 * only one month will be displayed. If not, the start and end months will be displayed separately. For example, if you
 * enter the start date and end date as "2023-08-01" and "2023-08-15" respectively, you will finally output "August 1 to 15, 2023".
 *
 * @param {string} start_date - The start date in 'YYYY-MM-DD' format.
 * @param {string} end_date - The end date in 'YYYY-MM-DD' format.
 * @returns {string} A string representing the date range in a human-readable format.
 * @throws {Error} If the start_date or end_date are not in the correct format or if start_date is after end_date.
 */
function dateRangeString(start_date, end_date) {
    // Helper function to validate date format
    function isValidDate(dateString) {
        const regex = /^\d{4}-\d{2}-\d{2}$/;
        if (!regex.test(dateString)) return false;
        const date = new Date(dateString);
        return date instanceof Date && !isNaN(date);
    }

    // Helper function to get month name from month number
    function getMonthName(month) {
        const monthNames = ["January", "February", "March", "April", "May", "June", 
                            "July", "August", "September", "October", "November", "December"];
        return monthNames[month];
    }

    // Validate input dates
    if (!isValidDate(start_date) || !isValidDate(end_date)) {
        throw new Error("Invalid date format. Dates must be in 'YYYY-MM-DD' format.");
    }

    const startDate = new Date(start_date);
    const endDate = new Date(end_date);

    if (startDate > endDate) {
        throw new Error("Start date cannot be after end date.");
    }

    const startYear = startDate.getFullYear();
    const startMonth = startDate.getMonth();
    const startDay = startDate.getDate();

    const endYear = endDate.getFullYear();
    const endMonth = endDate.getMonth();
    const endDay = endDate.getDate();

    const startMonthName = getMonthName(startMonth);
    const endMonthName = getMonthName(endMonth);

    if (startYear === endYear && startMonth === endMonth) {
        return `${startMonthName} ${startDay} to ${endDay}, ${startYear}`;
    } else {
        return `${startMonthName} ${startDay}, ${startYear} to ${endMonthName} ${endDay}, ${endYear}`;
    }
}
describe('TestDateRangeString', () => {
    it('should correctly format dates within the same month', () => {
        const result = dateRangeString("2023-08-01", "2023-08-15");
        expect(result).toBe("August 1 to 15, 2023");
    });

    it('should correctly format dates within the same month (start to end)', () => {
        const result = dateRangeString("2023-08-01", "2023-08-31");
        expect(result).toBe("August 1 to 31, 2023");
    });

    it('should correctly format dates across different months within the same year', () => {
        const result = dateRangeString("2023-08-30", "2023-09-05");
        expect(result).toBe("August 30, 2023 to September 5, 2023");
    });

    it('should correctly format dates across different years', () => {
        const result = dateRangeString("2023-12-30", "2024-01-02");
        expect(result).toBe("December 30, 2023 to January 2, 2024");
    });
});
