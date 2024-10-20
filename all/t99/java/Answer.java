package org.real.temp;

public class Answer {

    /**
     * Greets someone with a personalized message.
     * 
     * @param name The name to include in the personalized message.
     */
    public static void greet(String name) {
        if (name == null || name.trim().isEmpty()) {
            System.out.println("Hello, Guest!");
        } else {
            System.out.println("Hello, " + name.trim() + "!");
        }
    }

    /**
     * Calculates the sum of all elements in an array.
     * 
     * @param arr The array of numbers to sum.
     * @return The sum of all elements of the array.
     */
    public static int sum(int[] arr) {
        if (arr == null) {
            throw new IllegalArgumentException("Expected an array of numbers");
        }

        int total = 0;
        for (int num : arr) {
            total += num;
        }
        return total;
    }
}