package org.real.temp;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Checks if the provided image data is a valid Base64 encoded image string.
     *
     * @param imageData - The image data string to be validated.
     * @returns - Returns true if valid, otherwise false.
     */
    public static boolean isBase64Image(String imageData) {
        // Check if the input is a non-empty string
        if (imageData == null || imageData.trim().isEmpty()) {
            return false;
        }

        // Regular expression to validate a Base64 image string
        String base64ImagePattern = "^data:image/(jpeg|png|gif|bmp|webp);base64,[A-Za-z0-9+/]+={0,2}$";
        
        // Test the image data against the pattern
        return Pattern.matches(base64ImagePattern, imageData);
    }
}