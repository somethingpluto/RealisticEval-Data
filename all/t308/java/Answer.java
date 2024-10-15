package org.real.temp;

import java.time.LocalDate;

public class Answer {

    /**
     * Gets the current date and returns it as YYYY-MM-DD
     *
     * @return The current date formatted as YYYY-MM-DD.
     */
    public static String getCurrentDate() {
        LocalDate currentDate = LocalDate.now();
        return currentDate.toString(); // This automatically formats as YYYY-MM-DD
    }

    public static void main(String[] args) {
        System.out.println(getCurrentDate());
    }
}