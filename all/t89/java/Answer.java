public class TimeUtil {
    public static String timePassed(long startTimeInMillis) {
        // Get the current time in milliseconds
        long currentTimeInMillis = System.currentTimeMillis();

        // Calculate the difference in milliseconds
        long timeDifference = currentTimeInMillis - startTimeInMillis;

        // Convert the difference to seconds
        long totalSeconds = timeDifference / 1000;

        // Calculate minutes and seconds
        long minutes = totalSeconds / 60;
        long seconds = totalSeconds % 60;

        // Return the formatted string
        return String.format("%d:%02d", minutes, seconds);
    }

    public static void main(String[] args) {
        // Example usage
        long startTime = System.currentTimeMillis() - 65000; // 65 seconds ago
        System.out.println(timePassed(startTime)); // Output: "1:05"
    }
}