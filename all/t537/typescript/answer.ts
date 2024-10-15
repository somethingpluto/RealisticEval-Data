/**
 * Gets the current time formatted as 'hh:mm AM/PM'.
 *
 * @returns {string} The formatted time string.
 */
function getTime(): string {
    const currentDate: Date = new Date();
    const options: Intl.DateTimeFormatOptions = {
        hour12: true,
        hour: 'numeric',
        minute: 'numeric'
    };
    return currentDate.toLocaleTimeString('en-US', options);
}