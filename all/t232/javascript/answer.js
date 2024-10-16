function convertHmsToMilliseconds(timeStr) {
    // Regular expression to match the pattern XhYminZs
    const regex = /^(\d+)(?:h)?(\d+)(?:min)?(\d+)(?:s)?$/;

    // Match the input string with the regular expression
    const match = timeStr.match(regex);

    // If there is no match, return null
    if (!match) {
        return null;
    }

    // Extract hours, minutes, and seconds from the matched groups
    let [_, hours, minutes, seconds] = match;

    // Convert the extracted values to integers
    hours = parseInt(hours, 10);
    minutes = parseInt(minutes, 10);
    seconds = parseInt(seconds, 10);

    // Calculate the total milliseconds
    const milliseconds = (hours * 60 * 60 + minutes * 60 + seconds) * 1000;

    // Return the calculated milliseconds
    return milliseconds;
}