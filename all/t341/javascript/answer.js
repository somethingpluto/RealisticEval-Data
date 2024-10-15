/**
 * Converts a time string in the format "XhYmZs" (hours, minutes, seconds) into milliseconds.
 *
 * @param str The input string representing the time duration.
 * @returns The time in milliseconds.
 * @throws Error if the input string does not match the expected format.
 */
const convertTimeHmsStringToMs = (str) => {
    const regex = /(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/;
    const match = str.match(regex);

    if (!match) {
        throw new Error(`Cannot convert hms string "${str}" to ms!`);
    }

    const hours = parseInt(match[1] || '0', 10);
    const minutes = parseInt(match[2] || '0', 10);
    const seconds = parseInt(match[3] || '0', 10);

    const totalMilliseconds = ((hours * 60 + minutes) * 60 + seconds) * 1000;
    return totalMilliseconds;
};