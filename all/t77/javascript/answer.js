const { DateTime, ZoneInfo } = require('luxon');

function formatDateTimeStr(mtime, format = 'ccc LLL d hh:mm:ss a zzzz yyyy') {
    /**
     * Convert a UNIX timestamp to a formatted datetime string using the system's local timezone.
     *
     * @param {number} mtime - UNIX timestamp.
     * @param {string} format - Format string for `toFormat`.
     *
     * @returns {string} - Formatted datetime string.
     */
    if (mtime < 0) {
        throw new Error("error mtime");
    }

    try {
        // Get the local system timezone
        const localTz = ZoneInfo.get('local');
    } catch (error) {
        // Fallback to UTC if the local timezone is not found
        const localTz = ZoneInfo.get('UTC');
    }

    try {
        // Convert the UNIX timestamp to a datetime object with timezone
        const dt = DateTime.fromSeconds(mtime).setZone(localTz);
        // Return the formatted datetime string
        return dt.toFormat(format);
    } catch (error) {
        // Handle any other unexpected errors
        throw new Error(`Error formatting the datetime: ${error.message}`);
    }
}
