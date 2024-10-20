package org.real.temp;
import java.util.Calendar;
import java.util.Date;

public class Answer {

    public static int[] getTimeSinceBornUntilNow(Date birthDate) {
        Calendar now = Calendar.getInstance();
        Calendar birth = Calendar.getInstance();
        birth.setTime(birthDate);

        // Calculate years
        int years = now.get(Calendar.YEAR) - birth.get(Calendar.YEAR);

        // Calculate months
        int months = now.get(Calendar.MONTH) - birth.get(Calendar.MONTH);
        if (months < 0) {
            years -= 1;
            months += 12;
        }

        // Calculate days
        int days = now.get(Calendar.DAY_OF_MONTH) - birth.get(Calendar.DAY_OF_MONTH);
        if (days < 0) {
            months -= 1;
            // Set tempDate to the same year and month as now, but the day from birthDate
            now.set(Calendar.DAY_OF_MONTH, 1); // First day of the current month
            now.add(Calendar.MONTH, -1); // Go to the previous month
            days += now.getActualMaximum(Calendar.DAY_OF_MONTH); // Get the last day of the previous month
            now.add(Calendar.MONTH, 1); // Go back to the current month
        }

        // Calculate hours
        int hours = now.get(Calendar.HOUR_OF_DAY) - birth.get(Calendar.HOUR_OF_DAY);
        if (hours < 0) {
            days -= 1;
            hours += 24;
        }

        // Calculate minutes
        int minutes = now.get(Calendar.MINUTE) - birth.get(Calendar.MINUTE);
        if (minutes < 0) {
            hours -= 1;
            minutes += 60;
        }

        return new int[]{years, months, days, hours, minutes};
    }
}