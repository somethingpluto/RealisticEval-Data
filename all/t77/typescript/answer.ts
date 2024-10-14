import { DateTime, Zone } from 'luxon';

function formatDateTimeStr(mtime: number, format: string = 'ccc LLL d hh:mm:ss a zzzz yyyy'): string {
    /**
     * Convert a UNIX timestamp to a formatted datetime string using the system's local timezone.
     *
     * @param mtime - UNIX timestamp.
     * @param format - Format string for `toFormat`.
     * @returns Formatted datetime string.
     */
    if (mtime < 0) {
        throw new Error('error mtime');
    }

    try {
        // Get the local system timezone
        const localTz = Zone.local;

        // Convert the UNIX timestamp to a datetime object with timezone
        const dt = DateTime.fromMillis(mtime * 1000).setZone(localTz);

        // Return the formatted datetime string
        return dt.toFormat(format);
    } catch (e) {
        // Handle any other unexpected errors
        throw new Error(`Error formatting the datetime: ${e}`);
    }
}