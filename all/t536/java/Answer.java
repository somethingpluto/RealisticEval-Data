import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class Answer {
    /**
     * Gets the current date formatted as 'Month Day, Year'.
     *
     * @return The formatted date string.
     */
    public static String getDate() {
        // Create a new Date object representing the current date and time
        Date currentDate = new Date();

        // Define the date format
        SimpleDateFormat formatter = new SimpleDateFormat("MMMM d, yyyy", Locale.ENGLISH);

        // Return the formatted date string
        return formatter.format(currentDate);
    }

    public static void main(String[] args) {
        System.out.println(getDate());
    }
}