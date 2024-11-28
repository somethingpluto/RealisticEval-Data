package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Filters out the number of palindromes within any number n.
     * Palindrome numbers are numbers that read the same backward as forward, such as 121, 1331.
     *
     * @param n the range number
     * @return a list of palindrome numbers
     */
    public static List<Integer> getPalindromeList(int n) {
        List<Integer> palindromeNumbers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (isPalindrome(i)) {
                palindromeNumbers.add(i);
            }
        }
        return palindromeNumbers;
    }

    /**
     * Checks if a given number is a palindrome.
     *
     * @param number the number to check
     * @return true if the number is a palindrome, false otherwise
     */
    private static boolean isPalindrome(int number) {
        String numStr = Integer.toString(number);
        String reversedStr = new StringBuilder(numStr).reverse().toString();
        return numStr.equals(reversedStr);
    }

    // Example usage
    public static void main(String[] args) {
        List<Integer> palindromes = getPalindromeList(150);
        System.out.println(palindromes);
    }
}