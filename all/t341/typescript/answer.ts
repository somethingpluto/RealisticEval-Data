/**
 * Converts a time string in the format "XhYmZs" (hours, minutes, seconds) into milliseconds.
 * 
 * @param str The input string representing the time duration.
 * @returns The time in milliseconds.
 * @throws Error if the input string does not match the expected format.
 */
const convertTimeHmsStringToMs = (str: string): number => {
    // Regular expression to parse the string for hours, minutes, and seconds
    const regex = /(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?/;
    const match = str.match(regex);
    
    // Throw an error if the string does not match the expected format
    if (!match) {
        throw new Error(`Cannot convert hms string "${str}" to ms!`);
    }

    // Parse hours, minutes, and seconds, defaulting to 0 if any group is missing
    const hours = parseInt(match[1] || '0', 10);
    const minutes = parseInt(match[2] || '0', 10);
    const seconds = parseInt(match[3] || '0', 10);

    // Calculate the total milliseconds
    const totalMilliseconds = ((hours * 60 + minutes) * 60 + seconds) * 1000;
    return totalMilliseconds;
};