package org.real.temp;
public class Answer {
    public static String formatThreadCount(int count) {
        // Handle the case when there are no threads
        if (count == 0) {
            return "No Threads";
        }

        // Convert the count to a string and pad it to ensure at least 2 digits
        String threadCount = String.format("%02d", count);

        // Determine the correct word form based on the count
        String threadWord = (count == 1) ? "Thread" : "Threads";

        // Return the formatted string
        return threadCount + " " + threadWord;
    }
}