package org.real.temp;

public class Answer {
    public static int countDashes(String str) {
        int dashCount = 0;

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '-') {
                dashCount++;
            }
        }

        return dashCount;
    }

    public static void main(String[] args) {
        String input = "your-string-here"; // Replace with your input
        System.out.println(countDashes(input));
    }
}