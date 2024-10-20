package org.real.temp;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Answer {
    public static String formatDate(String dateString) throws IllegalArgumentException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");
        Date date;

        try {
            date = sdf.parse(dateString);
        } catch (ParseException e) {
            throw new IllegalArgumentException("Invalid Date");
        }

        Date currentDate = new Date();
        long timeDifference = currentDate.getTime() - date.getTime();

        // Calculate time differences in seconds, minutes, hours, and days
        long secondsDifference = timeDifference / 1000;
        long minutesDifference = secondsDifference / 60;
        long hoursDifference = minutesDifference / 60;
        long daysDifference = hoursDifference / 24;

        // Determine and return the appropriate time description
        if (daysDifference > 0) {
            return daysDifference + " day" + (daysDifference != 1 ? "s" : "") + " ago";
        } else if (hoursDifference > 0) {
            return hoursDifference + " hour" + (hoursDifference != 1 ? "s" : "") + " ago";
        } else if (minutesDifference > 0) {
            return minutesDifference + " minute" + (minutesDifference != 1 ? "s" : "") + " ago";
        } else {
            return secondsDifference + " second" + (secondsDifference != 1 ? "s" : "") + " ago";
        }
    }
}