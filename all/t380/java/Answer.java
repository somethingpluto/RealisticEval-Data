package org.real.temp;

public class Answer {

    /**
     * Calculate the total number of seconds given an array of time periods in the order of
     * days, hours, minutes, and seconds.
     *
     * @param time array where
     *             time[0] - number of days (optional)
     *             time[1] - number of hours (optional)
     *             time[2] - number of minutes (optional)
     *             time[3] - number of seconds (optional)
     * @return total number of seconds
     *
     * Examples:
     *     calculateTotalSeconds(new int[]{1, 2, 3, 4}) returns 93784
     *     calculateTotalSeconds(new int[]{0, 2, 3}) returns 7380
     */
    public static int calculateTotalSeconds(int[] time) {
        int totalSeconds = 0;

        if (time.length > 0) {
            totalSeconds += time[0] * 24 * 60 * 60; // Convert days to seconds
        }
        if (time.length > 1) {
            totalSeconds += time[1] * 60 * 60; // Convert hours to seconds
        }
        if (time.length > 2) {
            totalSeconds += time[2] * 60; // Convert minutes to seconds
        }
        if (time.length > 3) {
            totalSeconds += time[3]; // Add remaining seconds
        }

        return totalSeconds;
    }
}