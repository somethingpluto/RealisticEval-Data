package org.real.temp;
public class Answer {
    
    public static double calculateDiscount(double originalPrice, double actualPrice) {
        // Validate input
        if (originalPrice <= 0) {
            throw new IllegalArgumentException("Original price must be greater than zero.");
        }
        if (actualPrice < 0) {
            throw new IllegalArgumentException("Actual price cannot be negative.");
        }

        // Calculate the discount
        double discountAmount = originalPrice - actualPrice;
        double discountPercentage = (discountAmount / originalPrice) * 100;

        // Return the discount percentage, rounded to two decimal places
        return Math.round(discountPercentage * 100.0) / 100.0;
    }
}