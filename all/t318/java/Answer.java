package org.real.temp;

public class Answer {
    public static int countNumbers(String str) {
        int numberCount = 0;

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c >= '0' && c <= '9') {
                numberCount++;
            }
        }

        return numberCount;
    }

    public static void main(String[] args) {
        String input = "Hello123";
        System.out.println(countNumbers(input)); // Example usage
    }
}