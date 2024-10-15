import java.util.regex.Pattern;

public class CoordinateValidator {

    public static boolean isValidCoordinate(String coord) {
        // Regular expression for latitude and longitude
        String latitudeRegex = "^[-+]?([1-8]?[0-9](\\.\\d+)?|90(\\.0+)?)([NnSs]?)$"; // -90 to 90 degrees
        String longitudeRegex = "^[-+]?((1[0-7][0-9]|[0-9]?[0-9])(\\.\\d+)?|180(\\.0+)?)([EeWw]?)$"; // -180 to 180 degrees

        // Check if the coordinate matches latitude or longitude format
        return Pattern.matches(latitudeRegex, coord) || Pattern.matches(longitudeRegex, coord);
    }
}