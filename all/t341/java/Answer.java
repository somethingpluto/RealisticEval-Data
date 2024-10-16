import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TimeConverter {

    /**
     * Converts a time string in the format "XhYmZs" (hours, minutes, seconds) into milliseconds.
     *
     * @param str The input string representing the time duration.
     * @returns The time in milliseconds.
     * @throws IllegalArgumentException if the input string does not match the expected format.
     */
    public static long convertTimeHmsStringToMs(String str) {
        Pattern regex = Pattern.compile("(?:(\\d+)h)?(?:(\\d+)m)?(?:(\\d+)s)?");
        Matcher match = regex.matcher(str);

        if (!match.matches()) {
            throw new IllegalArgumentException("Cannot convert hms string \"" + str + "\" to ms!");
        }

        int hours = match.group(1) != null ? Integer.parseInt(match.group(1)) : 0;
        int minutes = match.group(2) != null ? Integer.parseInt(match.group(2)) : 0;
        int seconds = match.group(3) != null ? Integer.parseInt(match.group(3)) : 0;

        long totalMilliseconds = ((hours * 60 + minutes) * 60 + seconds) * 1000;
        return totalMilliseconds;
    }
}