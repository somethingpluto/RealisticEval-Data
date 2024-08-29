// Test case 1: Full ISO 8601 duration with hours, minutes, and seconds including milliseconds
console.log(convertTime('PT1H23M45.678S')); 
// Expected output: "1h23m45s678ms"

// Test case 2: Duration with only minutes and seconds including milliseconds
console.log(convertTime('PT0M30.123S'));    
// Expected output: "30s123ms"

// Test case 3: Duration with only seconds and milliseconds
console.log(convertTime('PT45.5S'));        
// Expected output: "45s500ms"

// Test case 4: Duration with hours and minutes, but no seconds
console.log(convertTime('PT2H5M'));         
// Expected output: "2h5m"

// Test case 5: Duration with only seconds, no milliseconds
console.log(convertTime('PT20S'));          
// Expected output: "20s"

/**
 * Converts an ISO 8601 duration string into a more readable format.
 * 
 * @param {string} duration - The ISO 8601 duration string (e.g., "PT1H23M45.678S").
 * @returns {string} A human-readable duration string (e.g., "1h23m45s678ms").
 */
function convertTime(duration) {
    const regex = /PT(?:(\d+)H)?(?:(\d+)M)?([\d.]+)S/;
    const matches = duration.match(regex);

    if (!matches) return ''; // Return an empty string if the input doesn't match the expected format

    const [ , hours, minutes, seconds ] = matches;
    let convertedTime = '';

    if (hours) {
        convertedTime += `${hours}h`;
    }

    if (minutes) {
        convertedTime += `${minutes}m`;
    }

    if (seconds) {
        const [wholeSeconds, milliseconds] = seconds.split('.').map(Number);

        convertedTime += `${wholeSeconds}s`;

        if (milliseconds) {
            convertedTime += `${Math.round(milliseconds * Math.pow(10, 3 - milliseconds.toString().length))}ms`;
        }
    }

    return convertedTime;
}
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
