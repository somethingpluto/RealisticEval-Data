function calculateTotalSeconds(time: [number, number?, number?, number?]): number {
    /**
     * Calculate the total number of seconds given a tuple or array of time periods in the order of
     * days, hours, minutes, and seconds.
     *
     * @param time: tuple or array, where
     *     time[0] - number of days (optional)
     *     time[1] - number of hours (optional)
     *     time[2] - number of minutes (optional)
     *     time[3] - number of seconds (optional)
     * @return: number, total number of seconds
     */

    let totalSeconds = 0;

    if (time.length > 0) {
        totalSeconds += time[0]! * 24 * 60 * 60; // days
    }

    if (time.length > 1) {
        totalSeconds += time[1]! * 60 * 60; // hours
    }

    if (time.length > 2) {
        totalSeconds += time[2]! * 60; // minutes
    }

    if (time.length > 3) {
        totalSeconds += time[3]!; // seconds
    }

    return totalSeconds;
}