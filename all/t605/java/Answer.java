package org.real.temp;


public class Answer {
    
    public static double calculateBMI(double weight, double height) {
        // Validate weight and height
        if (weight <= 0) {
            throw new IllegalArgumentException("Weight must be greater than zero.");
        }
        if (height <= 0) {
            throw new IllegalArgumentException("Height must be greater than zero.");
        }

        // Calculate BMI
        double bmi = weight / (height * height);
        return bmi; // Return the calculated BMI value
    }
}