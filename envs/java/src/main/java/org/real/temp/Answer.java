package org.real.temp;

    import java.util.ArrayList;
    import java.util.List;

    public class Answer {

        /**
         * Filters out the number of palindromes within any number n.
         * Palindrome numbers are numbers that read the same backward as forward,
         * such as 121, 1331.
         *
         * @param n the range number
         * @return a list of palindrome numbers
         */
        public static List<Integer> getPalindromeList(int n) {
            List<Integer> palindromeList = new ArrayList<>();
            int num = 1; // Start checking from 1

            // Using a while loop to iterate through numbers
            while (num <= n) {
                if (isPalindrome(num)) {
                    palindromeList.add(num);
                }
                num++;
            }

            return palindromeList;
        }

        private static boolean isPalindrome(int num) {
            String strNum = String.valueOf(num);
            String reversedNum = new StringBuilder(strNum).reverse().toString();
            return strNum.equals(reversedNum);
        }
    }