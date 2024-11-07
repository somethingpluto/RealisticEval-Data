package org.real.temp;

public class Answer {

    public static boolean isCronBetween2And4AM(String cronExpression) {
        // Split the cron expression by spaces
        String[] parts = cronExpression.split(" ");
        String hourPart = parts[1];

        // Split the hour part by commas and convert to integers
        String[] hourStrings = hourPart.split(",");
        for (String hourString : hourStrings) {
            try {
                int hour = Integer.parseInt(hourString);
                if (hour >= 2 && hour < 4) {
                    return true;
                }
            } catch (NumberFormatException e) {
                // In case of an invalid number, skip that part
                System.out.println("Invalid hour value: " + hourString);
            }
        }
        return false;
    }

    public static void main(String[] args) {
        // Example usage
        String cronExpression = "0 3 * * *";
        boolean result = isCronBetween2And4AM(cronExpression);
        System.out.println(result); // Output: true
    }
}
