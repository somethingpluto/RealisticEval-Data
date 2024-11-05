function convertHmsToMilliseconds(timeStr) {
    // Regex to match hours, minutes, and seconds
    const regex = /^(?:(\d+)h)?(?:(\d+)min)?(?:(\d+)s)?$/;
    const match = timeStr.match(regex);

    if (!match) {
        console.log(`remindme.js: Cannot convert time string "${timeStr}" to milliseconds!`);
        return null;
    }

    // Extract hours, minutes, and seconds from the regex groups, defaulting to 0 if not present
    const hours = match[1] ? parseInt(match[1], 10) : 0;
    const minutes = match[2] ? parseInt(match[2], 10) : 0;
    const seconds = match[3] ? parseInt(match[3], 10) : 0;

    // Calculate the total duration in milliseconds
    const totalMilliseconds = (hours * 60 * 60 + minutes * 60 + seconds) * 1000;

    return totalMilliseconds;
}