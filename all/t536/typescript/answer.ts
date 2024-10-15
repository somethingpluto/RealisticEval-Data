/**
 * Gets the current date formatted as 'Month Day, Year'.
 *
 * @returns {string} The formatted date string.
 */
function getDate(): string {
    // Create a new Date object representing the current date and time
    const currentDate: Date = new Date();

    // Define options for date formatting
    const options: Intl.DateTimeFormatOptions = {
        year: 'numeric',  // Full numeric year (e.g., 2024)
        month: 'long',    // Full month name (e.g., October)
        day: 'numeric'    // Day of the month (e.g., 1)
    };

    return currentDate.toLocaleString('en', options);
}