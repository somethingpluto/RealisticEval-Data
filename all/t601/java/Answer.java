package org.real.temp;

import java.util.Scanner;

public class Answer {
    
    public static int countWords(String str) {
        // Initialize a word count variable
        int wordCount = 0;
        
        // Create a Scanner to parse the input string
        Scanner scanner = new Scanner(str);
        
        // Extract words from the scanner
        while (scanner.hasNext()) {
            scanner.next(); // Move to the next word
            wordCount++; // Increment the count for each word found
        }
        
        scanner.close(); // Close the scanner
        return wordCount; // Return the total word count
    }

    public static void main(String[] args) {
        // Example usage
        String input = "Hello, this is an example string.";
        int count = countWords(input);
        System.out.println("Word count: " + count);
    }
}