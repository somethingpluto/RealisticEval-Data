package org.real.temp;

public class Answer {
    public static int dayOfWeek(int year, int month, int day) {
        int[] t = { 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 };
        if (month < 3) {
            year -= 1;
        }
        int result = (year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7;
        return (result == 0) ? 7 : (result % 7); // Adjusted to correctly map Sunday as 7
    }
}