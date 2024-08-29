/**
 * Converts an ISO 8601 duration string into a more readable format.
 * 
 * @param {string} duration - The ISO 8601 duration string (e.g., "PT1H23M45.678S").
 * @returns {string} A human-readable duration string (e.g., "1h23m45s678ms").
 */
function convertTime(duration) {
    const regex = /PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)(\.\d+)?S)?/;
    const matches = duration.match(regex);

    if (!matches) return ''; // Return an empty string if the input doesn't match the expected format

    const [ , hours, minutes, seconds, fractionalSeconds ] = matches;
    let convertedTime = '';

    if (hours) {
        convertedTime += `${hours}h`;
    }

    if (minutes) {
        convertedTime += `${minutes}m`;
    }

    if (seconds) {
        convertedTime += `${seconds}s`;
    }

    if (fractionalSeconds) {
        const milliseconds = Math.round(parseFloat(fractionalSeconds) * 1000);
        if (milliseconds > 0) {
            convertedTime += `${milliseconds}ms`;
        }
    }

    return convertedTime;
}
