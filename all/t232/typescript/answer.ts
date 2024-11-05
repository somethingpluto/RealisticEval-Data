import { match } from "assert";

function convertHmsToMilliseconds(timeStr: string): number | null {
    /**
     * Convert a time duration string in the format 'XhYminZs' to milliseconds.
     *
     * This function takes a string representing a time duration, where hours, minutes, and seconds
     * are optionally provided, and converts this duration into the equivalent number of milliseconds.
     *
     * @param timeStr - A string representing the time duration, e.g., '1h20min30s'.
     * @returns The equivalent duration in milliseconds, or null if the input is invalid.
     */
    const regex = /^(?:(\d+)h)?(?:(\d+)min)?(?:(\d+)s)?$/;
    const match = timeStr.match(regex);

    if (!match) {
        console.log(`remindme.ts: Cannot convert time string "${timeStr}" to milliseconds!`);
        return null;
    }

    // Extract hours, minutes, and seconds from the regex groups, defaulting to 0 if not present
    const [_, hoursStr, minutesStr, secondsStr] = match;
    const hours = hoursStr ? parseInt(hoursStr, 10) : 0;
    const minutes = minutesStr ? parseInt(minutesStr, 10) : 0;
    const seconds = secondsStr ? parseInt(secondsStr, 10) : 0;

    // Convert to milliseconds
    const totalMilliseconds = (hours * 60 * 60 + minutes * 60 + seconds) * 1000;

    return totalMilliseconds;
}