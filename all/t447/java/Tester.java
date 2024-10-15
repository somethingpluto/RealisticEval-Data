package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class Tester {

    @Test
    public void testCalculateAgeForBirthDateInThePast() {
        assertEquals(new Date().getYear() + 1900 - 2000, Integer.parseInt(calculateAge("2000-01-01")));
    }

    @Test
    public void testCalculateAgeForBirthDateInTheLongPast() {
        assertEquals(new Date().getYear() + 1900 - 1000, Integer.parseInt(calculateAge("1000-01-01")));
    }

    @Test
    public void testCalculateAgeForBirthDateToday() {
        String today = new SimpleDateFormat("yyyy-MM-dd").format(new Date());
        assertEquals(0, Integer.parseInt(calculateAge(today)));
    }

    @Test
    public void testCalculateAgeForPersonBornYesterday() {
        Calendar yesterday = Calendar.getInstance();
        yesterday.add(Calendar.DAY_OF_MONTH, -1); // Set to yesterday
        String birthDateString = new SimpleDateFormat("yyyy-MM-dd").format(yesterday.getTime());
        assertEquals(0, Integer.parseInt(calculateAge(birthDateString)));
    }
}