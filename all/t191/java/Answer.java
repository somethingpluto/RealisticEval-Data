package org.real.temp;

public class Answer {

    public static String floatToHex(float value) {
        // Interpret the float's bit pattern as an unsigned integer
        int intRepresentation = Float.floatToIntBits(value);

        // Convert the unsigned integer to a hexadecimal string
        String hexString = String.format("%08x", intRepresentation);
        
        return hexString;
    }

    public static void main(String[] args) {
        // Example usage
        float exampleValue = 3.14f;
        String hexValue = floatToHex(exampleValue);
        System.out.println("Hexadecimal representation: " + hexValue);
    }
}