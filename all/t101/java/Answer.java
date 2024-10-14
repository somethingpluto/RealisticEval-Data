public class BreakTimeChecker {
    /**
     * Determines if the current time falls within the break time range.
     * 
     * @param startTime - The start time of the break in HH:MM format.
     * @param endTime - The end time of the break in HH:MM format.
     * @param currentTime - The current time in HH:MM format.
     * @returns boolean - Returns true if the current time is within the break time range, false otherwise.
     */
    public static boolean isBreakTime(String startTime, String endTime, String currentTime) {
        int[] start = parseTime(startTime);
        int[] end = parseTime(endTime);
        int[] current = parseTime(currentTime);

        int startTotalMinutes = start[0] * 60 + start[1];
        int endTotalMinutes = end[0] * 60 + end[1];
        int currentTotalMinutes = current[0] * 60 + current[1];

        return currentTotalMinutes >= startTotalMinutes && currentTotalMinutes <= endTotalMinutes;
    }

    private static int[] parseTime(String time) {
        String[] parts = time.split(":");
        return new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])};
    }
}