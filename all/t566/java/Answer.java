import java.util.Date;
import java.util.Calendar;

public class DateUtils {

    /**
     * Checks if two timestamps correspond to the same day.
     *
     * @param timestamp1 - The first timestamp to compare.
     * @param timestamp2 - The second timestamp to compare.
     * @return True if both timestamps are on the same day, false otherwise.
     */
    public static boolean isSameDay(long timestamp1, long timestamp2) {
        // Create Calendar instances for both timestamps
        Calendar calendar1 = Calendar.getInstance();
        calendar1.setTime(new Date(timestamp1));

        Calendar calendar2 = Calendar.getInstance();
        calendar2.setTime(new Date(timestamp2));

        // Compare the year, month, and date of both Calendar objects
        return (calendar1.get(Calendar.YEAR) == calendar2.get(Calendar.YEAR)) &&
               (calendar1.get(Calendar.MONTH) == calendar2.get(Calendar.MONTH)) &&
               (calendar1.get(Calendar.DAY_OF_MONTH) == calendar2.get(Calendar.DAY_OF_MONTH));
    }
}