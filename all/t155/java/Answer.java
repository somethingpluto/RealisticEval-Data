import java.util.Date;

public class TimestampUtil {

    /**
     * Computes the difference between the specified date and the current time, returning it in a human-readable way.
     *
     * @param createdAt - The date to calculate the time difference from.
     * @return A string indicating the time elapsed, e.g., "3 days ago", "5 hours ago".
     */
    public static String getTimestamp(Date createdAt) {
        long now = System.currentTimeMillis();
        long diffInSeconds = (now - createdAt.getTime()) / 1000;

        // Define time intervals in seconds
        long year = 31536000;
        long month = 2592000;
        long week = 604800;
        long day = 86400;
        long hour = 3600;
        long minute = 60;

        long intervalCount;
        String intervalUnit;

        if (diffInSeconds >= year) {
            intervalCount = diffInSeconds / year;
            intervalUnit = intervalCount == 1 ? "year" : "years";
        } else if (diffInSeconds >= month) {
            intervalCount = diffInSeconds / month;
            intervalUnit = intervalCount == 1 ? "month" : "months";
        } else if (diffInSeconds >= week) {
            intervalCount = diffInSeconds / week;
            intervalUnit = intervalCount == 1 ? "week" : "weeks";
        } else if (diffInSeconds >= day) {
            intervalCount = diffInSeconds / day;
            intervalUnit = intervalCount == 1 ? "day" : "days";
        } else if (diffInSeconds >= hour) {
            intervalCount = diffInSeconds / hour;
            intervalUnit = intervalCount == 1 ? "hour" : "hours";
        } else if (diffInSeconds >= minute) {
            intervalCount = diffInSeconds / minute;
            intervalUnit = intervalCount == 1 ? "minute" : "minutes";
        } else {
            intervalCount = diffInSeconds;
            intervalUnit = intervalCount == 1 ? "second" : "seconds";
        }

        return intervalCount + " " + intervalUnit + " ago";
    }
}