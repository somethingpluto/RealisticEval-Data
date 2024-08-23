/**
 * Gets the current date and returns it as YYYY-MM-DD
 *
 * @returns {string} The current date formatted as YYYY-MM-DD.
 */
function getCurrentDate() {
    const currentDate = new Date();

    // Convert the current date to ISO string format and extract the date part (YYYY-MM-DD)
    return currentDate.toISOString().split('T')[0];
}
