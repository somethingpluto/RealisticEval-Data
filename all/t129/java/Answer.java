import java.util.regex.Pattern;

public class URLValidator {

    /**
     * Validates a URL string using a simplified and more comprehensive regular expression.
     *
     * @param str The URL string to validate.
     * @return True if the URL is valid, false otherwise.
     */
    public static boolean validURL(String str) {
        // Simplified and robust regex for URL validation
        String pattern = "^(http|https?:\\/\\/)?"
                + "((([a-zA-Z\\d]([a-zA-Z\\d-]*[a-zA-Z\\d])*)\\.)+[a-zA-Z]{2,}|"
                + "((\\d{1,3}\\.){3}\\d{1,3}))"
                + "(\\:\\d+)?"
                + "(\\/[-a-zA-Z\\d%_.~+]*)*"
                + "(\\?[;&a-zA-Z\\d%_.~+=-]*)?"
                + "(\\#[-a-zA-Z\\d_]*)?$";

        Pattern compiledPattern = Pattern.compile(pattern, Pattern.CASE_INSENSITIVE);
        return compiledPattern.matcher(str).matches();
    }

    public static void main(String[] args) {
        // Example usage
        String url = "https://www.example.com";
        System.out.println("Is the URL valid? " + validURL(url));
    }
}