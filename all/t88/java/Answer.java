import java.util.Arrays;

public class CronChecker {
    public static boolean isCronBetween2And4AM(String cronExpression) {
        String[] parts = cronExpression.split(" ");
        String hourPart = parts[1];

        int[] hours = Arrays.stream(hourPart.split(","))
                            .mapToInt(Integer::parseInt)
                            .toArray();

        for (int hour : hours) {
            if (hour >= 2 && hour < 4) {
                return true;
            }
        }
        return false;
    }
}