/**
 * Converts a date string into a relative time description.
 *
 * @param {string} dateString - The date string to convert.
 * @returns {string} A user-friendly string representing the relative time difference from the current date.
 * @throws {Error} If the date string is invalid.
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    if (isNaN(date.getTime())) {
        throw new Error('Invalid Date');
    }

    const currentDate = new Date();
    const timeDifference = currentDate.getTime() - date.getTime();

    // Calculate time differences in seconds, minutes, hours, and days
    const secondsDifference = Math.floor(timeDifference / 1000);
    const minutesDifference = Math.floor(secondsDifference / 60);
    const hoursDifference = Math.floor(minutesDifference / 60);
    const daysDifference = Math.floor(hoursDifference / 24);

    // Determine and return the appropriate time description
    if (daysDifference > 0) {
        return `${daysDifference} day${daysDifference !== 1 ? "s" : ""} ago`;
    } else if (hoursDifference > 0) {
        return `${hoursDifference} hour${hoursDifference !== 1 ? "s" : ""} ago`;
    } else if (minutesDifference > 0) {
        return `${minutesDifference} minute${minutesDifference !== 1 ? "s" : ""} ago`;
    } else {
        return `${secondsDifference} second${secondsDifference !== 1 ? "s" : ""} ago`;
    }
}