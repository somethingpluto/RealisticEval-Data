import java.util.Calendar;
import java.util.Date;
import java.text.SimpleDateFormat;

public class DateUtils {
    public static String getRelativeTime(Date messageDate) {
        Date now = new Date();
        long timeDifference = now.getTime() - messageDate.getTime();

        long oneDay = 1000 * 60 * 60 * 24; // milliseconds in one day
        long daysDifference = timeDifference / oneDay;

        Calendar calendar = Calendar.getInstance();
        calendar.setTime(messageDate);
        int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);

        if (daysDifference == 0) {
            return "Today";
        } else if (daysDifference == 1) {
            return "Yesterday";
        } else if (daysDifference < 7) {
            String[] daysOfWeek = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
            return daysOfWeek[dayOfWeek - 1]; // Calendar starts with Sunday as 1
        } else {
            SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");
            return formatter.format(messageDate);
        }
    }
}