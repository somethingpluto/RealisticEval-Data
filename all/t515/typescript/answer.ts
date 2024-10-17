import { moment } from 'moment-timezone';

/**
 * Converts a date string from the format '%a, %d %b %Y %H:%M:%S %z (%Z)'
 * to the format '%Y-%m-%d_%H:%M:%S'.
 *
 * @param dateStr - The input date string.
 * @returns The formatted date string in the format '%Y-%m-%d_%H:%M:%S', or null if the input date string is invalid.
 */
function formatDateString(dateStr: string): string | null {
    try {
        // Convert to a moment object using the specified format
        const dateObject = moment(dateStr, 'ddd, DD MMM YYYY HH:mm:ss ZZ (Z)', true);

        if (!dateObject.isValid()) {
            throw new Error('Invalid date format');
        }

        // Convert to the desired output format
        const formattedDate = dateObject.format('YYYY-MM-DD_HH:mm:ss');

        return formattedDate;
    } catch (error) {
        console.error(`Error parsing date: ${error}`);
        return null;
    }
}