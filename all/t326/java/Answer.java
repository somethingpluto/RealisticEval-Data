package org.real.temp;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class Answer {
    public static TimeDifference calculateTimeDifference(String givenDate) {
        Date dateToCompare = new Date(givenDate);
        Date currentDate = new Date();

        long differenceInMilliseconds = currentDate.getTime() - dateToCompare.getTime();

        if (differenceInMilliseconds < 0) {
            return new TimeDifference(0, 0, 0);
        }

        long minutes = TimeUnit.MILLISECONDS.toMinutes(differenceInMilliseconds);
        long hours = TimeUnit.MILLISECONDS.toHours(differenceInMilliseconds);
        long days = TimeUnit.MILLISECONDS.toDays(differenceInMilliseconds);

        long remainingHours = hours % 24;
        long remainingMinutes = minutes % 60;

        return new TimeDifference(days, remainingHours, remainingMinutes);
    }

    public static class TimeDifference {
        public long days;
        public long hours;
        public long minutes;

        public TimeDifference(long days, long hours, long minutes) {
            this.days = days;
            this.hours = hours;
            this.minutes = minutes;
        }
    }
}