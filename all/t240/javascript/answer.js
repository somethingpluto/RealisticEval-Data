function genTimeoutDuration(timeString) {
    /**
     * Converts a time duration string into a moment.duration object.
     * The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
     * eg. "1d 2h 3m 4s 500ms"
     * Each unit should be specified by an integer followed by its corresponding unit letter.
     *
     * @param {string} timeString - A string representing the time duration.
     * @returns {moment.duration} - A moment.duration object representing the input duration.
     */

    // Define an object to hold all our values
    const timeValues = { d: 0, h: 0, m: 0, s: 0, ms: 0 };

    // Regular expression to find all parts of the time string
    const parts = timeString.match(/(\d+)([dhms]{1,2})/g);

    // Process each found part
    parts.forEach(part => {
        const match = part.match(/(\d+)([dhms]{1,2})/);
        const amount = parseInt(match[1], 10);
        const unit = match[2];

        if (unit === 'd') {
            timeValues.d += amount;
        } else if (unit === 'h') {
            timeValues.h += amount;
        } else if (unit === 'm') {
            timeValues.m += amount;
        } else if (unit === 's') {
            timeValues.s += amount;
        } else if (unit === 'ms') {
            timeValues.ms += amount;
        }
    });

    // Create a moment.duration object using the extracted values
    return moment.duration({
        days: timeValues.d,
        hours: timeValues.h,
        minutes: timeValues.m,
        seconds: timeValues.s,
        milliseconds: timeValues.ms
    });
}