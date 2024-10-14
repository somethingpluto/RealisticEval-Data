import java.util.Calendar;
import java.util.GregorianCalendar;

public class TimestampConverter {
    public static String timestampToReadableDate(long unixTimestamp) {
        // Convert UNIX timestamp to milliseconds
        long millis = unixTimestamp * 1000;
        
        // Create a calendar instance
        Calendar calendar = new GregorianCalendar();
        calendar.setTimeInMillis(millis);
        
        // Month names
        String[] monthNames = {
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        };
        
        // Get month, day, hours, and minutes
        String month = monthNames[calendar.get(Calendar.MONTH)];
        int day = calendar.get(Calendar.DAY_OF_MONTH);
        int hours = calendar.get(Calendar.HOUR_OF_DAY);
        String minutes = String.format("%02d", calendar.get(Calendar.MINUTE));
        
        // Return formatted date string
        return String.format("%s %d, %d:%s", month, day, hours, minutes);
    }

    public static void main(String[] args) {
        long timestamp = 1633072800; // Example timestamp
        String readableDate = timestampToReadableDate(timestamp);
        System.out.println(readableDate);
    }
}