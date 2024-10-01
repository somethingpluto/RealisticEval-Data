/**
 * Gets the current time formatted as 'hh:mm AM/PM'.
 *
 * @returns {string} The formatted time string.
 */
function getTime() {
    // Create a new Date object representing the current date and time
    const currentDate = new Date();

    // Define options for time formatting
    const options = {
        hour12: true,     // Use 12-hour format (AM/PM)
        hour: 'numeric',  // Display hour in numeric format
        minute: 'numeric' // Display minutes in numeric format
    };

    // Return the formatted time string using the default locale
    const timeString = currentDate.toLocaleTimeString('en-US', options);
    return timeString;
}
