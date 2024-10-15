package org.real.temp;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Answer {

    public static String calculateAge(String birthDateString) {
        if (birthDateString == null || birthDateString.isEmpty()) {
            return "";
        }

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        Date birthDate;
        try {
            birthDate = sdf.parse(birthDateString);
        } catch (ParseException e) {
            return "";
        }

        Date today = new Date();
        int age = today.getYear() + 1900 - birthDate.getYear(); // getYear() returns year since 1900

        boolean isBirthdayPassed = today.getMonth() > birthDate.getMonth() ||
                (today.getMonth() == birthDate.getMonth() && today.getDate() >= birthDate.getDate());

        if (!isBirthdayPassed) {
            age--;
        }

        return birthDateString + " (" + age + ")";
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(calculateAge("2000-01-15")); // Change the date string as needed
    }
}