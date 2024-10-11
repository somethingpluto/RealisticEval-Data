/**
 * Convert a time duration string in the format 'XhYminZs' to milliseconds.
 *
 * This function takes a string representing a time duration, where hours, minutes, and seconds
 * are optionally provided, and converts this duration into the equivalent number of milliseconds.
 *
 * @param {string} timeStr - A string representing the time duration, e.g., '1h20min30s'.
 * @returns {(number | null)} The equivalent duration in milliseconds, or null if the input is invalid.
 */
function convertHmsToMilliseconds(timeStr: string): number | null {
    const regex = /^(\d+)h(\d+)min(\d+)s$/;
    const matches = timeStr.match(regex);

    if (!matches) {
        return null; // Return null for invalid input
    }

    // Extract hours, minutes, and seconds from the matched groups
    const [hours, minutes, seconds] = matches.slice(1).map(Number);

    // Calculate total milliseconds
    const milliseconds = (hours * 60 * 60 + minutes * 60 + seconds) * 1000;

    return milliseconds;
}