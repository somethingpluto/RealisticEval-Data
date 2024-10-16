package org.real.temp;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Calendar;

public class Answer {
    public static String calculateAge(String birthDateString) {
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
        Date birthDate;
        
        try {
            birthDate = format.parse(birthDateString);
        } catch (ParseException e) {
            return "Invalid date format. Please enter a valid date.";
        }

        Calendar today = Calendar.getInstance();
        Calendar birth = Calendar.getInstance();
        birth.setTime(birthDate);

        int age = today.get(Calendar.YEAR) - birth.get(Calendar.YEAR);
        if (today.get(Calendar.MONTH) < birth.get(Calendar.MONTH) ||
            (today.get(Calendar.MONTH) == birth.get(Calendar.MONTH) && today.get(Calendar.DAY_OF_MONTH) < birth.get(Calendar.DAY_OF_MONTH))) {
            age--;
        }

        return String.valueOf(age);
    }
}