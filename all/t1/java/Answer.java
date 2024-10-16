package org.real.temp;

public class Answer {
    public static Object numericalStrConvert(String value) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            try {
                return Float.parseFloat(value);
            } catch (NumberFormatException ex) {
                return value;
            }
        }
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(numericalStrConvert("123")); // Should print 123 as an integer
        System.out.println(numericalStrConvert("123.456")); // Should print 123.456 as a float
        System.out.println(numericalStrConvert("abc")); // Should print "abc" as a string
    }
}