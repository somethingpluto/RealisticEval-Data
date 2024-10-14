package org.real.temp;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Answer {

    /**
     * Generate a formatted date range string.
     *
     * @param startDate The start date in 'YYYY-MM-DD' format.
     * @param endDate   The end date in 'YYYY-MM-DD' format.
     * @return A string representing the date range in a human-readable format.
     * @throws IllegalArgumentException If the startDate or endDate are not in the correct format or if startDate is after endDate.
     */
    public static String dateRangeString(String startDate, String endDate) throws IllegalArgumentException {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
        Date startDt, endDt;

        try {
            startDt = dateFormat.parse(startDate);
            endDt = dateFormat.parse(endDate);

            if (startDt.after(endDt)) {
                throw new IllegalArgumentException("startDate cannot be after endDate.");
            }
        } catch (ParseException e) {
            throw new IllegalArgumentException("Date must be in 'YYYY-MM-DD' format.", e);
        }

        SimpleDateFormat monthFormat = new SimpleDateFormat("MMMM");
        SimpleDateFormat dayFormat = new SimpleDateFormat("dd");
        SimpleDateFormat yearFormat = new SimpleDateFormat("yyyy");

        String startMonth = monthFormat.format(startDt);
        String endMonth = monthFormat.format(endDt);
        String startDay = dayFormat.format(startDt);
        String endDay = dayFormat.format(endDt);
        String startYear = yearFormat.format(startDt);
        String endYear = yearFormat.format(endDt);

        // Format output based on whether dates are within the same month and/or year
        if (!startYear.equals(endYear)) {
            return String.format("%s %s, %s to %s %s, %s", startMonth, startDay, startYear, endMonth, endDay, endYear);
        } else if (startMonth.equals(endMonth)) {
            return String.format("%s %s to %s, %s", startMonth, startDay, endDay, startYear);
        } else {
            return String.format("%s %s to %s %s, %s", startMonth, startDay, endMonth, endDay, startYear);
        }
    }

    // Example usage
    public static void main(String[] args) {
        try {
            System.out.println(dateRangeString("2023-01-01", "2023-01-31"));
            System.out.println(dateRangeString("2023-01-01", "2023-02-28"));
            System.out.println(dateRangeString("2023-01-01", "2024-02-28"));
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        }
    }
}
