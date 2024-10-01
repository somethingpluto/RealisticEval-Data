/**
 * Gets the current time formatted as 'hh:mm AM/PM'.
 *
 * @returns {string} The formatted time string.
 */
function getTime() {
    const currentDate = new Date();
    const options = {
        hour12: true,
        hour: 'numeric',
        minute: 'numeric'
    };
    return currentDate.toLocaleTimeString('en-US', options);
}