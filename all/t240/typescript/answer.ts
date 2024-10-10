function genTimeoutDuration(timeString: string): Duration {
    /**
     * Converts a time duration string into a moment.Duration object.
     * The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
     * e.g. "1d 2h 3m 4s 500ms"
     * Each unit should be specified by an integer followed by its corresponding unit letter.
     *
     * @param timeString - A string representing the time duration.
     * @returns A moment.Duration object representing the input duration.
     */

    const regex = /(\d+)([dhms])/g;
    let match;
    let duration = Duration(0);

    while ((match = regex.exec(timeString)) !== null) {
        const value = parseInt(match[1], 10);
        const unit = match[2];

        switch(unit) {
            case 'd':
                duration.add(value, 'days');
                break;
            case 'h':
                duration.add(value, 'hours');
                break;
            case 'm':
                duration.add(value, 'minutes');
                break;
            case 's':
                duration.add(value, 'seconds');
                break;
            default:
                throw new Error(`Unknown time unit: ${unit}`);
        }
    }

    return duration;
}