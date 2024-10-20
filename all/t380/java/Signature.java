import java.util.Arrays;

public class Answer {

    private static final int SECONDS_PER_DAY = 86400;
    private static final int SECONDS_PER_HOUR = 3600;
    private static final int SECONDS_PER_MINUTE = 60;

    /**
     * Calculate the total number of seconds given an array of time periods in the order of
     * days, hours, minutes, and seconds.
     *
     * @param time an array where
     *             time[0] - number of days (optional)
     *             time[1] - number of hours (optional)
     *             time[2] - number of minutes (optional)
     *             time[3] - number of seconds (optional)
     * @return the total number of seconds
     */
    public static int calculateTotalSeconds(int[] time) {
        // Unpacking the time with defaults
        int days = time.length > 0 ? time[0] : 0;
        int hours = time.length > 1 ? time[1] : 0;
        int minutes = time.length > 2 ? time[2] : 0;
        int seconds = time.length > 3 ? time[3] : 0;

        int totalSeconds = (
                days * SECONDS_PER_DAY +
                hours * SECONDS_PER_HOUR +
                minutes * SECONDS_PER_MINUTE +
                seconds
        );

        return totalSeconds;
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(calculateTotalSeconds(new int[]{1, 2, 3, 4})); // Output: 93784
        System.out.println(calculateTotalSeconds(new int[]{0, 2, 3}));    // Output: 7380
    }
}